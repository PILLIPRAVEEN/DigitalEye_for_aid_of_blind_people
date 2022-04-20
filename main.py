#                       DESCRIPTION OF THE CODE

#This file is completely based on the nested file handling techniques to import various functionalities of the design.

#Each functionality of the block is equipped with a trigger to activate the corresponding block

#This device main code is completely operates based on the priority conditions of the activated blocks.

import time

import cv2

import gpioaccess as gp

import voice_output as vo               #For generating voice instructions

from Navigation import navigation       #For performing Navigation block including vehcile avoidance

import Face_Recog_Detect_Save as frds   #For performing face detection and reecogntion including the storage of known faces

from cloud_codes import obj_test        #For detection and reecognization of common objects

import object_detect_avoid as oda            #For performing the obstacle avoidance. 


#EXTERNAL TRIGGERS :

#These external triggers are the user choice switches, in which each switch trigger a unique feature to activate

Navigate_vehicle_avoid_GPIO =  1803     #Switch to activate the navigation block and the vehicle avoidance block in the path.

Face_detect_recognize_GPIO  =  1804     #Switch to activate the face detection and recognition and to store the known faces of the user.

Text_detect_recognize_GPIO  =  1805     #Switch to activate the text detection and recognization block of the device

Object_detect_avoid_GPIO    =  1806     #Switch to activate the common object detection excluding navigation block

#Here our device is designed in such a way that

#       1.The device can operate with a single trigger and can also operate with multiple triggers
#          which enbles the device to execute simulatneous blocks.

#       2.The execution of the code IS performed based on the priority conditions of the corersponding blocks.
#        PRIORITY LEVELS OF THE DESIGN during the simultaneous execution of two blocks:
#           Navigation and the vehicle avoidance Block >            (Highest priority block)
#           Obstacle/common object detection and avoidance block >  (Second highest prority block)
#           Face detection and Recognization block >                (Moderate prority block)
#           Text detection and recognization block                  (Least priority block)

Triggers=[Navigate_vehicle_avoid_GPIO,
          Face_detect_recognize_GPIO,
          Text_detect_recognize_GPIO,
          Object_detect_avoid_GPIO]



#Exporting all external triggers

for trig in Triggers:
    gp.Export(trig)


#Declaration of trigger pins as Input pins

for trig in Triggers:
    gp.Direc(trig,'in')



