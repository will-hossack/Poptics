"""
        Optimal Bend of singlet
"""

from poptics.lens import SimpleSinglet
from poptics.psf import Psf
from poptics.ray import RayPencil
from poptics.tio import getUnit3d,tprint
import matplotlib.pyplot as plt
import numpy as np



def main():
    singlet = SimpleSinglet()
    u = getUnit3d("Direction",0.0)

    ip = singlet.backFocalPlane()

    bdata = np.linspace(-1.0,1.0)
    adata = np.zeros(bdata.size)

    for i,bend in enumerate(bdata):
        singlet.setBend(bend,True)
        pencil = RayPencil().addBeam(singlet,u,"array")


        pencil *= singlet
        pencil *= ip

        psf = Psf().optimalArea(pencil, ip)
        adata[i] = psf.area()

    plt.plot(bdata,adata)
    plt.show()

if __name__ == "__main__" :
    main()




