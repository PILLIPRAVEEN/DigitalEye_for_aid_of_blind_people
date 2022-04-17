#           FACE DETECTIOON AND DISTANCE PREDICTION

#Here In the Face detection block we have used haarcascadei.e the cascade classifier files in the format of .xml
#Where the training of various number of images are done based on the Viola Jones algoirthm
#This algorithm works with the best speed and accuracy where the 90% of the detections are successful.
#The distance can be predicted using the dimensional ratio equalities of the widths and distances
# of a pre-captured image and a live image

import cv2
fonts = cv2.FONT_HERSHEY_COMPLEX

#Function to detect face and measure the distance of the face from the camera.
def face(img):
    k=0
    dis=0

    f1=0
    cc=cv2.CascadeClassifier('face.xml')
    

    #Known distance of reference face image
    kd_face = 50
    #Known width of reference face image
    kw_face= 15

    face_img=cv2.imread("ref_face.jpeg")
    face_grimg=cv2.cvtColor(face_img,cv2.COLOR_BGR2GRAY)
    ref_rect=cc.detectMultiScale(face_grimg,1.1,9)
    
    for(x,y,w,h) in ref_rect:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        fw=w
        #reference focal value
    fl=(fw*kd_face)/kw_face


    grimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    recta=cc.detectMultiScale(grimg,1.1,9)
    #IF the face is detected then a rectangle will be created based on the dected dimesnions.
    for(x,y,w,h) in recta:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        fw=w
        if(x>=0):
            k=k+1

    #If the detection is successful then the distance prediction will be triggered
    if(k>0):

        #Predicted distance
        dis=(kw_face*fl)/fw
        s='Distance :'+str(dis)

        #printing the distance on the frame
        cv2.putText(img,s,(50,50),fonts,2,(255,0,0))
        return([dis,x,y,w,h])
