"""
        Test wavefron fitting

"""

from poptics.wavefront import WaveFront,WavePointSet,WavePoint
from poptics.vector import Vector2d
from poptics.tio import tprint
import matplotlib.pyplot as plt
import numpy as np


def main():

    #     Read in a wavefront
    wf = WaveFront().fromFile()
    tprint(repr(wf))
    wf.plot()

    ws = WavePointSet()

    radius = wf.getRadius()
    yscan = np.linspace(-radius,radius,11)
    xscan = np.linspace(-radius,radius,11)

    for y in yscan:
        for x in xscan:
            if x*x + y*y <= radius*radius:
                pt = Vector2d(x,y)
                wp = WavePoint(wavelength = 0.65).setWithWaveFront(wf,pt)
                ws.add(wp)


    zw = ws.fitZernike(4)
    tprint(repr(zw))
    zw.plot()
    #ws.plot()
    plt.show()


if __name__ == "__main__":
    main()