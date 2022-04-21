#                           FUNCTIONALITY OF THE CODE

#This is a basic currency recogntion block which is completely dependent on the face recogntion and text recogntion algorithms.
#If the trigger for this block is activated, then immediately the face detection unit will activate. If any face is detected on the frame,
# Then the image will be sent to the face recogntion block of the cloud section and the result of prediction will be stored.
#And the predicted result will be compared with the faces of the national deligates on the currency and immediately the text recogntion block will activate.
#The result of text detection block is segmented according to the curency value priority and compared with the values of currency.
#And the finalized value will be sent includeing the type of curerncy to the voice outuput unit of the device.

#Finally if the duration of the block is excced than the required duraion, then block will terminate.

import time

import cv2

import voice_send as vs  #For sending the detected currency label to the voice output unit.

import facedetect_distance as fdd #For detecting the faces on the currency

from cloud_codes import face_test #Importing the face recognition code from the cloud docker resource 

import text_recog as tr


def value(img):
    #Gray scale image conversion
    gr=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #Performing OTSU Threshold
    ret,thresh = cv2.threshold(gr,0,255,cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    #Bounding the size of the rectangle for the detection of text in a sentence
    rect = cv2.getStructuringElement(cv2.MORPH_RECT,(18,18))

    #Applying the dilation on the threshold image
    dil=cv2.dilate(thresh,rect,iterations = 1)

    #finding contours and heirachy
    contrs,heir = cv2.findContours(dil,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #Detected contours will be looped and the rectangle bounding box will be cropped.

    total_txt = ''
    for cnt in contrs:
        #Bouding the rectangle dimensions
        x,y,w,h = cv2.boundingRect(cnt)

        #Drawing the rectangle
        rect=cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

        #Croppingthe image
        cr=img[y:y+h,x:x+w]

        #Detection of text sentense by sentense
        txt=pytesseract.image_to_string(cr)

        ##cv2.imshow(img)
        ##cv2.waitKey(0)

        #Forming complete text in the frame
        total_txt= total_txt + " " +txt
        return(total_text)


def detect(vid,duration):

    #Initial time of starting the block
    init_time = time.time()    

    #Faces of diffrent curreency images
    curre_faces=['Rupee','dollar1','dollar2','dollar3','dollar4','dollar5','dollar6']

    #Values of US Dollars
    dollar=['100','50','20','10','5','2','1']

    #Values of Indian rupees
    rupee=['100','50','20','10']

    while vid.isOpened():
        
        ret,img-vid.read()
        result = face_test.recognize(img)

        li=fdd.face(img)

        #If a face on the currency is detected
        if(li[0]>0):

            #Face recogniion block will be activated.
            name=result['prediction']

            #If any any face is recongnized in with the faces of the database
            if(name != 'Unknown'):

                #Checks for the type of currency to be in dollars
                for i in range(1,len(curr_faces)):

                    #If a name of the dollar is matched with the face on the currency
                    if(curr_faces[i]==name):

                        #Detecting the text on the currency
                        val=value(img)

                        #If the value dollar list it sends ta message of detection of dollars with the value
                        if(val in dollar[i]):
                            message = "a "+ val + " dollar note is detected"

                            vs.send(message)

                            #If one value is detected then the loop will break to avoid repetition.
                            break

                #Checking for the face of the currency match with indian rupee
                if(name == curre_faces[0]):

                        #Detecting the text on the currency
                        val=value(img)

                        #Checking if the value is present in indian rupee values
                        if val in rupee:

                            #If the value of the currency is detected then it sends a message to the user with its value
                            message = "a"+ val + "Rupee note is detected"
                            vs.send(message)

                            #If one value is detected then the loop will break to avoid repetition.
                            break

        #Final time to record
        final_time = time.time()

        #If the duration of the block is greater than the required duration, then the block will end
        if((final_time-init_time)>= duration):
            break
