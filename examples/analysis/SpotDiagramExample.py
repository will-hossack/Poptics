"""
   Example Programme to for a Spot Digram using high level SpotAnalysis class


"""

from poptics.lens import DataBaseLens
from poptics.vector import Angle,Unit3d
from poptics.wavelength import getDefaultWavelength
from poptics.analysis import SpotAnalysis
from poptics.tio import getFloat
import matplotlib.pyplot as plt

def main():

    #      Get lens from database 
    lens = DataBaseLens()       
    
    #           Get angle of beam and wavelnegth 
    angle =getFloat("Angle in degrees",0.0,0.0,15.0)
    u = Unit3d(Angle().setDegrees(angle))     # Angle as unit vectr
    wave = getFloat("Wavelength",getDefaultWavelength())


    #            Get optimal area psf and create a SpotDiagram 
    sd = SpotAnalysis(lens,u,0,wavelength = wave)

    #             Go round loop plotting the sopt diagram as various zplane positions

    while True:
        zp = getFloat("Delta",0.0)
        
        sd.draw(zp, True)
        pos = sd.plane.getPoint().z 
        print("Plane pos " + str(pos))
        plt.title("Spot diagram")
        plt.show(block = True)
    

main()
