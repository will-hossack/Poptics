"""


    Example program to similate the output of of a prism spectrometer for a range
    of wavelengths read from a csv file
"""
import math
from poptics.spectrometer import PrismSpectrometer
from poptics.wavelength import MaterialIndex,Mercury_e
import poptics.tio as t
import matplotlib.pyplot as plt
from poptics.csvfile import readCSV,writeCSV



def main():

    #      First set up prism
    n = MaterialIndex()                   # get materail, angle and height
    prismAngle = t.getFloat("Prism angle in degrees",60.0)
    prismHeight = t.getFloat("Height of prism",100.0)
    beam = t.getFloat("Beam Radius",10.0)

    #       Set up spectrometer
    prism = PrismSpectrometer(0.0,prismAngle,prismHeight,n,beam)
    t.tprint(repr(prism))


    setupWavelength = t.getFloat("Set up wavelength",Mercury_e)
    prism.setUpWavelength(setupWavelength)
    deviation = prism.minDeviation()
    t.tprint("Min deviation : {0:6.4f} at : {1:6.4f}".format(math.degrees(deviation),setupWavelength))
    t.tprint("Max resolutions is : {0:7.3f}".format(prism.maxResolution(setupWavelength)))
    t.tprint("Resolution with specified beam : {0:7.3f}".format(prism.resolution()))

    #          Get the wavelengths and intensities of the spcetrum
    fileName = t.getFilename("Wavelength file","csv")
    wavelengths,intensities = readCSV(fileName)


    if t.getBool("Display Graph",True):
        prism.plotSpectrum(wavelengths, intensities)
        plt.show()
    else:
        fieldAngle,spectrum = prism.getIntensitySpectum(wavelengths,intensities)
        fileName = t.getFilename("Output file","csv")
        n = writeCSV(fileName,[fieldAngle,spectrum])
        t.tprint("No of lines written: ",n)







main()
