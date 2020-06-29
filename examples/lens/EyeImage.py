"""

        Example of image of test pattern on Eye retina

"""
from poptics.analysis import OpticalImage
from poptics.lens import Eye
import matplotlib.pyplot as plt
from poptics.tio import tprint


def main():

    #     Make a test image of 100 x 100 pixels and size 300 x 300 mm
    #a4 -400 mm
    oi = OpticalImage(-400,100,100,300,300)
    oi.addTestGrid(8,8)           # Add a 8 x 8 test grid

    #plt.subplot(1,2,1)
    #oi.draw()

    eye = Eye(pixels =100)
    #eye.setNearPoint(400)
    tprint(repr(eye))
    #tprint("Focal length " + str(eye.backFocalLength()))

    ip = eye.getRetina()
    tprint(repr(ip))
    #ip.getImage(eye,oi)

    #     Make plot area and plot target on the left
    #plt.subplot(1,2,2)
    ip.draw()

    plt.show()


if __name__ == "__main__":
    main()