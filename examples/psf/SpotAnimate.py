"""
   Example Programme for SpotAnimation


"""

from poptics.lens import DataBaseLens
from poptics.psf import SpotAnimation
from poptics.ray import RayPencil
from poptics.wavelength import Default
from poptics.tio import getUnit3d,getFloat

import matplotlib.pyplot as plt



def main():

    #      Get lens from database
    lens = DataBaseLens()

    #           Get angle of beam and wavelnegth
    u = getUnit3d("Direction",0.0)
    w = getFloat("Wavelength",Default)

    #    Make a ray through lens
    pencil = RayPencil().addBeam(lens,u,"array",wavelength=w)
    pencil *= lens       # Propagate through lens

    sd = SpotAnimation(pencil)

    #             Go round loop plotting the sopt diagram as various zplane positions
    bf = lens.backFocalPlane()     # Back focal plane
    sd.run(bf)          #1.0,0.1,400)
    #plt.show()


main()
