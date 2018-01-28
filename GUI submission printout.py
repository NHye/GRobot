###This file consists of robot navigation and control strategies program which forms a part of
###MSc AI with Robotics degree's Artificial Life with Robotics module.
##Author: Nehal Hye


import tkinter as tk
from grobot import*



jarvis=NewRobot("jarvis")

rcApp=tk.Tk()

rcApp.title(" Grid Robot-Control ")  # Title of the box

#Create buttons and place it in a GUI window

rstButton = tk.Button( rcApp, text="Restart" , command = jarvis.init)

rstButton.pack( side=tk.TOP)

rgtButton =  tk.Button( rcApp, text="Right" , command = jarvis.right)

rgtButton.pack( side=tk.RIGHT)

lftButton = tk.Button( rcApp , text="Left" , command= jarvis.left)

lftButton.pack( side=tk.LEFT)

fwButton = tk.Button(rcApp , text="Forward" , command= jarvis.forward)

fwButton.pack()

jlButton = tk.Button ( rcApp , text="jarvis look" , command= jarvis.look)

jlButton.pack()


rcApp.mainloop()
