# 10_cball1.py
from math import sin, cos, radians 

def main():
    angle = float(input("enter the launch angle (in degrees): "))
    vel = float(input("enter the initial velocity (in meterssec): "))
    h0 = float(input("enter the initial height (in meters): "))
    time = float(input("enter the time interval between position calculations: "))

    # convert angle to radians 
    theta = radians(angle) 

    # set the initial position and velocities in x and y directions 
    xpos = 0 
    ypos = h0 
    xvel = vel * cos(theta) 
    yvel = vel * sin(theta) 

    # loop until the ball hits the ground 
    while ypos >= 0:
        # calculate position and velocity in time seconds 
        xpos = xpos + time * xvel 
        yvel1 = yvel - time * 9.8 
        ypos = ypos + time * (yvel + yvel1) / 2.0 
        yvel = yvel1 
    print("\nDistance traveled: {0:0.1f} meters".format(xpos))

main()