import cv2

import time

import gpioaccess as gp # to activate trigger to send the serial data to Raspberry pi

import facedetect_distance as fdd  # For face_detection count triggering

import voice_input as vi #for recieving the name of the person to save in the database

import voice_output as vo #For generating the voice output to enter the name

import voice_send as vs#For sending the detected face name to Raspberry pi


from cloud_codes import face_test #Importing the face recognition code from the cloud docker resource 


def final(vid):

    #Initially set the face detection count =0
    face_detect_count=0
    
    while(vid.isOpened()):
        ret,img=vid.read()

        #Initiaslizing face_detection algorithm and obtaining the distance from the camera.
        face_list=fdd.face()

        #If the detected face is in the range of 2 meters then the face detection count will increase.
        if(face_list[0]<=200):

            #If there are 10 continious face detections in 2 meter range then the face recognition code executes.
            if(face_detect_count == 10):
                

                if(name != 'Unknown'):
                    #Running face recongition block from the cloud.
                    result=face_test.recognize(img)
                    
                    #predicted name of the face will be obtained
                    name=result['prediction']
    
                    text= name+ "is infront of you"
                    
                    vo.send(text)

                elif(response == unknown):

                    #voice output code = 01110 -->  A person is near you Do you want to save the name of the person
                    vo.output([0,1,1,1,0])
                                        
                    

                    
            
            
