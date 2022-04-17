import gpioaccess as gp
import time

def output(li):
    gpio=[1839,1840,1841,1842,1843]

    #Exporting Multiplexing voice output gpio pins
    for i in range(5):
        gp.Export(gpio[i])

    #Declaring the Voice output pins as output pins
    for i in range(5):
        gp.Direc(gpio[i],'out')

    #Assigning the corresponding values to the fpio pins
    for i in range(5):
        gp.Value(gpio[i],li[i])

        #There should be some presence of some delay to have a successful transmission of gpio values to Raspberry pi.
        time.sleep(5)

    #Un exporting the voice output pins
    for i in range(5):
        gp.Clear(gpio[i])

