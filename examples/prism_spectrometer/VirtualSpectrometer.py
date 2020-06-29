"""
    Virtual Spectometer
    Example program to similate the output of of a prism spectrometer for a range
    of wavelengths read from a csv file
"""
import math
from poptics.spectrometer import PrismSpectrometer
from poptics.wavelength import MaterialIndex,Mercury_e
from poptics.tio import getFloat,tprint,getFilename,getBool
import matplotlib.pyplot as plt
from poptics.csvfile import readCSV,writeCSV



def main():

    #      First set up prism
    n = MaterialIndex()                   # get materail, angle and height
    prismAngle = getFloat("Prism angle in degrees",60.0)
    prismHeight =getFloat("Height of prism in mm",100.0)
    beam =getFloat("Beam Radius in mm",10.0)

    #       Set up spectrometer
    prism = PrismSpectrometer(0.0,prismAngle,prismHeight,n,beam)
    tprint(repr(prism))

    #        Get the setup wavelength (set prsm at min deviation)
    setupWavelength = getFloat("Set up wavelength",Mercury_e)
    prism.setUpWavelength(setupWavelength)

    #         Print out details
    deviation = prism.minDeviation()
    tprint("Min deviation : {0:6.4f} at : {1:6.4f}".format(math.degrees(deviation),setupWavelength))
    tprint("Max resolutions is : {0:7.3f}".format(prism.maxResolution(setupWavelength)))
    tprint("Resolution with specified beam : {0:7.3f}".format(prism.resolution()))

    #          Get the wavelengths and intensities of the spcetrum
    fileName = getFilename("Wavelength file","csv")
    wavelengths,intensities = readCSV(fileName)

    #        Give option for matplotplot or save to CSV

    if getBool("Display Graph",True):
        prism.plotSpectrum(wavelengths, intensities)
        plt.show()
    else:
        fieldAngle,spectrum = prism.getIntensitySpectum(wavelengths,intensities)
        fileName = getFilename("Output file","csv")
        n = writeCSV(fileName,[fieldAngle,spectrum])
        tprint("No of lines written: ",n)


if __name__ == "__main__":
    main()
