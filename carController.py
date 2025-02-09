# Car Controller - Run from the Pico
# Advertises, and then yells to tell 
import time
from BLE_CEEO import Yell
from machine import Pin

def peripheral(name):
    # Defining GPIO pin assignments
    button = Pin('GPIO0', Pin.IN, Pin.PULL_UP)
    
    try:
        # Creating the yelling component
        coms = Yell('pico', verbose = True)
        if coms.connect_up():
            print("Coms is connected via Bluetooth")

        while True:
            if(not button.value()): # Upon button press:
                print("Button has been pressed!")
                #message = readSensors() # TODO: Write sensor reading program
                message = 'FLBR' # tester message while waiting for sensor code
                if coms.connect_up():
                        time.sleep(0.01)
                        coms.send(message)
            
    except Exception as e:
        print("except 1")
        print(e)
        
    
    finally:
        coms.disconnect()
        print('closing up')

# Code-testing area
peripheral('pico')
