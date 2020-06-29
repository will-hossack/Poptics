#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:17:13 2020

@author: wjh
"""

from poptics.spectrometer import PrismSpectrometer

def main():

    spec = PrismSpectrometer().fromFile("BK7")
    print(repr(spec))
    print("Waveleng is " + str(spec.wavelength))

main()