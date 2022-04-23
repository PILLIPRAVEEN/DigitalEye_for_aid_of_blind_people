#                       WORKING PRINCIPLE OF THE ALGORITHM

#When the navigation block is activated, the device asks for the user's destination and recieves the destination name through serial communication
#Coordinates will be fetched from the destination name from geocoders and the shortest path will be mapped from the user's current coordinate to the destination.

#1.  Initially the path between the user's current coordinate and the destination coordinates
#    are stored in a list.

#2.  It initially considers the first coordinate as the minimum distance coordinate
#    form the user's coordinate.

#3.  It compares the distance between user's coordinate and the each oordinate of the path list.

#4.  If any coordinate is found to be nearest distance from the user's location, then
#    that coordinate will be updated as minimum distalce coordinate.

#5.  Now by using math_functions the angle between the minimum distance coordinate and the user's
#    current coordinate will be calculated and stored as direct angle.

#6.  And from the Magneto Meter readings of the RFS card the angle of deviation of the user is
#    calculated.

#7.  Now the difference between the direct angle and the deviation angle is considered as
#    reference angle.

#8.  Finally by using Octa-segmentaion of the polar plane, the refrence angle is comared to fit
#    in a segment

#9.  And the command mapped the corresponding segment will be executed immediatley.
#    (i.e the voice output commands to navigate the user)

#10. For each iteration the the minimum distance coordinate will be updated and the complete
#    procedure will iterates until the below condition.

#11. If the minimum index position position is equal to the destination index postion, then the
#    procedure terminates by generating a voice output of "YOUR DESTINATION HAS ARRIVED"
                #VEHICLE AVOIDANCE BLOCK
#1.Meanwhile the camera is continuosly captures the frames of the road along with path mapping

#2.The complete frame will be divided into slots and if the vehicle is detected in a particular slot,
#  then the cooresponding voice output code will be generated and fed to Raspberry pi.

import time

import user_coordinates         #For collecting the user's location coordinates

import destination_coordinates  #For collecting the user's destination coordinates

import path_coordinates         #For mapping the path and collecting the coordinates from current location to destination

import math_functions           #For mathematical operations of the coordinates

import voice_output as vo       #For generating voice output in the multiplexing unit from Raspberry pi

import vehicle_avoid as va      #For Performing vehicle and pedestrian avoidance block


