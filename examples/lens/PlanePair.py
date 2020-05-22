"""
Example code to take a use a DataBaseLens and form an optical system with
a 100mm object and a magnification of -0.3. 

Program generated a image plane, sets the locations of the object and image
plane and plots a raypencil

"""

from poptics.lens import DataBaseLens
from poptics.ray import RayPencil, RayPath
import matplotlib.pyplot as plt



def main():

    lens = DataBaseLens("Tessar-F4.5")  # Get lens from database
    lens.setFocalLength(50)             # Set focal length by scaling
    print(repr(lens))

    mag = -0.3                          # Set magnification
    obj,ima = lens.planePair(mag)        # Make pair of planes,
    print("Object Plane : " + str(repr(obj)))
    print("New Image Plane : " + str(repr(ima)))
    
    #     Make a ray pencil from point in object 
    pencil = RayPencil().addBeam(lens,obj.getSourcePoint(0.0,10.0))
    pencil.addMonitor(RayPath())

    # Propgate pencil through lens to image plane
    pencil *= lens
    pencil *= ima

    
    #     Make plot
    lens.draw(True,True)    # With paraxial planes and legend
    obj.draw()
    ima.draw()
    pencil.draw()
    plt.title(lens.title)
    plt.axis("equal")
    plt.show()
    
    
    
main()
