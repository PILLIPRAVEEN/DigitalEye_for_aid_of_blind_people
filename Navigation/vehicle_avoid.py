import cv2

import vehicle_distance as vd       #To get the distance and the dimensions and coordinates of the bounding rectangle

import voice_output as vo

def avoid(img):

    #Plotting a boundary rectangle on the frame size 450 X 450 for pixel sectional division
    cv2.rectangle(img,(200,50),(650,500),(255,0,0),2)
    
    #Dividing the boundary rectangle into three regions.
    cv2.line(img,(350,50),(350,500),(255,0,0),2)
    cv2.line(img,(500,50),(500,500),(255,0,0),2)

    #Calling all the vehcile functions to identify the vehicles in the frame
    car=vd.car()
    bus=vd.bus()
    bike=vd.bike()
    pedestrian=vd.pedestrian()

    #Creating vehicle list
    vehicle_list=[car,bus,bike,pedestrian]

    for veh in vehicle_list:
        #If the detection of the vehicle is successful
        if(veh != None):
            #If the distance of the vehicle is less than 6 meters 
            if(veh[0]<=600):

                #voice output code = 01011 -->  A vehicle is approaching 
                vo.output([0,1,0,1,1])

                #Center point og the bounding box
                xcp=veh[1]+veh[3]//2
                ycp=veh[2]+veh[4]//2

                if(xcp>200 and xcp<350):

                    #voice output code = 01100  -->  Move right to go safe
                    vo.output([0,1,1,0,0])

                elif(xcp>350 and xcp<500):

                    #If the vehicle is detected at the straight front then it prefers left side to travel
                    #voice output code = 01100  -->  Move left to go safe
                    vo.output([0,1,1,0,1])

                elif(xcp>500 and xcp<650):

                    #voice output code = 01101  -->  Move left to go safe
                    vo.output([0,1,1,0,1])
    

