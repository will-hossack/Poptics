"""

Example program to create and display a few test surfaces

"""

from poptics.surface import CircularAperture, IrisAperture, SphericalSurface, ImagePlane
import matplotlib.pyplot as plt

def main():
    
    #       Make a set of surface
    op = ImagePlane(-100,30)
    ca = CircularAperture(-10,20)
    ia = IrisAperture(50,15).setRatio(0.7)
    fs = SphericalSurface(20,0.025,15,"BK7")
    bs = SphericalSurface(30,-0.025,15,"air")
    ip = ImagePlane(60,40)
    
    #      Plot them in a simple diagram 
    op.draw()
    ca.draw()
    ia.draw()
    fs.draw()
    bs.draw()
    ip.draw()
    plt.axis("equal")           # Set the x/y axis to the same scale 
    plt.show()

main()

