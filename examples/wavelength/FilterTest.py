#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:25:25 2020

@author: wjh
"""

import matplotlib.pyplot as plt
import poptics.tio as tio
import poptics.wavelength as wave
import numpy as np
import math



def main():

    wdata = np.linspace(0.35,0.7,100)
    #fdata = np.zeros(wdata.size)

    wl = tio.getFloat("Long Cut off",0.4)
    ws = tio.getFloat("Short Cut off",0.5)
    dw = tio.getFloat("dw",0.01)



    short = wave.ShortPassFilter(ws,dw)
    long = wave.LongPassFilter(wl,dw)
    stack = wave.FilterStack(short,long)
    band = wave.BandPassFilter(0.4,0.65,0.05)

    tio.tprint(long.getValue(wl + dw/2),"   ", long.getValue(wl - dw/2))
    tio.tprint(short.getValue(ws + dw/2),"   ", short.getValue(ws - dw/2))


    band.draw()
    #stack.draw()

    #spectrum = wave.PlanckSpectrum()
    #spectrum.filter = stack
    #spectrum.draw()


    #plt.plot(wdata,fdata)
    plt.show()

main()

