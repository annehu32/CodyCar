# Car Controller - Run from the Pico
# Advertises, and then yells to tell 
import time
from BLE_CEEO import Yell
from machine import Pin

def peripheral(name):
    try:
        # Creating the yelling component
        coms = Yell('pico', verbose = True)
        while True:
            if coms.connect_up():
                print("Coms is connected via Bluetooth")
                time.sleep(1)
                coms.send("testing from Pico")
            
    except Exception as e:
        print("except 1")
        print(e)
        
    
    finally:
        coms.disconnect()
        print('closing up')

# Code-testing area
peripheral('pico')
