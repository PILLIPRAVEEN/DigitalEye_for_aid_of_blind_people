#                           DESCRIPTION OF THE CODE

#This block text recognition is completely based on the pytesseract module in
# the dimensions of the text are designed such that to identify the complete sentence

#At first the frame captured in the camera will be perfomed threshold operation and
#   and applied by dilation and then the dilated image will be bounded by a rectangle in whhich the while sentense is captured

#And finally the detected text will be fed to the voice output multiplexing unit.

#If a frame is found to be detected the same text, then the device triggers for a voice output read the same text or not.

#Based on the user's choice the repeated text will be read or neglected.



import cv2

import pytesseract #For text recognition

import voice_output as vo #To send message if the same frame is detected

import voice_input as vi #For the user choice to read the same frame or not

import voice_send as vs #For sending the detected text to multiplexing voice unit of the device.

def read(vid):

    #Creating temporary variable to detect if the same frame is repeated.
    temp_txt = ''

    
    while vid.isOpened():

        ret,img=vid.read()

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


        #If the device is found to detect the same text with the next frame
        if(total_txt == temp_txt):

            #The device sends an output that the same frame is captured. Would yout like to read it or not.
            vo.output([1,1,1,1,1])

            #Taking the user's choice as input
            choice = vi.voice()

            #If the user's choice is yes then the detected text will be read again
            if(choice == 'yes'):

                #Ending the detected text to voice output multiplexing unit.  
                vs.send(total_txt)
        #Updating the temporary text with the detected text
        temp_txt = total_txt            

        #If the frame is not matched with the previous frame
        else:
            
            #sending the detected text to voice output multiplexing unit
            vs.send(total_txt)

            #Updating the temporary text with the detected text
            temp_txt = total_txt
                

            
                

            


