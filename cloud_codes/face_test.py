import requests
import cv2
import time
import os
import base64

#Face recogntion url
face_url = "http://Dgital_Eye.azurewebsites.net/face_recognition"

def recognize(img):
    #Resizing and colour mapping
    small_img= cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    rgb_img = cv2.cvtColor(small_img, cv2.COLOR_BGR2RGB)

    #Saving the captured image
    cv2.imwrite('captures-images/temp1.jpg', rgb_img)

    #Sending the captured image to the docker.
    my_img1 = {'image': open('captures-images/temp1.jpg', 'rb')}
    response1 = requests.post(face_url, files=my_img1)

    return(response1.json())

