"""
         Example to form an imaging system with specified magnification
         and plot out system with ray pencil.
"""


from poptics.matrix import DataBaseMatrix
from poptics.ray import RayPencil,RayPath
from poptics.tio import getFloat,tprint
import matplotlib.pyplot as plt

def main():


    lens = DataBaseMatrix("Tessar-100")      # get a lens from the database
    lens.setFocalLength(80.0)                # Set the focal length to 80mm
    lens.setInputPlane(120)
    
    #               Get system parameters
    mag = getFloat("Magnification",-2)
    ysize = getFloat("Height of Object plane",20.0)
    
    
    #               Mage a pair of io / outplut place 
    op,ip  = lens.planePair(ysize,mag)
    tprint("Object plane at ; " + str(op.inputPlane()))
    tprint("Image plane at ; "+ str(ip.inputPlane()))
    
    #               make a stsrem that conatins planes and lens in ordedr 
    

    #                Maake a source bema from lower edge of object plane
    pencil = RayPencil().addSourceParaxialBeam(lens,-ysize, op).addMonitor(RayPath())
    #                Portagate throgh system
    pencil *= lens
    pencil *= ip

    #                Draw out the sytsem
    op.draw()
    lens.draw(True)   # Add a legend box
    ip.draw()
    pencil.draw()
    plt.axis("equal")
    plt.show()

main()
