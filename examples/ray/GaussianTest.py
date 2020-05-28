
"""
Created on Wed May 27 14:13:54 2020

@author: wjh
"""
from poptics.matrix import ParaxialThinLens
from poptics.ray import GaussianBeam
from poptics.tio import getFloat,tprint
import math

def main():

    #w = getFloat("Beam Waist",100)
    g = GaussianBeam(0.0,0.23,wavelength = 0.633)
    lens = ParaxialThinLens(750, 50)
    #tprint("Beam ",repr(g))

    r = g.getRadius()

    #tprint("Radius is : ",r)

    print("Initial conditions")
    w = g.getWaist()
    tprint("Waist : ",w)
    z = g.getWaistLocation()
    tprint("Waist location is : ", z)




    g *= lens

    r = g.getRadius()

    print("Beam is : " + str(g.beam))
    print("New Location of beam is : " + str(g.z))

    tprint("New Radius is : ",r)
    tprint("New Waist : ",g.getWaist())
    z = g.getWaistLocation()
    tprint("Waist location is : ", z)




main()