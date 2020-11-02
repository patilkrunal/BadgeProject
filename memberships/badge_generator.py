from django.shortcuts import HttpResponseRedirect
from BadgeProject.settings import BASE_DIR

import csv
import os
import PIL
import cv2 as cv


def generate_badge(request):

    def calc_start(center,arr,size_of_font):
        length = len(arr)
        center[0] = int(center[0] - size_of_font * (length/2))
        return center

    BASE_DESTINATION= os.path.join(BASE_DIR,"static/images/Badges/")
    if not os.path.exists(BASE_DESTINATION):
        os.makedirs(BASE_DESTINATION)

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
                    # #enter destination
                    # destination = BASE_DESTINATION

                    #enter template
                    imgpath = os.path.join(BASE_DIR,"static/images/Badges/input_image.jpg")
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

                    img_path = str(destination) + str(unique_id_list[i]) + '.jpg'
                    cv.imwrite(img_path, img)

                    print('******************************************************')
                    print(f'***    SUCCESS IN CREATING BADGE {i+1}/{len(name_list)}   ***')
                    print('******************************************************')
                    print(f"")

                    img_path1="/".join( img_path.split('/')[-5:] )
                    
                    print('***************************************')
                    print(img_path1)
                    print('***************************************')
                    
                    return img_path1

                except:
                    print("Something went wrong")
        except:
            print(f"file is not proper format: {arr[i]}")
