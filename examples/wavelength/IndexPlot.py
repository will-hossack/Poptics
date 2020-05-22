"""
    Example program to plot refractive index against wavelength is a default plot

"""
from poptics.wavelength import MaterialIndex
import matplotlib.pyplot as plt

def main():
        #       Get a material index, the defaut is to prompt for key
        index = MaterialIndex()
        index.draw()
        plt.show()
        
        


main()