def navigate():
        user_coord = user_coordinates.coordinates() #Fetches user's current location coordinates
        
        dest_coord - destination_coordinates.destination() #Fectches destination coordinates
        
        path_coord = path_coordinates.getpath(user_coord,dest_coord) #Stores the path coordinates form the user's location to destination location.
        
        
        temp_ind = 0      #Temporary index of the minimum distance coordinate of path list from the user's crrent coordinate
        
        
        #Initializing camera to avoid vehicles inthe path
        
        vid=cv2.VideoCapture(0)
        
        while temp_ind < len(path_coord)-1 and vid.isOpened():
                curr_coord = user_coordinates.coordinates() #user's current coordinates
                x2 = curr_coord[0]
                y2 = curr_coord[1]
        
                #Angle between the temporary minimum distace coordinate and user's current coordinate.
                ang = math_functions.direc(curr_coord[temp_ind][0], curr_coord[temp_ind][1],x2,y2)
                if(temp_ind>=0):
                        mi=temp_ind     #mi --> minimum distance coordinate index
        
                #m --> Minimum distance of the user's location to the path
                m = hs.haversine((x2,y2), (curr_coord[temp_ind][0], curr_coord[temp_ind][1]))
                
                #Comparing the distance of the user's current coordinate with the consecutive 5 coordinates of the path list
                for i in range(tem_ind,temp_ind+5,1):
                        
                        #If the distance of the path coordinate is less than the minimum distance, then this coordinate index will be minimum distance coordinate index
                        if(hs.haversine((x2,y2),(curr_coord[i][0], curr_coord[i][1]))<m):
                                m=hs.haversine((x2,y2),(curr_coord[i][0], curr_coord[i][1]))
                                mi=i
        
        	#If the minimum distance coordinate is not updated then the initial coordinate is taken as the minimum distance coordinate.
                if(m==hs.haversine((x2,y2),(curr_coord[temp_ind][0], curr_coord[temp_ind][1]))):
                        mi=temp_ind
        
            	#Final minimum distance coordinate index is mapped to temporary index.
                temp_ind=mi
        
            	#Angle between the user's cuurent coordinate to the minimum index coordinate -->  Direct Angle.
                ang1=math_functions.direc(cord[temp_ind][0],cord[temp_ind][1],x2,y2)
        
            	#Direct Angle bounded for single rotation.
                Direc_ang=math_functions.angdec(ang1)
        
            	#Angle of deflection obtained form Magnetometer of the RFS card --> Deviation Angle
                #Deviat_ang=math_functions.angdec()
        
            	#Difference between the deviation angle and the direct angle -->  Reference Angle.
                Ref_ang=Direc_ang
        
        
                #                       OCTA - SEGMENTATION OF THE POLAR PLANE
                
        
                #segment-1 :  337.5 degrees  to  22.5 degrees
                
                if(((Ref_ang>=-22.5)and(Ref_ang<22.5))or((Ref_ang<=382.5)and(Ref_ang>337.5))):
        
                        #voice output values = 0,0,0,1,1  -->     "MOVE FORWARD"
                        vo.output([0,0,0,1,1])
        
        
        
                #segment-2 :  22.5 degrees  to  67.5 degrees 
                        
                elif(((Ref_ang>=22.5)and(Ref_ang<67.5))or((Ref_ang<-292.5)and(Ref_ang>-337.5))):
        
                        #voice_output values = 0,0,1,0,0  -->     "MOVE FRONT LEFT CORNER"
                        vo.output([0,0,1,0,0])
        
        
        
                #segment-3 :  67.5 degrees  to  112.5 degrees
        
                elif(((Ref_ang>=67.5)and(Ref_ang<112.5))or((Ref_ang<-247.5)and(Ref_ang>-292.5))): 
        
                        #voice output values = 0,0,1,0,1 -->      "MOVE LEFT"
                        vo.output([0,0,1,0,1])
        
        
        
                #segment-4 :  112.5 degrees  to  157.5 degrees 
        
                elif(((Ref_ang>=112.5)and(Ref_ang<157.5))or((Ref_ang<-202.5)and(Ref_ang>-247.5))):
        
                        #voice output values = 0,0,1,1,0 -->      "TURN BACK AND MOVE RIGHT"
                        vo.output([0,0,1,1,0])
        
        
        
                #segment-5 :  157.5 degrees  to  202.5 degrees 
        
                elif(((Ref_ang>=157.5)and(Ref_ang<202.5))or((Ref_ang<-157.5)and(Ref_ang>-202.5))):
        
                        #voice output values = 0,0,1,1,1 -->      "TURN BACK AND MOVE FORWARD"
                        vo.output([0,0,1,1,1])
        
        
        
                #segment-6 :  202.5 degrees  to  247.5 degrees 
        
                elif(((Ref_ang>=202.5)and(Ref_ang<247.5))or((Ref_ang<-112.5)and(Ref_ang>-157.5))):
        
                        #voice output values = 0,1,0,0,0 -->      "TURN BACK AND MOVE RIGHT"
                        vo.output([0,1,0,0,0])
        
        
        
                #segment-7 :  247.5 degrees  to  292.5 degrees 
        
                elif(((Ref_ang>=247.5)and(Ref_ang<292.5))or((Ref_ang<-67.5)and(Ref_ang>-112.5))):
                        
                        #voice output values = 0,1,0,0,1 -->      "MOVE RIGHT"
                        vo.output([0,1,0,0,1])
                                
                
        
        
                #segment-8 :  292.5 degrees  to  337.5 degrees 
        
                elif(((Ref_ang>=292.5)and(Ref_ang<337.5))or((Ref_ang<-22.5)and(Ref_ang>-67.5))):
        
                        #voice output values = 0,1,0,1,0 -->      "MOVE FRONT RIGHT CORNER"
                        vo.output([0,1,0,1,0])
        
        
                        #VEHICLE AVOIDANCE BLOCK
        
                #Reading the frames of the camera.
                ret,img=vid.read()
        
                #Performing Vehicle detection and avoidance block.
                va.avoid()
                    

