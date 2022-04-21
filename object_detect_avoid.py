#                               WORKING PRINCIPLE OF THE CODE

#This code runs on the basis of the recognized samples of the obj_test code in the Cloud Deocker resource section.
#The object recognition process works on the basis of cvlib which usually trains the YOLOV3 dataset as the reference models
#YOLOV3 consists of 80 predefined real time object models and are trained using Tensorflow.

#If an object is detected, then a voice ouput will be generated with name of the objec talong wtth the direction of detection.

#Here some of the models are defined to be as obstacles and remaining are considered as non obstacles.
#The bounding box coordinates of the obstacles are to be recorded and the central coordinates are to be calculated.
#Based on the central coordinates, the device takes a decesion to direct the user in an appropriate direction inorder to 
#  avoid the obstacle.

#Finally if the required duration time is exceeded the complete block will be terminated.

import time

import cv2

from cloud_codes import obj_test #For performing object detectiona and recognition from the cloud section.

import voice_send as vs #For sending voice output with the name of the object detected and the direction to move to navigate safe.

vid.cv2.VideoCapture(0)

def obj_det_avd(vid,duration):
    
    #Initial time of starting the block
    init_time = time.time()    

    while vid.isOpened():

        ret,img=vid.read()
        
        #Calling the objeect recognition block from the cloud section
        result = obj_test.recog_obj(img)
        
        label = result[0]
        bbox  = result[1]
    
        #obstacles list which are to be avoided by the user excluding the case of Navigation 
        obst_list=['bench','dog','motorcycle','bus','car','truck','chair']

        for i in range(len(label)):
        
            #Name of the detected object.
            name=label[i]

            x1=bbox[i][0]
            y1=bbox[i][1]
            x2=bbox[i][2]
            y2=bbox[i][3]

            #Plotting a boundary rectangle on the frame size 450 X 450 for pixel sectional division
            cv2.rectangle(img,(200,50),(650,500),(255,0,0),2)
    
            #Dividing the boundary rectangle into three regions.
            cv2.line(img,(350,50),(350,500),(255,0,0),2)
            cv2.line(img,(500,50),(500,500),(255,0,0),2)
    
            #Center point og the bounding box
            xcp=(x1+x2)//2
            ycp=(y1+y2)//2
    
            if(xcp>200 and xcp<350):
    
                #If an object is detected at front left corner
                #Sending voice output with name of the object along with the direction it is detected. 
                vs.send("a "+name+" is detected at front left corner")
    
                #Direction of detection
                direc = "front_left"
    
            elif(xcp>350 and xcp<500):
    
                #If an object is detected at front
                #Sending voice output with name of the object along with the direction it is detected. 
                vs.send("a "+name+" is detected in front of you")
    
                #Direction of detection
                direc="infront"
            elif(xcp>500 and xcp<650):
    
                #If an object is detected at front right corner
                #Sending voice output with name of the object along with the direction it is detected. 
                vs.send("a "+name+" is detected at front right corner")
    
                #Direction of detection
                direc="front_right"
    
            #If any object is considered as obstacle
            if label[i] in obst_list:
    
                #and if the obstacle is infront of the user
                if(direc=="infront"):
    
                    #sending output to change direction to eliminate the obstacle in the path. 
                    vs.send("Move to your front left side to eliminate the "+name)

        #Final time to record
        final_time = time.time()

        #If the duration of the block is greater than the required duration, then the block will end
        if((final_time-init_time)>= duration):
            break
    
    
    
        
