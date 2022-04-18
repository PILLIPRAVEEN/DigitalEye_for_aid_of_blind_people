#                           FUNCTIONALITY OF THE CODE

#This code works on the basis of pre trained models of tensor flow using cvlib and runs in the Docker resource section of cloud.
#cvlib uses the YOLOV3 custom image dataset which has upto 80 pretrained labels and classifications of real time
# objects and creatures.
#If an object in the frame is recognized, then the detected parts of the frame will be indicated by bounding boxes.
#In the labels of the YOLOV3 models, some models are to be classified as obstacles and they need to be avoided.
#Based on the coordinate sections of the bounding boxes, the central coordinates of the obstacle are obtained.
#The central coordinates compared with the segmentations of the reference frame rectangle and based on this,
# the corresponding decesion will be taken to avoid the obstacle in the path.

import cv2

#Initializing the cvlib training models
import cvlib as cl

#Attaching boudning boxex for the detected lables of the cvlib.
from cvlib.object_detection import draw_bbox

#Object detection URL
obj_detect_url = "http://Dgital_Eye.azurewebsites.net/object_recognition"

#Function to detect common objects in the frame.
def obj_detect(img1):

    #Reading the image
    img=cv2.imread(img1)

    #detecting box coordinates , labels and the percentage of confidence to detect the common objects.
    bx,lbl,cnf=cl.detect_common_objects(img)

    #Drawing bounding box with detected labels of the frame
    img1=draw_bbox(img,bx,lbl,cnf)
    
    #Finally the function will returns the label name and the coordinates of the boundig boxes.
    return([lbl,bx])
