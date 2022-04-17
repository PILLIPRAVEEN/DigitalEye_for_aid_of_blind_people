import gpioaccess as gp   #importing gpio access file

import time

import voice_input as vi  #importing the voice input file to get the name of the destination location from the user

from geopy.geocoders import Nominatim







#                   MULTIPLEXING VOICE OUPUT CODE

# Here pins from 1839 to 1842 are considered as multiplexing voice output pins
# According to the condition, the values of the multiplexing pins will be given certain values.
# According the values([1839,1840,1841,1842]), Raspberry pi will generates a corresponding voice output instruction.


#Here  if values([1839,1840,1841,1842,1843]) = 00001  -->   "Enter the name of the destination location"

#      if values([1839,1840,1841,1842,1843]) = 00010  -->   "Invalid destination name"


def destination():
    Voice_output_GPIO=[]
    
    for pin in range(1839,1844):
        Voice_output_GPIO.append(pin)
    
    #Exporting the multiplexer voice output gpio pins
    for pin in Voice_output_GPIO:
        gp.Export(pin)
    
    
    #Declaring the values of the multiplexer gpio as output pins
    for pin in Voice_output_GPIO:
        gp.Direc(pin,'out')
    
    
    
    
    
    
    
    #               RECIEVING THE NAME OF THE DESTINATION FROM USER
    
    
    Voice_input_trig=1844   #Trigger pin to capture name of the destination location from Raspberry pi
    
    #Exporting the trigger pin to capture voice input pin
    gp.Export(Voice_input_trig)
    
    
    #Declaring the Voice_input_trig pin as output pin
    gp.Direc(Voice_input_trig,'out')
    
    #For recieving the name of the destination location from the user the Voice_input_trigger need to be HIGH
    #Whenever the Raspberry pi board recieves the presence of voice_input trigger,
    #                   -> it immediately turns on the microphone and recognizes the name of the location using Speech Recognition module
    #                   -> then the recieved audio will be converted into text using Google recognizer
    #                   -> And the obtained text will be sent to the DE10 Nano board via serial communication.
    
    
    
    #Sending the trigger value as HIGH
    gp.Value(Voice_input_trig,1)
    
    #Waits for the respone from the user
    time.sleep(10)
    
    #After the average trasmission duration the trigger value will again reset to LOW
    gp.Value(Voice_input_trig,0)


    
    while True:
    
        #Multiplexing voice output code = 0001 =>  "Enter the name of the location" 
        gp.Value(Voice_output_GPIO[0],0)
        gp.Value(Voice_output_GPIO[1],0)
        gp.Value(Voice_output_GPIO[2],0)
        gp.Value(Voice_output_GPIO[3],1)
        
        # Name of the location from the user obtained from serial communication
        location=vi.location_name()
        
        #Initialising the Nominatim tool
        loc=Nominatim(user_agent='GetLoc')
        
        #Obtaining the address of the destination location from geocode
        loc_addr=loc.geocode(location)
        
        #If the entered location is invalid it sends a message to the user that the location name is invalid.
        # And asks the destination name again and again sends the trigger value as HIGH
        
        if(loc_addr==None):
            
            #Multiplexing voice output code = 0010 =>  "Invalid destination name"
            gp.Value(Voice_output_GPIO[0],0)
            gp.Value(Voice_output_GPIO[1],0)
            gp.Value(Voice_output_GPIO[2],1)
            gp.Value(Voice_output_GPIO[3],0)
                
            #Again sending the trigger value as HIGH
            gp.Value(Voice_input_trig,1)
            time.sleep(10)
            continue
            
        #Coordinate list of the user's destination location.
        loc_coord=[]
        
        loc_coord.append(loc_addr.latitude)
        loc_coord.append(loc_addr.longitude)
        if(len(loc_coord)==2):
            gp.Value(Voice_input_trig,0)
            break
    return(loc_coord)















