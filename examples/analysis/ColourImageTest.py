"""      Tests of Optical Image
"""

import matplotlib.pyplot as plt
from  poptics.analysis import ColourImage
from poptics.lens import SimpleSinglet

def main():

    oi = ColourImage(0,100,100,300,300)
    oi.addTestGrid(8,8,intensity = [1,1,1])


    #     Make plot area and plot target on the left
    plt.subplot(1,2,1)
    oi.draw()
    oi.draw()
    plt.show()
    lens = SimpleSinglet(200,80,10,index="SF11")



    im = oi.getSystemImage(lens,-0.2)

    print(repr(oi))
    print(repr(im))

    plt.subplot(1,2,2)
    im.draw()

    plt.show()


main()
