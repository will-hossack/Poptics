"""
    Phototube class to simulate photelecectric experimen in Physics 1B
"""
from poptics.wavelength import WaveLength,BandPassFilter,FilterStack,OpticalFilter
from scipy.integrate import quad
import numpy as np
import math



class PhotoCathode(OpticalFilter):
    """ Class to represent the photocathone as a short pass filter
        with a sharp cutoff at wavelength set by the voltage.

    :param workfunction: workfunction voltage of the device
    :param width: with od cutoff
    :param transmission: the transmission at long wavelength
    """
    def __init__(self,workfunction = 1.6,width = 0.03,transmission = 1.0):
        OpticalFilter.__init__(self,transmission)
        self.workfunction = workfunction
        self.alpha = math.tan(0.4*math.pi)/(0.5*width)
        self.setVoltage()

    def setVoltage(self,volt = 0.8):
        """
        Method to set the inverse bias voltage on the photocathode
        taking into account the workfunction.

        :param volt: the voltage (Default = 3.0)
        :type volt: float
        """
        self.cutoff = 1.237/(volt + self.workfunction)
        return self


    def __getNewValue__(self,wavelength):
        """
        Get the new value
        """

        dw = self.cutoff - wavelength
        return self.transmission*(math.atan(self.alpha*dw) + math.pi/2)/math.pi

        #if wavelength > self.cutoff:
        #    return 0.0
        #else:
        #    dw = self.cutoff - wavelength
        #    return 2.0*self.transmission*(math.atan(self.alpha*dw))/math.pi

class PhotoTube(WaveLength):
    """
    Class to implement a phototube, only the workfunction set in the
    constuctor

    :param workfunction: workfunction of the photocathode in eV (Default = 0.65)
    :type workfunction: float
    """

    def __init__(self,workfunction = 0.65):

        WaveLength.__init__(self)

        self.spectrum = None
        self.window = BandPassFilter(0.4,0.65,0.05) # Overall response
        self.cathode = PhotoCathode(workfunction,0.01) # The Photopcathode filter
        self.stack = FilterStack(self.window,self.cathode)
        self.range = [0.3,0.75]


    def setVoltage(self,volt = 0.0):
        """
        Method to set the inverse boas voltage on the photocathode

        :param volt: the voltage (Default = 0.0)
        :type volt: float
        """
        self.cathode.setVoltage(volt)
        return self

    def setSpectrum(self,spectrum):
        """
        Method to set the input spectrum falling on the photocathode

        :param sprecturm: the input light spectrum
        :type spectrum: Spectrum
        """
        self.spectrum = spectrum



    def getOutput(self,voltage):
        """
        Method to get the output voltage being an integral  over the
        response wavelengths at the specified voltage

        :param voltage: the applied bias voltage
        :type voltage: float
        """

        self.setVoltage(voltage)
        a,err = quad(self.getValue,self.range[0],self.range[1])
        return a

    def getArrayOutputs(self,voltage):
        """
        Get nparray of output voltages

        """
        output = np.zeros(voltage.size)
        for i,v in enumerate(voltage):
            output[i] = self.getOutput(v)

        return output


    def __getNewValue__(self, wave):
        """
        Internal method to get the new value (called by useds via getValue())
        """
        return self.spectrum.getValue(wave)*self.stack.getValue(wave)

