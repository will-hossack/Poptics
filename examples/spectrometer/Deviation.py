"""
    Program to read in a spectrometer definition file and file of wavelength
    and output the minimun deviations in a CSV file

"""
from poptics.spectrometer import PrismSpectrometer
import poptics.csvfile as csv
from poptics.tio import getFilename,tprint
import numpy as np

def main():

    #        Get sprectometer from definition file
    spectrometer = PrismSpectrometer().fromFile("bk7")
    tprint(repr(spectrometer))

    #        Get wavelength from csv file (only first col)
    wavein = getFilename("File of wavelength","csv")
    wave, = csv.readCSV(wavein,[True,False])
    tprint(str(wave))

    #        Make array to hold angles
    angle = np.empty(wave.size)

    #        Make the angle array in degrees
    for i,w in enumerate(wave):
        angle[i] = np.degrees(spectrometer.minDeviation(w))

    tprint(str(angle))

    #       Output to csv file with wave , angle
    waveout = getFilename("Output file","csv")
    n = csv.writeCSV(waveout,[wave,angle])
    tprint("No of lines writen : ",n)


if __name__ == "__main__":
    main()
