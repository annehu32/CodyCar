# Car - Run from the ESP
# Connects to the carController, listens for commands from Pico

import time
from BLE_CEEO import Listen
from machine import Pin, PWM

right1 = PWM(Pin(0, Pin.OUT), freq=50)
right2 = PWM(Pin(1, Pin.OUT), freq=50)
left1 = PWM(Pin(2, Pin.OUT), freq=50)
left2 = PWM(Pin(21, Pin.OUT), freq=50)

def central(name):
    try:
        L = Listen(name, verbose = True)
        
        while True:
            if L.connect_up():
                print(str(name)+" is connected")
                
                while True:
                    if L.is_any:
                        reply = L.read()
                        print(reply)
                        drive(reply)
                    
    except Exception as e:
        print("exception!")
        print(e)
        
    finally:
        L.disconnect()
        print('closing up')

def runCommand(x):
    global right1, right2, left1, left2
    print("----- running command: "+x+" -------")

    if (x == 'F'):
        print("----Going Forward----")
        right1.duty(0)
        left1.duty(0)
        time.sleep(0.01)
        
        right2.duty(1023)
        left2.duty(1023)
        time.sleep(2)
        
        right2.duty(0)
        left2.duty(0)
        time.sleep(0.01)
    
    elif (x == 'B'):
        print("----Going Backward----")
        right2.duty(0)
        left2.duty(0)
        time.sleep(0.01)
        
        right1.duty(1023)
        left1.duty(1023)
        time.sleep(2)
        
        right1.duty(0)
        left1.duty(0)
        time.sleep(0.01)

    
    elif(x == 'R'):
        print("----Turning Right----")

        right1.duty(0)
        left1.duty(0)
        time.sleep(0.01)
        
        right2.duty(500)
        left2.duty(1023)
        time.sleep(2)
        
        right2.duty(0)
        left2.duty(0)
        time.sleep(0.01)


    elif (x == 'L'):
        print("----Turning Left----")

        right1.duty(0)
        left1.duty(0)
        time.sleep(0.01)
        
        right2.duty(1023)
        left2.duty(500)
        time.sleep(2)
        
        right2.duty(0)
        left2.duty(0)
        time.sleep(0.01)

        
    else:
        print("-----invalid command, not FBLR-----")

def drive(command):
    loopOpen = -1
    loopClose = -1
    
    # Assumes correct open/close use of loop brackets
    for i in range(0,5):
        if command[i] == 'P':
            print("-----Loop opening present at "+str(i)+"------")
            loopOpen = i
            for j in range (i+1, 5):
                if command[j] == 'P':
                    print("-----Loop closing present at "+str(j)+"-----")
                    loopClose = j
            break
        print("Loop open index: "+str(loopOpen)+", loop close index: "+str(loopClose))
    
    # If a loop is present
    if (not loopOpen == -1 and not loopClose==-1):
        print("------LOOP EXECUTING STUFF-----")
        # Run any blocks before the loop
        print(str(range(0,loopOpen)))
        for k in range(0,loopOpen):
            runCommand(command[k])
        
        # Loop will run 4 times
        for k in range(0,4):
            print("------ inside for 4 loop -----")
            print("loop range: "+str(range(loopOpen+1, loopClose)))
            for j in range(loopOpen+1, loopClose):
                runCommand(command[j])
        
        # Run any blocks after the loop
        for k in range(loopClose+1,5):
            runCommand(command[k])
            
    
    # If a loop is not present
    else:
        print("------NO LOOP :(-----")
        runCommand(command[0])
        runCommand(command[1])
        runCommand(command[2])
        runCommand(command[3])
        runCommand(command[4])

    print("----- Done running command "+str(command)+"-------")


# Code-testing area
central('pico')

