import serial
import gpioaccess as gp
serial_port=serial.Serial(port='/dev/ttyUSB0',baudrate=115200,bytesize=8,timeout=2)

def location_name():

    voice_input_trig=1844
    gp.Export(voice_input_trig)
    gp.Direc(voice_input_trig,'out')
    gp.Value(voice_input_trig,1)

    if(serial_port.in_waiting > 0):
        ser_loc=serial_port.readLine()
        location=ser_loc.decode('Ascii')
        gp.Value(voice_input_trig,0)
        gp.Clear(voice_input_trig)
        return(location)

def person_name():

    voice_input_trig=1844
    gp.Export(voice_input_trig)
    gp.Direc(voice_input_trig,'out')
    gp.Value(voice_input_trig,1)
    if(serial_port.in_waiting > 0):
        ser_loc=serial_port.readLine()
        location=ser_loc.decode('Ascii')
        gp.Value(voice_input_trig,0)
        gp.Clear(voice_input_trig)
        return(location)  
        
    
