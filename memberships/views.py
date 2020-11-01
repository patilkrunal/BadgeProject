from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.views import generic

import csv
import os
import PIL
import cv2 as cv

from BadgeProject.settings import BASE_DIR
from .models import StudentMembership
from courses.models import Course
from . import forms


class StudentsListView(generic.ListView):
    model = StudentMembership
    template_name = 'memberships/membership_list.html'

    def get_context_data(self, **kwargs):
        context = super(StudentsListView, self).get_context_data(**kwargs)
        student_membership_qs = StudentMembership.objects.all()
        list = [l for l in [s for s in student_membership_qs]]
        context= {'student_membership_qs': list}
        return context

    @login_required
    def add_members(request):
      if request.method == 'POST':
        form = forms.AddMembers(request.POST, request.FILES)
        if form.is_valid():
          instance = form.save(commit=False)
          instance.author = request.user
          instance.save()
          return redirect('courses:course_list')
      else:
        form = forms.AddMembers()
      return render(request, 'memberships/add_members.html', { 'form': form })


# class CourseDetailRedirect(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         try:
#           pk = self.args.get('pk')
#         except:
#           pk=1
        
#         try:
#           course = Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#           course = Course.objects.get(pk=1)
        
#         return reverse('courses:course_detail', course.slug)


from django.db.models import Q
class SearchResultsView(generic.ListView):
    model = StudentMembership
    template_name = 'memberships/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = StudentMembership.objects.filter(
            Q(email_id__icontains=query) | Q(student_name__icontains=query)
        )

        output_file_path = BASE_DESTINATION= os.path.join(BASE_DIR,"input.csv")
        with open(output_file_path, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)

            for member in object_list:
                writer.writerow([member.student_name, member.email_id, member.id, member.course])

        return object_list

    def press_my_buttons(request):
        if request.POST:
            # Run your script here
            print("Got the POST request")
        return render(request, 'memberships/search_results.html')


def submit(request):
    # function to calculate the start for each blank depending on size of string to be filled
    def calc_start(center,arr,size_of_font):
        length = len(arr)
        center[0] = int(center[0] - size_of_font * (length/2))
        return center

    BASE_DESTINATION= os.path.join(BASE_DIR,"static/images/Badges/teams/")
    included_ext = ['csv']
    
    # returns all csv files in the current directory
    arr=[fn for fn in os.listdir() if any(fn.endswith(ext) for ext in included_ext)]
    no_of_files = len(arr)

    #start printing
    for i in range(no_of_files):
        try:
            group = arr[i]
            print('*****   ' + arr[i] + '   *****')

            # with open(arr[i]) as csv_file:
            #     csv_reader = csv.reader(csv_file, delimiter=',')
            #     for row in csv_reader:
            #         print(row)
            # print('//////////////////////////////////////////')
            
            name_list=[]
            email_list=[]
            unique_id_list=[]
            course_list = []

            with open(group) as csv_file:
                csv_reader = csv.reader(csv_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
                
                for row in csv_reader:
                    name_list.append(row[0])
                    email_list.append(row[1])
                    unique_id_list.append(row[2])
                    course_list.append(row[3])

            print('==============')
            print(name_list)
            print(email_list)
            print(unique_id_list)
            print(course_list)
            print('==============')
            
            # OPENCV2 CONFIGURATION FILES
            from os import environ
            environ["QT_DEVICE_PIXEL_RATIO"] = "0"
            environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
            environ["QT_SCREEN_SCALE_FACTORS"] = "1"
            environ["QT_SCALE_FACTOR"] = "1"

            #print certificates
            for i in range(0, len(name_list)):
                try:
                    #enter destination
                    destination = BASE_DESTINATION + course_list[i] + '/'
                    if not os.path.exists(destination):
                        os.makedirs(destination)

                    #enter template
                    imgpath = os.path.join(BASE_DIR,"static/images/Badges/achievementsports.jpg")
                    img = cv.imread(imgpath, 1)
                    
                    # # Displaying the image 
                    # cv.imshow('image', img)
                    # cv.waitKey(0)

                    #enter the centers; this can be found using paint
                    center_1 = [1800,1375] #name
                    center_2 = [1800,1540] #college
                    center_3 = [1430,1715] #position like first/second
                    center_4 = [2535,1715] #sport

                    font = cv.FONT_HERSHEY_TRIPLEX
                    #font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
                    size_of_font = 40 

                    #calculating starts of each blank
                    start_1 = calc_start(center_1,name_list[i],size_of_font)
                    start_2 = calc_start(center_2,email_list[i],size_of_font)
                    start_3 = calc_start(center_3,unique_id_list[i],size_of_font)
                    start_4 = calc_start(center_4,course_list[i],size_of_font)

                    cv.putText(img,name_list[i],tuple(start_1), font, 2,(0,0,0),2,cv.LINE_AA)
                    cv.putText(img,email_list[i],tuple(start_2), font, 2,(0,0,0),2,cv.LINE_AA)
                    cv.putText(img,unique_id_list[i],tuple(start_3), font, 2,(0,0,0),2,cv.LINE_AA)
                    cv.putText(img,course_list[i],tuple(start_4), font, 2,(0,0,0),2,cv.LINE_AA)

                    img_path = str(destination) + str(name_list[i]) + '_' + str(unique_id_list[i]) + '.jpg'
                    cv.imwrite(img_path, img)

                    print('***************************************')
                    print('***    SUCCESS IN CREATING BADGE    ***')
                    print('***************************************')
                    # print(f"{i+1}/{len(name)}")

                    img_path1="/".join( img_path.split('/')[-5:] )
                    context = {
                        'img_url': img_path1
                    }
                    
                    print('***************************************')
                    print(img_path1)
                    print('***************************************')

                    return render(request,'memberships/view_badge.html',context)

                except:
                    print("Something went wrong")
        except:
            print(f"file is not proper format: {arr[i]}")
