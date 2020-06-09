"""
Program to read in wavelength , index values from CSV file and
fit first order Sellmier

"""

from poptics.csvfile import readCSV
from poptics.wavelength import Sellmeier,Sodium_D
from poptics.tio import getFilename, tprint
import matplotlib.pyplot as plt

def main():

    #      Read in csv filename
    file = getFilename("File","csv")   # Open File
    wave,ref = readCSV(file)           # Read to two np arrays

    #    Create a Sellmier index and it it to the read in np arrays
    index = Sellmeier().fitIndex(wave,ref)

    #     Print out results and Nd / Vd values
    tprint("Index : " , repr(index))
    tprint("Nd : ",index.getNd()," Vd : ",index.getVd())

    #     Get the digital rerivative at the Sodium Doublet
    dn = index.getDerivative(Sodium_D)
    tprint("Derivative is : ", dn)

    #     Plot out the data valuse a s x
    plt.plot(wave,ref,"x")
    index.draw()       # Defaul draw of the index from 0.35 -> 0.7
    plt.title("Plot of Sellmeier index")
    plt.ylabel("Index")
    plt.show()


if __name__ == "__main__" :
    main()

