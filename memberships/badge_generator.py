from django.shortcuts import HttpResponseRedirect
from BadgeProject.settings import BASE_DIR
from memberships.models import StudentMembership

import cv2 as cv
import PIL
import os
import csv

def calc_start(center,arr,size_of_font):
    length = len(arr)
    center[0] = int(center[0] - size_of_font * (length/2))
    return center

def generate_badge(request, member_id):
    student = StudentMembership.objects.get(id=member_id)

    BASE_DESTINATION= os.path.join(BASE_DIR, "static/images/Badges/")
    if not os.path.exists(BASE_DESTINATION):
        os.makedirs(BASE_DESTINATION)

    try:        
        student_name=student.student_name
        student_email=student.email_id
        student_id=str(student.id)
        student_course=str(student.course)
    
        # enter badge image template
        imgpath = os.path.join(BASE_DIR,"static/images/Badges/input_image.jpg")
        img = cv.imread(imgpath, 1)

        # enter the centers; this can be found using ms-paint
        center_1 = [1800,1375] #name
        center_2 = [1800,1540] #student_email
        center_3 = [1430,1715] #student_id
        center_4 = [2535,1715] #student_course

        font = cv.FONT_HERSHEY_TRIPLEX
        #font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
        size_of_font = 40 

        #calculating starts of each blank
        start_1 = calc_start(center_1, student_name,    size_of_font)
        start_2 = calc_start(center_2, student_email,   size_of_font)
        start_3 = calc_start(center_3, student_id,      size_of_font)
        start_4 = calc_start(center_4, student_course,  size_of_font)

        cv.putText(img, student_name,   tuple(start_1), font, 2, (0,0,0), 2, cv.LINE_AA)
        cv.putText(img, student_email,  tuple(start_2), font, 2, (0,0,0), 2, cv.LINE_AA)
        cv.putText(img, student_id,     tuple(start_3), font, 2, (0,0,0), 2, cv.LINE_AA)
        cv.putText(img, student_course, tuple(start_4), font, 2, (0,0,0), 2, cv.LINE_AA)

        img_path1 = str(BASE_DESTINATION) + str(student_id) + '.jpg'
        cv.imwrite(img_path1, img)

        img_path2="/".join( img_path1.split('/')[-3:] )

        print('*****************************************')
        print(f'***    SUCCESS IN GENERATING BADGE   ***')
        print('*****************************************')
        print(f'{img_path2}')
        print('*****************************************')
        
        return img_path2
    except:
        print("Something went wrong while generating badge image")
