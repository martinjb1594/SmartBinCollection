import dweepy
import time
import psutil
import random
import time
import datetime
import grovepi
import math

#Import configuration file 
import config

# Grove Pi Connections
ultrasonic_ranger = 4       # Grove port D4


#Get current time 
now = datetime.datetime.now()


def getDistance():
    return grovepi.ultrasonicRead(ultrasonic_ranger)
   
def getTime():
    return now.hour,now.minute,now.second

    
#Send information to specific dweet thing
def post(readings):
    thing =config.thing
    dweepy.dweet_for(thing, readings)
 
#Get all information and store in a dictionary
def getReadings():
    dict = {}
    dict["Distance"] = getDistance();
    dict["Description"] = "IoT Ultrasinic Sensor"
    dict["Time"] = getTime()
    return dict

#Dweet new data every 6 seconds 
while True:
    #error handling in case of issues with grove pi
    try: 
        dict = getReadings();
        post(dict)
    
        #Duration to sleep in seconds before gathering data again and Dweeting
        time.sleep(6)
    except IOError:
        print(config.IOError)

    except KeyboardInterrupt:
        exit()

    except:
        print(config.PiError)

