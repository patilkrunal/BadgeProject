from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.shortcuts import render, redirect
from django.views import generic
from django.db.models import Q
import csv, os

from memberships.models import StudentMembership
from qrcodeapp.models import QRcodeModel
from courses.models import Course

from memberships.badge_generator import generate_badge
from memberships.forms import AddMembers
from BadgeProject.settings import BASE_DIR


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
            form = AddMembers(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()

                return redirect('courses:course_list')
        else:
            form = AddMembers()
        
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


class SearchResultsView(generic.ListView):
    model = StudentMembership
    template_name = 'memberships/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')               # accept the search term and put it in query variable
        if query:                                       # if the query variable is not none
            object_list = StudentMembership.objects.filter(     # filter the StudentMembership model to check if query exists in Q(email_id) or in (student_name)
                Q(email_id__icontains=query) | Q(student_name__icontains=query) # if it exists create list in object list
            )

            # output_file_path = os.path.join(BASE_DIR, "input.csv")      # dump whole object_list in input.csv file 
            # with open(output_file_path, 'w', newline='') as file:
            #     writer = csv.writer(file, quoting=csv.QUOTE_ALL)

            #     for member in object_list:
            #         writer.writerow([member.student_name, member.email_id, member.id, member.course])

            return object_list      # return the object list


def badge_generator_view(request, member_id):
    
    context = {
        'img_url': generate_badge(request, member_id)
    }

    return render(request, 'memberships/badge_wIth_QRcode.html', context)