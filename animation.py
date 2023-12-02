# -*- coding: utf-8 -*-
"""
Simulation of the cart-pendulum system in Python by using Pygame

This file will load the simulation data in the file "simulationData.npy"
and it will generate the animation

Author: Aleksandar Haber 
Date: November 2023
"""
# import the necessary libraries
# pip install pygame
import pygame
import numpy as np
 
# Initialise pygame
pygame.init()
 
# Set window size
size = width,height = 1600, 800
screen = pygame.display.set_mode(size)
# Clock
clock = pygame.time.Clock()


# this is a frame counter
i=0
# load the simulation data that is computed by simulating the cart-pendulum 
# state-space model
solutionArray = np.load('simulationData.npy')

# x coordinate of the cart
x=solutionArray[:,0]
# angle of the pendulum
theta=solutionArray[:,2]

# here, we need to scale and translate x in order to get x in pixels
maxX=max(x)
minX=min(x)
offsetScreenLimits=500
lB=offsetScreenLimits
uB=width-offsetScreenLimits
scaleX=(uB-lB)/(maxX-minX)
offsetX=lB-scaleX*minX
x=scaleX*x+offsetX


# geometrical parameters
# ball radius 
ballRadius=40
# cart width and height
cartWidth=150
cartHeight=100
# rod length
rodLength=300
# wheel radius
wheelRadius=25
# pendulum support bearing
pendulumSupportRadius=15
# position of the base point of the cart in the y-direction
yPositionCart=400

# colors
colorRail=(255, 165, 0)
colorCart=(255,255,153)
colorBall=(255, 0, 0)
colorWheels=(0, 200, 0)
colorPendulumSupport=(255, 165, 0)
colorRod=(255,0,255)

# simulation while loop
while (i<len(x)):
     # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
         
    # Background Color
    screen.fill((0, 0, 0))
    
    # point C -base point of the cart
    xC=x[i]
    yC=yPositionCart
    
    # draw the rail
    pygame.draw.line(screen,colorRail,
                     (int(min(x)-300),int(yC+cartHeight+2*wheelRadius)),
                     (int(max(x)+300), int(yC+cartHeight+2*wheelRadius)),6)
    
    #draw the cart
    pygame.draw.rect(screen,colorCart,
                     (int(xC-cartWidth/2), yC, cartWidth, cartHeight))
    
    #draw the pendulum circle support - rotation support
    
    pygame.draw.circle(screen,colorPendulumSupport,(int(xC)
                                           ,int(yC)),
                                           pendulumSupportRadius)
    
    #draw the cart wheels
    # left wheel
    pygame.draw.circle(screen,colorWheels,(int(xC-cartWidth/2+wheelRadius)
                                           ,int(yC+cartHeight+wheelRadius)),
                                           wheelRadius)
    # right wheel
    pygame.draw.circle(screen,colorWheels,(int(xC+cartWidth/2-wheelRadius)
                                           ,int(yC+cartHeight+wheelRadius)),
                                           wheelRadius)
    
    #draw the rod
    # end point 
    xB=xC-rodLength*np.sin(theta[i])
    yB=yC-rodLength*np.cos(theta[i])    
    pygame.draw.line(screen,colorRod,(int(xC),yC ),(int(xB), int(yB)),8)
    
    # draw the ball
    pygame.draw.circle(screen,colorBall,(int(xB), int(yB)),ballRadius)
        
    pygame.display.flip()
    # introduce a delay
    pygame.time.delay(1)
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    clock.tick(100)
    i=i+1

# this is important, run this if the pygame window does not want to close
pygame.quit()