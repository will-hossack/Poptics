"""
          Plot a TargetImage
"""




from poptics.analysis import TargetPlane
from poptics.lens import SimpleSinglet
from poptics.tio import tprint
from poptics.psf import Psf
from poptics.wavelength import WavelengthColour
import matplotlib.pyplot as plt


def main():


    lens = SimpleSinglet(200,80,10)
    obj,im = lens.planePair(-0.2,200.0)
    tprint("Object plane : " + repr(obj))
    tprint("Image plane : " + repr(im))


    objectTarget = TargetPlane(obj,wavelength = 0.6)
    imageTarget = TargetPlane(im)

    objectTarget.addGrid(5,5)

    fig = plt.figure()
    panel = fig.add_subplot(1,1,1)
    panel.axis('equal')

    imageTarget.draw()

    targetPencil = objectTarget.getPencils(lens, wavelength = 0.45)

    for pencil in targetPencil:
        pencil *= lens
        pencil *=imageTarget
        psf = Psf().setWithRays(pencil,imageTarget)
        psf.draw(colour = WavelengthColour(0.45))

    plt.show()

main()
