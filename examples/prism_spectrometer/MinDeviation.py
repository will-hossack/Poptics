"""
    Simple program to set up a default spectometer with specified material
    and calcualte minimum deviation angle from terminal prompts.

"""

from poptics.spectrometer import PrismSpectrometer
from poptics.tio import getString,getFloat,tprint
import math

def main():

    #         Get name of index and make a default sprectometer with 60 degreee prism
    glassname = getString("Glass type",default = "BK7")
    prism = PrismSpectrometer(index = glassname)
    tprint(repr(prism))         # Show details of spectrometer

    #        Get a wavelngth, calculate min deviation and display it
    while True:
        wavelength = getFloat("Wavelength in um",min = 0.35,max = 1.0)
        mindeviation = math.degrees(prism.minDeviation(wavelength))
        tprint("Minimum deviation for {0:5.3f} um is : {1:7.4f} degrees".format(wavelength,mindeviation))

main()


