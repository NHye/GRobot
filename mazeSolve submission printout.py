###This file consists of robot navigation and control strategies program which forms a part of
###MSc AI with Robotics degree's Artificial Life with Robotics module.
##Author: Nehal Hye

# mazeSolve.py (Assignment Worksheet 2)
# Right Hand Rule, maze solving Program for simulated gRobot.
# Initialise a new GRobot
from grobot import *
jarvis=NewRobot("robot", colour="yellow")

# Initialise a new GRobot
from grobot import *
jarvis=NewRobot("jarvis", colour="red")

look=[] # Create an empty list to receive robot.look() data
print ("Press Ctrl C to Stop")
while True:
        try:
                look = jarvis.look()

                if look[4] == None:        #if clear on right, move to right square
                        jarvis.right()     
                        jarvis.forward()
                elif look[2] == None:      #otherwise, if forward clear, move forward
                        jarvis.forward()
                else:
                        jarvis.left()      #otherwise turn left
        except KeyboardInterrupt:
                break
exit()

