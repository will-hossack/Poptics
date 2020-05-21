"""
Example program to show converting between angle and Unit3d and reading an angle 
in degrees using the poptics.tio function.

"""
from poptics.tio import getAngleDegrees,tprint
from poptics.vector import Angle,Unit3d

def main():
    
    angle = Angle().setDegrees(30,80)   # Angle with theta = 30 , psi = 80 degrees
    tprint("Angle is : ",angle)         # print, note tprint() automaticall take str()
    u = Unit3d(angle)                   # Convert to Unit3d
    tprint(repr(u))                     # print using repr()
    
    angle = u.getAngle()                    # get angle from Unit3d
    theta,psi = angle.getDegrees()          # get the angle as a list in degrees
    tprint("Theta is : ", theta, " and psi is : ", psi)   # print it
    
    angle = getAngleDegrees("Get angle in degtrees")
    tprint(repr(angle))
    u = Unit3d(angle)                   # Convert to Unit3d
    tprint(repr(u))                     # print using repr()

main()