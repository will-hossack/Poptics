#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:27:36 2020

@author: wjh
"""

from poptics.wavefront import WaveFront
from poptics.tio import getBool
import matplotlib.pyplot as plt


def main():
    wave = WaveFront().fromFile()
    print(repr(wave))
    
    log = getBool("Take log",True)
    wave.drawPSF(log = log)
    
    plt.show()
    
        
    
main()