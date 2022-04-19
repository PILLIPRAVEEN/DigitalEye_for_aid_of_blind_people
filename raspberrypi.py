# NOTE:   No processing will be done in this Raspberry pi board. It is only used for voice input and output multiplexing flow
#         This code need to be run in startup of the Rapsberry pi


#               MULTIPLEXING UNIT OF VOICE INPUT AND OUTPUT BLOCKS

#Due to the absence of audio drivers in the pre installer OS, the microphone and the speaker connections are left idle.
#To recieve the voice input from the user and to generate a voice ouput, we are using this Raspberry pi board. 
 
#                           CONNECTIONS
#   Raspberry pi            DE10 Nano               PIN_TYPE
#   GPIO5                   GPIO1839                Voice_output[4]
#   GPIO6                   GPIO1840                Voice_output[3]
#   GPIO17                  GPIO1841                Voice_output[2]            
#   GPIO22                  GPIO1842                Voice_output[1]
#   GPIO27                  GPIO1843                Voice_output[0]

#   GPIO23                  GPIO1844                Voice_input_Trigger
#   GPIO24                  GPIO1845                Trigger to send data from dd10 nano to Raspberry pi


import RPi.GPIO as gp
import serial

import time
import pyttsx3      #For generating voice output

en=pyttsx3.init()   #Activating the engine

import speech_recognition as sr     #For recieving the voice input

#setting GPIO BCM mode
gp.setmode(gp.BCM)

#voice output GPIO pins
vo=[5,6,17,22,27]

#Triggering GPIO pins
tr=[23,24]

#Declaring the voice output pins as input pins
for i in vo:
    gp.setup(i,gp.IN)

#Dfeclaring the triggering pins as input pins
for i in tr:
    gp.setup(i,gp.IN)
    
while True:
    tr_val=[]
    vo_val=[]

    #reading the gpio values of the raspberry pi board from DE10 nano

    for i in vo:
        vo_val.append(gp.input(i))

    for i in tr:
        tr_val.append(gp.input(i))


    #while Voice input trigger is activated
    while(tr_val[0]==1):
        r=sr.Recognizer() #Initializing the voice recognizer
        with sr.Microphone() as src:
            r.adjust_for_ambient_noise(src,0.2)

            #listening
            aud=r.listen(src)

            #converted text
            txt=r.recognize_google(aud)
            txt=txt.lower()
            #Initializing the serial port
            ser=serial.Serial('/dev/ttyUSB0')
            
            #Assigning the baud rate
            ser.baudrate = 115200
            
            #Sending the captured text
            ser.write(txt.encode())

            time.sleep(10)
            #wait for some delay and terminate the serial
            ser.close()


    #while serial data sending trigger is activated        
    while(tr_val[1]==1):
        #initializing the serial port
        serial_port=serial.Serial(port='/dev/ttyUSB0',baudrate=115200,bytesize=8,timeout=2)

        #Reading data from the board
        if(serialport.in_waiting > 0):
            ser_loc=serial_port.readLine()
            text=ser_loc.decode('Ascii')

            #voice output generation of the recieved text
            en.say(text)
            en.runAndWait()


            
    #           MULTIPLEXING VOICE OUTPUT BLOCK
    while(vo_val==[0,0,0,0,1]):
        en.say("Enter the name of the location")
        en.runAndWait()
    while(vo_val==[0,0,0,1,0]):
        en.say("your destination name is Invalid")
        en.runAndWait()
    while(vo_val==[0,0,0,1,1]):
        en.say("Move forward")
        en.runAndWait()
    while(vo_val==[0,0,1,0,0]):
        en.say("Move front left corner")
        en.runAndWait()
    while(vo_val==[0,0,1,0,1]):
        en.say("Move left")
        en.runAndWait()
    while(vo_val==[0,0,1,1,0]):
        en.say("Turn back and move right")
        en.runAndWait()
    while(vo_val==[0,0,1,1,1]):
        en.say("Turn back and move forward")
        en.runAndWait()
    while(vo_val==[0,1,0,0,0]):
        en.say("Turn back and move right")
        en.runAndWait()
    while(vo_val==[0,1,0,0,1]):
        en.say("Move right")
        en.runAndWait()
    while(vo_val==[0,1,0,1,0]):
        en.say("Move front right corner")
        en.runAndWait()
    while(vo_val==[0,1,0,1,1]):
        en.say("A vehicle is approaching near you")
        en.runAndWait()
    while(vo_val==[0,1,1,0,0]):
        en.say("Move right to go safe")
        en.runAndWait()
    while(vo_val==[0,1,1,0,1]):
        en.say("Move left to go safe")
        en.runAndWait()
    while(vo_val==[0,1,1,1,0]):
        en.say("A person is infront of you  Do you want to save the name of the person")
        en.runAndWait()
    while(vo_val==[0,1,1,1,1]):
        en.say("Enter the name of the person")
        en.runAndWait()
    while(vo_val==[1,0,0,0,0]):
        en.say("All blocks of your device are de activated")
    while(vo_val==[1,0,0,0,1]):
        en.say("Navigation block is activated")
    while(vo_val==[1,0,0,1,0]):
        en.say("Your destination has arrived")
    while(vo_val==[1,0,0,1,1]):
        en.say("Face detection and recognition block is actiavted")
    while(vo_val==[1,0,1,0,0]):
        en.say("Face detection and recogntion block is deactivated")
    while(vo_val==[1,0,1,0,1]):
        en.say("Object detection and obstacle avoidance block is activated")
    while(vo_val==[1,0,1,1,0]):
        en.say("Object detection and obstacle avoidance block is deactivated")
    while(vo_val==[1,0,1,1,1]):
        en.say("Text detection and recognition block is activated")
    while(vo_val==[1,1,0,0,0]):
        en.say("Text detection and recognization block is activated")
    while(vo_val==[1,1,1,0,0]):
        en.say("Text detection and recognization block is deactivated")
    while(vo_val==[1,1,1,0,1]):
        en.say("Currency detection and recognition block is activated")
    while(vo_val==[1,1,1,1,0]):
        en.say("Currency detection and recognition block is deactivated")
    
    
        












