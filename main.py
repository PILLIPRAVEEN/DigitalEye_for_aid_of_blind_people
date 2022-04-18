import gpioaccess as gp

#EXTERNAL TRIGGERS :

#These external triggers are the user choice switches, in which each switch trigger a unique feature to activate

Navigate_vehicle_avoid_GPIO =  1803     #Switch to activate the navigation block and the vehicle avoidance block in the path.

Face_detect_recognize_GPIO  =  1804     #Switch to activate the face detection and recognition and to store the known faces of the user.

Text_detect_recognize_GPIO  =  1805     #Switch to activate the text detection and recognization block of the device

Object_detect_avoid_GPIO    =  1806     #Switch to activate the common object detection excluding navigation block

#Here our device is designed in such a way that

#       1.The device can operate with a single trigger and can also operate with multiple triggers
#          which enbles the device to execute simulatneous blocks.

#       2.The execution of the code IS performed based on the priority conditions of the corersponding blocks.
#        PRIORITY LEVELS OF THE DESIGN during the simultaneous execution of two blocks:
#           Navigation and the vehicle avoidance Block >            (Highest priority block)
#           Obstacle/common object detection and avoidance block >  (Second highest prority block)
#           Face detection and Recognization block >                (Moderate prority block)
#           Text detection and recognization block                  (Least priority block)

Triggers=[Navigate_vehicle_avoid_GPIO,
          Face_detect_recognize_GPIO,
          Text_detect_recognize_GPIO,
          Object_detect_GPIO]



#Exporting all external triggers

for trig in Triggers:
    gp.Export(trig)


#Declaration of trigger pins as Input pins

for trig in Triggers:
    gp.Direc(trig,'in')



while True:
    #Reading values of the triggers

    Trig_values=[]

    for trig in Triggers:
        val=gp.Read(trig)
        Trig_values.append(val)


    while(Trig_values==[0,0,0,0]):
        print("No operation")
    while(Trig_values==[1,0,0,0]):
        print("Only the Navigation block is on")
    while(Trig_values==[0,1,0,0]):
        print("Only face detection and recognition block is on")
    while(Trig_values==[0,0,1,0]):
        print("Only the text detection block is on")
    while(Trig_values==[0,0,0,1]):
        print("Only the object detection block is on")
