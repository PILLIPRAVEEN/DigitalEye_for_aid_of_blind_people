import serial    #importing serial to recieve user's current coordinates from USB GPS reciver

import time



def coordinates():

    #Initializing the serial communication from the USB GPS reciever
    
    gps =  serial.Serial("/dev/ttyUSB1",baudrate=115200)
    

    #Reading the GPS data
    
    ser_data=gps.readline()
    

    #Decoding GPS data and format conversion into degrees
    
    gps_data=ser.data.decode("utf-8").split(".")
    

    #$GPRMC --> NMEA sentence to get Time,date,position,course and speed data.
    
    if(gps_data[0]=='$GPRMC'):
        #Converting NMEA data to decimal coordinates
        
        #Finding latitude
        
        lat_deg=gps_data[3]
        latdeg = lat_deg[:2]
        
        #Computing the integral part of the latitude in degrees
        if(gps_data[6]  ==  'S'):
                latitude_degree=float(latdeg) * (-1)
        else:
                latitude_degree=float(latdeg)
        
        #computing the decimal part of latitude 
        latitude_degree=str(latitude_degree).strip('.0')
        lat_dec = coord_deg[2:10]
        lat_ang_dec = float(lat_dec)/60
        
        #computing decimal value upto 8 decimals
        lat_ang_dec = str(lat_ang_dec).strip('0.')[:8]
        latitude = latitude_degree + "." + lat_ang_dec
        
        


        #Finding longitude
        
        lon_deg = gps_data[5]
        londeg = lon_deg[1:3]
        
        #Computing the integral part of the longitude in degrees
        if(gps_data[4]  ==  'W'):
            longitude_degree=float(londeg) * (-1)
        else:
            longitude_degree=float(londeg)
        
        #computing the decimal part of latitude 
        longitude_degree=str(longitude_degree).strip('.0')
        lon_dec = lon_deg[3:18]
        lon_ang_dec = float(lon_dec)/60
        
        #computing decimal value upto 8 decimals
        lon_ang_dec = str(lon_ang_dec).strip('0.')[:8]
        longitude = longitude_degree + "." + lon_ang_dec
        
        #converting the string values of the coordinates to float
        lat=float(latitude)
        lon=float(longitude)
        
        curr_coord=[]
        curr_coord.append(lat)
        curr_coord.append(lon)
        
        return(curr_coord)



