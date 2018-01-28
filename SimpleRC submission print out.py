###This file consists of robot navigation and control strategies program which forms a part of
###MSc AI with Robotics degree's Artificial Life with Robotics module.
##Author: Nehal Hye


# simpleRC.py #Assignment submission (Worksheet 1)
# Assignment - incorporating "init" feature and grid square positions Simple Remote Control Program for simulated gRobot.
from grobot import *

jarvis=NewRobot("jarvis", 1, 1, colour="black") #initialise a new GRobot Jarvis
msg=""  #Giving commands F,L,R,I(or f,l,r,i) for forward,left,right directions and i to initialise Jarvis once it crashes
x = 1
y = 1
direction = 1  #North
newdirection = 1   #North
while msg!="q" and msg!="Q":
        msg = input("Type: F=Forward, R=Turn Right, L = Turn Left, I = Initialise. Then press RETURN: ")
        if msg == "f" or msg == "F":
                
                if newdirection == 1:    #Pointing North
                        y = y+1
                if newdirection == 2:    #Pointing West
                        x = x-1
                if newdirection == 3:    #Pointing South
                        y = y-1
                if newdirection == 4:    #Pointing East
                        x = x+1
                print ("xpos ypos = ", x,y)
                jarvis.forward()
                
        
        if msg == "l" or msg == "L":


                if direction == 1:        #if left turn reference is North
                        direction = 3     #Set next pointing direction when "L" is pressed to South
                        newdirection = 2  #Set next reference turn direction to West
                        
                if direction == 3:        #if left turn reference is South
                        direction = 4     #Set next pointing direction when "L" is pressed to East
                        newdirection = 3  #Set next reference turn direction to South
                                      
                if direction == 4:        #if left turn reference is East
                        direction = 0     #Set next pointing direction when "L" is pressed to Initial position
                        newdirection = 4  #Set next reference turn direction to East
                        
                if direction == 0:        #if left turn direction is set to initial position
                        direction = 1     #set initial position
                        newdirection = 1  #set initial position
                print ("xpos ypos = ", x,y)    #print x and y co-ordinates
                jarvis.left()     #Turns left

        if msg == "r" or msg == "R":
                
                if direction == 1:        #if right turn reference is North
                        direction = 3     #Set next pointing direction when "R" is pressed to South
                        newdirection = 4  #Set next reference turn direction to East
                        
                if direction == 3:        #if right turn reference is South
                        direction = 2     #Set next pointing direction when "R" is pressed to West
                        newdirection = 3  #Set next reference turn direction to South
                                      
                if direction == 2:        #if right turn reference is West
                        direction = 0     #Set next pointing direction when "R" is pressed to Initial position
                        newdirection = 2  #Set next reference turn direction to West
                        
                if direction == 0:        #if right turn direction is set to initial position
                        direction = 1     #set initial position
                        newdirection = 1  #set initial position
                print ("xpos ypos = ", x,y)    #print x and y co-ordinates
                jarvis.right()    #Turns right

        if msg == "i" or msg == "I":
                jarvis.init(1,1)     #Initializes after a crash
                x = 1
                y = 1
                print ("xpos  ypos = ", x,y)
exit()
