from django.shortcuts import HttpResponseRedirect
from datetime import datetime

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

def generate_badge(request, member_id, tutor):
    student = StudentMembership.objects.get(id=member_id)

    BASE_DESTINATION= os.path.join(BASE_DIR, "static/images/Badges/")
    if not os.path.exists(BASE_DESTINATION):
        os.makedirs(BASE_DESTINATION)

    try:        
        student_name=student.student_name
        student_course=str(student.course)
        tutor_name=tutor.username
        date = str(datetime.today().strftime('%d-%m-%Y'))

    
        # enter badge image template
        imgpath = os.path.join(BASE_DIR,"static/images/Badges/input_image.jpg")
        img = cv.imread(imgpath, 1)

        # enter the centers; this can be found using ms-paint
        center_1 = [2230,1006] # tutor name 1
        center_2 = [1180,1165] # student name
        center_3 = [1960,1340] # student_course
        center_4 = [1070,1830] # tutor name 1
        center_5 = [2450,1835] # date


        font = cv.FONT_HERSHEY_TRIPLEX
        size_of_font = 40 

        #calculating starts of each blank
        start_1 = calc_start(center_1, tutor_name,    size_of_font)
        start_2 = calc_start(center_2, student_name,   size_of_font)
        start_3 = calc_start(center_3, student_course,      size_of_font)
        start_4 = calc_start(center_4, tutor_name,  size_of_font)
        start_5 = calc_start(center_5, date,  size_of_font)

        cv.putText(img, tutor_name,    tuple(start_1), font, 2, (0,0,0), 2, cv.LINE_AA)
        cv.putText(img, student_name,  tuple(start_2), font, 2, (0,0,0), 2, cv.LINE_AA)
        cv.putText(img, student_course,tuple(start_3), font, 2, (0,0,0), 2, cv.LINE_AA)
        cv.putText(img, tutor_name,    tuple(start_4), font, 2, (0,0,0), 2, cv.LINE_AA)
        cv.putText(img, date,          tuple(start_5), font, 2, (0,0,0), 2, cv.LINE_AA)

        img_path1 = str(BASE_DESTINATION) + str(student.id) + '.jpg'
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