while True:
    #Reading values of the triggers

    Trig_values=[]

    for trig in Triggers:
        val=gp.Read(trig)
        Trig_values.append(val)


    while(Trig_values==[0,0,0,0]):

        #since all triggers are deactivated no operation is perfomed
        print("All blocks are de activated")

        #voice output pins = 01111 -->  All blocks of your device are deactiavted
        vo.output([0,1,1,1,1])

        #If no block is activted then the device reminds the user for every 1 minute that no block is activated.
        time.sleep(60)
        

    #Here Navigation block is the superior block so the priority of the device will be activated from the Navigation block
    #Here along with path mapping and direction guiding from the user's current location to the destination,
    # the detection of vehicles and the distance prediction procedure will be activated.
    #If a vehicle is inside the permittable range, then according to the segmentation of the image, the central coordinates
    #of the detected vehicle is found and the corresponding voice output will be generated to avoid the vehicle in the path.
        
    #When the trigger for Navigatio block is activated
    while(Trig_values[3]==1):

        #Voice output pin = 10000 -->  Navigation block is activated
        vo.output([1,0,0,0,0])

        #Initializing camera
        vid=cv2.VideoCapture(0)

        #Calling the navigation block
        navigation.navigate(vid)

        #When the destinatio destination coordinates are matched with minimum distance coordintes, then the block will terminate

        #Generating a voice output that the destination has arrived.

        #   voice output pin - 10001 -->  "Your destination has arrived"
        vo.output([1,0,0,0,1])



        #If the trigger for face detection and recognition and known face storage is activated
        if(Trig_values[2]==1):
            
            #When the face detectiona and recognition block is activated, then the immediately the
            #  face detections count will be recorded ideally and also with a distance range.
            #If the face detection count with distance range is excceded by a limit(10) then the face recognition block will be activated.
            #If the detected face is recognized as one  of the face in the stored faces then a voice output will be generated with the
            # name of the detected face.
            #If the face is not recognized in the stored faces then the device asks for the user to save the name of the person or not.
            #If the user suggest yes, then the device asks for the name of the face to save.
            #Finally the captured frame will be saved with the name of the face in the saved faces for next time recognition.

            #NOTE : that this block will be alive upto 50 face detections or 5 face recognitions.
            #       After that the complete block need to be restarted.
            
            #Initializing the face detection and recognition and the storage of the known faces block.
            frds.final(vid)
            #After 50 face detections or 5 face recogntions, the block will terminate.

            #camera will be turned off
            vid.release()
        if(Trig_values[1]==1):

            #When the Object detection and obstacle avoidance block is activated, then the common objects are segregated into obstacle and 
            #   non obstacle objects and are trained to the model.
            #The object recognition process works on the basis of cvlib which usually trains the YOLOV3 dataset as the reference models
            #YOLOV3 consists of 80 predefined real time object models and are trained using Tensorflow.

            #If an object is detected, then a voice ouput will be generated with name of the objec talong wtth the direction of detection.

            #Here some of the models are defined to be as obstacles and remaining are considered as non obstacles.
            #The bounding box coordinates of the obstacles are to be recorded and the central coordinates are to be calculated.
            #Based on the central coordinates, the device takes a decesion to direct the user in an appropriate direction inorder to 
            #  avoid the obstacle.

            #NOTE: This object detection and obstacle avoidance block is meant only for 1 minute. After that it will be terminated and restarted.

            #Intitial time when the object detection block is detected
            init_time = time.time()
            while vid.isOpened():
                ret,img=vid.read()

                #Calling the object detection and obstacle avoidance function.
                oda.obj_det_avd(img)

                #Final time for duration comparision
                final_time=time.time()

                #If the duration is greater than one minute, the camera will be turned off.
                if((final_time-init_time)>60):
                    vid.release()
        
        if(Trig_values[0] == 1):

            vid=cv2.VideoCapture(0)

            #If the text recogntion block is activated then, the text will be detected in a blocks of sentences using tesseract OCR
            #This block text recognition is completely based on the pytesseract module in
            # the dimensions of the text are designed such that to identify the complete sentence

            #At first the frame captured in the camera will be perfomed threshold operation and
            #   and applied by dilation and then the dilated image will be bounded by a rectangle in whhich the while sentense is captured

            #And finally the detected text will be fed to the voice output multiplexing unit.

            #If a frame is found to be detected the same text, then the device triggers for a voice output read the same text or not.

            #Based on the user's choice the repeated text will be read or neglected.


            #Initializing the text recognition block.
            tr.read(vid)


    while(Trig_values[3]==0):

        #Voice output pin = 10000 -->  Navigation block is activated
        vo.output([1,0,0,0,0])

        #Initializing camera
        vid=cv2.VideoCapture(0)

        #Calling the navigation block
        navigation.navigate(vid)

        #When the destinatio destination coordinates are matched with minimum distance coordintes, then the block will terminate
        #Generating a voice output that the destination has arrived.

        #   voice output pin - 10001 -->  "Your destination has arrived"
        vo.output([1,0,0,0,1])



        #If the trigger for face detection and recognition and known face storage is activated
        if(Trig_values[2]==1):

            #NOTE : that this block will be alive upto 50 face detections or 5 face recognitions.
            #       After that the complete block need to be restarted.
            
            #Initializing the face detection and recognition and the storage of the known faces block.
            frds.final(vid)
            #After 50 face detections or 5 face recogntions, the block will terminate.

            vid.release()
        if(Trig_values[1]==1):

            #Intitial time when the object detection block is detected
            init_time = time.time()
            while vid.isOpened():
                ret,img=vid.read()

                #Calling the object detection and obstacle avoidance function.
                oda.obj_det_avd(img)

                #Final time for duration comparision
                final_time=time.time()

                #If the duration is greater than one minute, the camera will be turned off.
                if((final_time-init_time)>60):
                    vid.release()

