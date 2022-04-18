import serial
import gpioaccess as gp
import time
def send(command):

    send_trig=1845

    #Exporting the trigger value
    gp.Export(send_trig)

    #Direction = out
    gp.Direc(send_trig,'out')

    #Activating the trigger
    gp.Value(send_trig,1)

    #Initializing the serial port
    ser=serial.Serial('/dev/ttyUSB0')

    #Assigning the baud rate
    ser.baudrate = 115200

    #Sending the data
    ser.write(command.encode())

    time.sleep(5)
    
    #wait for some delay and terminate the serial
    ser.close()

    #De activating the trigger
    gp.Value(send_trig,0)

    #Un exporting the trigger
    gp.Clear(send_trig)

    
