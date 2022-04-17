import math

#Module to find the distance between two gps coordinates.
import haversine as hs

#importing trigonometric functions from math for coputation
from math import pi
from math import sin
from math import cos
from math import atan2



#           FUNCTION TO FIND THE ANGLE BETWEEN TWO GPS COORDINATES

def direc(x1,y1,x2,y2):
	lat1=x1*pi/180
	lon1=y1*pi/180
	lat2=x2*pi/180
	lon2=y2*pi/180

	x = cos(lat2)*sin(lon2-lon1)
	y = (cos(lat1)*sin(lat2))-(sin(lat1)*cos(lat2))*(cos(lon2-lon1))

	ang=atan2(x,y)

	angdeg=ang*180/pi

	return(angdeg)




#       FUNCTION TO BOUND THE ANGLE WITH IN A SINGLE ROTATION (i.e 0 to 360) 

def angdec(x):
    if(x>=0 and x<=360):
        return(x)
    else:
        return(360-x)


#       FUNCTION TO PERFORM MODULUS OPERATION
def mod(a):
	if(a>=0):
		return(a)
	else:
		return(-1*a)
