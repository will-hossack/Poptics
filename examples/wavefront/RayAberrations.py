"""
    Example program to plot the Ray Aberrations for a lens
Author: Will Hossack, The Unievsrity of Edinburgh
"""
from poptics.lens import DataBaseLens
from poptics.wavelength import getDefaultWavelength
import matplotlib.pyplot as plt
from poptics.wavefront import WaveFrontAnalysis
import math
from poptics.tio import getFloat

def main():

    # Get lens and other info

    lens = DataBaseLens()
    angle = math.radians(getFloat("Angle in degrees"))
    wave = getFloat("Wavelength of plot",getDefaultWavelength())

    wa = WaveFrontAnalysis(lens)
    wa.drawAberrationPlot(angle,wavelength=wave,legend = "lower left")

    
    plt.show()

main()
            
    

