# Car - Run from the ESP
# Connects to the carController, listens for commands from Pico

import time
from BLE_CEEO import Listen
from machine import Pin

def central(name):
    try:
        L = Listen(name, verbose = True)
        
        while True:
            if L.connect_up():
                print(str(name)+" is connected")
                
                while True:
                    L.send("testing from ESP")
                    time.sleep(1)
                    
                    if L.is_any:
                        reply = L.read()
                        print(reply)
                    
    except Exception as e:
        print("exception!")
        print(e)
        
    finally:
        L.disconnect()
        print('closing up')

# Code-testing area
central('pico')

