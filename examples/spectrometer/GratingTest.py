#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 09:56:25 2020

@author: wjh
"""

from poptics.spectrometer import Grating
from poptics.ray import RayPencil,RayPath,Disc
from poptics.surface import ImagePlane
import matplotlib.pyplot as plt
from poptics.vector import Unit3d
import math

def main():

        grating = Grating(pitch = 3.3, height = 100, angle = math.radians(0))

        #print(repr(grating[0]))
        #print(repr(grating[1]))

        #disc = Disc(-50,10)
        #pencil = RayPencil().addBeam(disc,0.0).addMonitor(RayPath())
        ip = ImagePlane(50,xsize=30)
        orders = [0,1,2,3]
        for order in orders:

            pencil = RayPencil().addRays(-60,math.radians(0),[0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7])
            pencil.addMonitor(RayPath())

            pencil *= grating


            for ray in pencil:
                yi = ray.director.y
                ym = yi + order*ray.wavelength/grating.pitch
                zm = math.sqrt(1.0 - ym*ym)
                ray.director = Unit3d(0.0,ym,zm)



            pencil *= ip

            pencil.draw()


        grating.draw()
        ip.draw()
        plt.axis("equal")
        plt.grid()
        plt.show()


main()