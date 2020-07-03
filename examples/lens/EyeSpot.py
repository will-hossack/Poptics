"""

Program to explore stop diagrams on the back of the retina in the Eye class
"""
from poptics.lens import Eye
from poptics.ray import RayPencil,RayPath
from poptics.tio import getFloat,tprint,getUnit3d
from poptics.psf import Psf,SpotDiagram
import matplotlib.pyplot as plt

def main():

        lens = Eye()
        iris = getFloat("Iris",1.0)
        lens.setIris(iris)

        u = getUnit3d("Direction",0.0)

        vpencil = RayPencil().addBeam(lens,u,key="vl").addMonitor(RayPath())
        spencil = RayPencil().addBeam(lens,u,key="array")


        vpencil *= lens
        spencil *= lens
        plane = lens.getRetina()

        ps = Psf().setWithRays(spencil,plane)
        tprint("PSF is",repr(ps))

        plt.subplot(2,1,1)
        lens.draw()
        vpencil.draw()
        plt.axis("equal")

        plt.subplot(2,1,2)
        spot = SpotDiagram(spencil)
        spot.draw(plane,True)

        plt.show()



main()
