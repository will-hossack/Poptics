#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example program to simulate a simple prism spectrometer. The system is set to min
deviation at Mercury e line, then output angle are calcualted between Mercury i line
and Helium r line by ray tracing


"""

import poptics.ray as r
from poptics.lens import Prism
from poptics.wavelength import MaterialIndex, Mercury_e, Mercury_i, Helium_r
import matplotlib.pyplot as plt
from poptics.vector import Angle
import math
from poptics.tio import tprint
import numpy as np

def main():
    
    #      Get the materail type and make a prism of default angle, size and location
    n = MaterialIndex()
    prism = Prism(index = n)
    tprint(repr(prism))
    
    
    #      Get input point on prism and min deviation at Mercury_i line
    pt = prism.getInputPoint()
    dev = prism.minDeviation(Mercury_e)
    tprint("Min deviation : ", math.degrees(dev), " at : ",Mercury_e)
    tprint("Max resolutions is ",prism.maxResolution(Mercury_e))
    tprint("Resolution with 20 mm diameter beam : ", prism.resolution(10,Mercury_e))
    
    u = Angle(dev/2)      # Set ray input angle at half min deviation
    
    #      Form np array of wavelength and angle
    wavelengths = np.linspace(Mercury_i,Helium_r,50)
    angle = np.zeros(wavelengths.size)
    
    #      Go through each wavelength, make a ray and trace it
    for i,wave in enumerate(wavelengths):
        ray = r.IntensityRay(pt,u,wave)
        ray *= prism
        #      Extract angle of ray in degrees
        angle[i] = math.degrees(Angle(ray.director).theta)
         
    # Do the plotting
    
    plt.plot(wavelengths,angle)
    plt.title("Spectrometer Output angle")
    plt.xlabel("Wavelength in microns")
    plt.ylabel("Output angle in degrees")
    plt.grid()
    

    plt.show()
    
    
main()