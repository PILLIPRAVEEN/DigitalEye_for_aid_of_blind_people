import requests
import cv2
import time
import os
import base64

#Object detectiona and recognition url
obj_url = "http://Dgital_Eye.azurewebsites.net/object_recognition"

def recog_obj(img):

    #Saving the captured image
    cv2.imwrite('captures-images/temp2.jpg', rgb_img)
    
    #Sending the captured image to the docker server of the cloud.
    
    my_img1 = {'image': open('captures-images/temp2.jpg', 'rb')}
    response1 = requests.post(obj_url, files=my_img1)

    #Returning the response in the json format.
    return(response1.json())

    
    
    
