# 10_cball1.py
# to define a Class for projectile
# use 'projectile' module 

from projectile import Projectile 


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