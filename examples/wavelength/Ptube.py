
"""
Created on Sun Jul  5 15:16:50 2020

@author: wjh
"""
#import poptics.wavelength as wave
from poptics.wavelength import PlanckSpectrum,LongPassFilter
from poptics.phototube import PhotoTube
import poptics.tio as tio
import matplotlib.pyplot as plt
import numpy as np







def main():


    spectrum = PlanckSpectrum(3500)
    fw = tio.getFloat("Filter cutoff",0.5)
    vl = tio.getFloat("Bias Voltage start",0.3)
    vh = tio.getFloat("Bias Voltage end",1.5)
    filter = LongPassFilter(fw)
    spectrum.addFilter(filter)
    photo = PhotoTube(1.6)
    photo.setSpectrum(spectrum)
    photo.setVoltage((vh + vl)/2)
    plt.subplot(2,2,1)
    spectrum.draw()
    plt.subplot(2,2,2)
    photo.stack.draw()
    plt.subplot(2,2,3)
    photo.draw()

    volt = np.linspace(vl,vh)
    outdata = photo.getArrayOutputs(volt)


    plt.subplot(2,2,4)
    plt.plot(volt,outdata)
    #photo.draw()
    plt.show()


main()



