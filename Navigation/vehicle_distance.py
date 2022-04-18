#           VEHICLE DETECTIOON AND DISTANCE PREDICTION

#Here In the vehicle & pedestrian detection block we have used haarcascade files
#Where the training of the vehicle or pedestrian images are done in the viola jones algoirthm
#This algorithm works with the best speed and accuracy where the 90% of the detections are successful.
#The distance can be predicted using the dimensional ratio equalities of the widths and distances
# of a pre-captured image and a live image

import cv2
fonts = cv2.FONT_HERSHEY_COMPLEX

#Function to detect cars and measure the distance of the car from the camera.
def car(img):
    k=0
    dis=0

    f1=0
    cc=cv2.CascadeClassifier('Cascade_Classifiers/car.xml')
    

    #Known distance of reference car image
    kd_car = 1500
    #Known width of reference car image
    kw_car = 330

    car_img=cv2.imread("ref_images/car.jpg")
    car_grimg=cv2.cvtColor(car_img,cv2.COLOR_BGR2GRAY)
    ref_rect=cc.detectMultiScale(car_grimg,1.1,9)
    
    for(x,y,w,h) in ref_rect:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        fw=w
        #reference focal value
    fl=(fw*kd_car)/kw_car


    grimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    recta=cc.detectMultiScale(grimg,1.1,9)
    #IF the car is detected then a rectangle will be created based on the dected dimesnions.
    for(x,y,w,h) in recta:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        fw=w
        if(x>=0):
            k=k+1

    #If the detection is successful then the distance prediction will be triggered
    if(k>0):

        #Predicted distance
        dis=(kw_car*fl)/fw
        return([dis,x,y,w,h])


#Function to detect pedestrians and measure the distance of the pedestrian from the camera.
def pedestrian(img):
    k=0
    dis=0

    f1=0
    cc=cv2.CascadeClassifier('Cascade_Classifiers/pedestrian.xml')
    

    #Known distance of the reference pedestrian image
    kd_pedestrian=730
    #Known width of the reference pedestrian image
    kw_pedestrian=93

    pedestrian_img=cv2.imread("ref_images/pedestrian.jpg")
    pedestrian_grimg=cv2.cvtColor(pedestrian_img,cv2.COLOR_BGR2GRAY)
    ref_rect=cc.detectMultiScale(pedestrian_grimg,1.1,9)
    
    for(x,y,w,h) in ref_rect:
        cv2.rectangle(pedestrian_img,(x,y),(x+w,y+h),(0,255,0),2)
        fw=w
        #reference focal value
        fl=(fw*kd_pedestrian)/kw_pedestrian


    grimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    recta=cc.detectMultiScale(grimg,1.1,9)
    #IF the pedestrian is detected then a rectangle will be created based on the dected dimesnions.
    for(x,y,w,h) in recta:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        fw=w
        if(x>=0):
            k=k+1

    #If the detection is successful then the distance prediction will be triggered
    if(k>0):

        #Predicted distance
        dis=(kw_pedestrian*fl)/fw
        return([dis,x,y,w,h])



#Function to detect bus and measure the distance of the bus from the camera.
def bus(img):
    k=0
    dis=0

    f1=0
    cc=cv2.CascadeClassifier('Cascade_Classifiers/bus.xml')
    

    #Known distance of reference bus image
    kd_bus= 5500
    #Known width of reference bus image
    kw_bus= 2600


    bus_img=cv2.imread("ref_images/bus.jpg")
    bus_grimg=cv2.cvtColor(bus_img,cv2.COLOR_BGR2GRAY)
    ref_rect=cc.detectMultiScale(bus_grimg,1.1,9)
    
    for(x,y,w,h) in ref_rect:
        cv2.rectangle(bus_img,(x,y),(x+w,y+h),(0,255,0),2)
        fw=w
        #reference focal value
        fl=(fw*kd_bus)/kw_bus


    grimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    recta=cc.detectMultiScale(grimg,1.1,9)
    #IF the bus is detected then a rectangle will be created based on the dected dimesnions.
    for(x,y,w,h) in recta:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        fw=w
        if(x>=0):
            k=k+1

    #If the detection is successful then the distance prediction will be triggered
    if(k>0):

        #Predicted distance
        dis=(kw_bus*fl)/fw
        return([dis,x,y,w,h])


#Function to detect bike and measure the distance of the bike from the camera.
def bike(img):
    k=0
    dis=0
    f1=0
    
    cc=cv2.CascadeClassifier('Cascade_Classifiers/bike.xml')
    

    #Known distance of the reference bike image
    kd_bike= 120
    #Known width of the reference bike image
    kw_bike= 58


    bike_img=cv2.imread("ref_images/bike.png")
    bike_grimg=cv2.cvtColor(bike_img,cv2.COLOR_BGR2GRAY)
    ref_rect=cc.detectMultiScale(bike_grimg,1.1,9)
    
    for(x,y,w,h) in ref_rect:
        cv2.rectangle(bike_img,(x,y),(x+w,y+h),(0,255,0),2)
        fw=w
        #reference focal value
        fl=(fw*kd_bike)/kw_bike


    grimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    recta=cc.detectMultiScale(grimg,1.1,9)
    #IF the bus is detected then a rectangle will be created based on the dected dimesnions.
    for(x,y,w,h) in recta:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        fw=w
        if(x>=0):
            k=k+1

    #If the detection is successful then the distance prediction will be triggered
    if(k>0):

        #Predicted distance
        dis=(kw_bike*fl)/fw
        return([dis,x,y,w,h])
