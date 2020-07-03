"""
    Simply test of the Eye class

"""


from poptics.lens import Eye
from poptics.ray import RayPencil,RayPath
import poptics.wavelength as wl
import matplotlib.pyplot as plt
import math
from poptics.vector import Unit3d

def main():


    eye = Eye(0.0)
    print("Original Focalength : " + str(eye.backFocalLength(wl.PhotopicPeak)))
    #eye.setIris(0.5)
    eye.moveRetina(1.0)

    #eye.setNearPoint(300)
    #print("Modified Focalength : " + str(eye.backFocalLength(wl.PhotopicPeak)))

    theta = 10
    u = Unit3d().parseAngle(math.radians(theta))
    pencil = RayPencil().addBeam(eye,u,"vl",10,wl.Red)
    pencil.addBeam(eye,u,"vl",10,wl.Green)
    pencil.addBeam(eye,u,"vl",10,wl.Blue)
    pencil.addMonitor(RayPath())
    pencil *= eye

    eye.draw()
    pencil.draw()
    plt.axis("equal")
    plt.grid()
    plt.show()



main()
