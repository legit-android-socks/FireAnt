#!/usr/bin/env python

# Import modules. 
from fireant import FireAnt
import random

# User implemented functions

def userFunctions(args):
    #do stuff
    value = args
    return value

def readSensor1():
    return 100

def readSensor2():
    return random.randint(1,501)

# main part
if __name__ == '__main__':
    try:
        #create a FireAnt object. This registers with the platform and sets the robot online.
        myAnt = FireAnt('auth.json')
        print(myAnt.is_robot_online())
        print(myAnt.get_name())
        print(myAnt.get_description())
        while myAnt.is_robot_online():
            
            #wait for a user to request control
            print('Waiting for users ...')
            myAnt.wait_for_available_user()
            print('Got user!')
            #as long as the user is online and in control:
            while myAnt.get_useron():
                #get control data
                controldata = myAnt.get_control_data()
                print(controldata)
                
                #do stuff with control data
                #check if sensor reading is requested
                request1 = myAnt.get_sensor_request('sensor1')
                request2 = myAnt.get_sensor_request('sensor_2')
                
                #send sensor reading
                if request1:
                    reading = readSensor1()
                    myAnt.publish_data( ("sensor1", reading, False) )
                if request2:
                    myAnt.publish_data(("sensor_2", readSensor2(), True))
            
            #log session
            myAnt.log_session()
    except KeyboardInterrupt:
        myAnt.log_session()
        print("Interrupted by master")