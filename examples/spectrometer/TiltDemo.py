
"""
    Profram to demonstrate tiliting a prism

"""
from poptics.spectrometer import PrismSpectrometer
from poptics.wavelength import Green,Helium_d
from poptics.tio import tprint
import math
import numpy as np
import matplotlib.pyplot as plt

def main():

        # Default spectrometer
        prism = PrismSpectrometer()
        prism.setUpWavelength(Helium_d)
        tprint(repr(prism))

        # Get min deviation at current wavelength
        minDev = prism.minDeviation()

        midAngle = minDev/2
        tprint("Min deviations : ",minDev," Beam angle : ",midAngle)

        dtilt = math.radians(10)

        tiltData = np.linspace(-dtilt,dtilt,50)
        angleData = np.zeros(tiltData.size)

        for i,tilt in enumerate(tiltData):
            prism.setTilt(tilt)
            angleData[i] = prism.getOutputAngle(midAngle,Helium_d)

        plt.plot(np.degrees(tiltData),np.degrees(angleData))
        plt.show()





if __name__ == "__main__":
    main()

