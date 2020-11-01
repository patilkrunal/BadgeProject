import PIL
import csv
import os
import cv2 as cv

#function to calculate the start for each blank depending on size of string to be filled
def calc_start(center,arr,size_of_font):
    length = len(arr)
    center[0] = int(center[0] - size_of_font * (length/2))
    return center

#read all csv files and enter destination
base_destination = 'teams/'
included_ext = ['csv']
# returns all csv files in the current directory
arr=[fn for fn in os.listdir() if any(fn.endswith(ext) for ext in included_ext)]
no_of_files = len(arr)

#start printing
for i in range(no_of_files):
    try:
        group = arr[i]
        print(arr[i])

        #read csv and store values in arrays
        name=[]
        position=[]
        sport=[]
        college = []
        with open(group) as file:
            data=csv.reader(file, delimiter=',')
            count=0
            for row in data:
                count+=1
                if(count==1):
                    continue
                name.append(row[0])
                college.append(row[1])
                position.append(row[2])
                sport.append(row[3])
                   
        print(name[0])
        print(college[0])
        print(position[0])
        print(sport[0])

        #print certificates
        for i in range(0, len(name)):
            try:
                #enter destination
                destination = base_destination + college[i] + '/' + sport[i] + '/'
                if not os.path.exists(destination):
                    os.makedirs(destination)

                #enter template
                img = cv.imread("achievementsports.jpg")

                #enter the centers; this can be found using paint
                center_1 = [1800,1375] #name
                center_2 = [1800,1540] #college
                center_3 = [1430,1715] #position like first/second
                center_4 = [2535,1715] #sport

                font = cv.FONT_HERSHEY_TRIPLEX
                #font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
                size_of_font = 40 


                #calculating starts of each blank
                start_1 = calc_start(center_1,name[i],size_of_font)
                start_2 = calc_start(center_2,college[i],size_of_font)
                start_3 = calc_start(center_3,position[i],size_of_font)
                start_4 = calc_start(center_4,sport[i],size_of_font)

                cv.putText(img,name[i],tuple(start_1), font, 2,(0,0,0),2,cv.LINE_AA)
                cv.putText(img,college[i],tuple(start_2), font, 2,(0,0,0),2,cv.LINE_AA)
                cv.putText(img,position[i],tuple(start_3), font, 2,(0,0,0),2,cv.LINE_AA)
                cv.putText(img,sport[i],tuple(start_4), font, 2,(0,0,0),2,cv.LINE_AA)

                cv.imwrite(destination+ name[i] + '_' + sport[i] + '.jpg',img)

                print(f"{i+1}/{len(name)}")
            except:
                print("Something went wrong")

    except:
        print(f"file is not proper format: {arr[i]}")
        