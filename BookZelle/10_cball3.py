# 10_cball1.py
# to define a Class for projectile

from math import sin, cos, radians 

class Projectile:

    def __init__(self, angle, velocity, height):
        self.xpos = 0.0 
        self.ypos = height 
        theta = radians(angle) 
        self.xvel = velocity * cos(theta) 
        self.yvel = velocity * sin(theta) 
    
    def getX(self):
        return self.xpos 

    def getY(self):
        return self.ypos 

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel 
        yvel1 = self.yvel - time * 9.8 
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0 
        self.yvel = yvel1

def getInputs():
    a = float(input("enter the launch angle (in degrees): "))
    v = float(input("enter the initial velocity (in meterssec): "))
    h = float(input("enter the initial height (in meters): "))
    t = float(input("enter the time interval between position calculations: "))
    return a,v,h,t 

def main():
    angle, vel, h0, time = getInputs() 
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters".format(cball.getX()))

main()