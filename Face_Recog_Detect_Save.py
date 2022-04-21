#                  FUNCTIONALITY OF THE CODE

#This code imports the face detection algorithm from the local folder (in DE10 Nano)
# and initiates face detections count and distancr predictions algorithm to the detected face.  

#If the face is inside a permittable range of 2 meters then the face detections count will increase.

#If the face detection count reaches up to a maximum of 10 detections inside the range,
#  then the face recongition code will tend to activate from the Cloud dcker resource section

#If the deted face recognized as one of the face of the stored faces, then the device will generates
#  a voice output with the name of the person.

#If the face is not recognized, then the device will asks the user to save the face of the person or not.

#If the user's choice is yes, then the device asks the user to say the name of the person.

#Then after recieving the name, then that face will be saved in the daved faces folder in the local machine.

#And from the next iteration the saved face will also be recognized.

#Finally the block will end if the duration time is exceeded.


import cv2

import time

import gpioaccess as gp # to activate trigger to send the serial data to Raspberry pi

import facedetect_distance as fdd  # For face_detection count triggering

import voice_input as vi #for recieving the name of the person to save in the database

import voice_output as vo #For generating the voice output to enter the name

import voice_send as vs#For sending the detected face name to Raspberry pi


from cloud_codes import face_test #Importing the face recognition code from the cloud docker resource 


#Initializing the camera
vid -cv2.VideoCapture(0)


def final(vid,duration):

    #Initial time of starting the block
    init_time = time.time()    

    #Initially set the face detection count =0
    face_detect_count=0
    
    while(vid.isOpened()):
        ret,img=vid.read()

        #Initiaslizing face_detection algorithm and obtaining the distance from the camera.
        face_list=fdd.face()

        #If the detected face is in the range of 2 meters then the face detection count will increase.
        if(face_list[0]<=200):

            face_detect_count +=1
            #If there are 10 continious face detections in 2 meter range then the face recognition code executes.
            if(face_detect_count == 10):

                
                #Running face recongition block from the cloud.
                result=face_test.recognize(img)
                    
                #predicted name of the face will be obtained
                name=result['prediction']
                
                #If a person face is identified in the saved faces,
                if(name != 'Unknown'):

                    #It generates a voice output with the name of the person
                    text= name+ "is infront of you"
                    
                    vo.send(text)

                elif(response == unknown):

                    #voice output code = 01110 -->  A person is near you Do you want to save the name of the person
                    vo.output([0,1,1,1,0])

                    #getting user's choice
                    choice=vi.voice()

                    if(choice=='yes'):

                        #voice output code = 01111 --> Say the Name of the person.
                        vo.output([0,1,1,1,1])

                        #Recieving name of the person
                        name = vi.voice()

                        #Saving the face image with the recieved name of the person.
                        img_name = 'saved_faces/' + name + '.jpg'
                        cv2.imwrite(img_name,img)

                #Finally resets the face detections coutn to 0
                face_detect_count = 0
                
        #Final time to record
        final_time = time.time()

        #If the duration of the block is greater than the required duration, then the block will end
        if((final_time-init_time)>= duration):
            break

        
            
            
