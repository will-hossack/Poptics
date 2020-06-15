"""
        Test wavefron fitting, read in a wavefront from a file, form a
        WavePointSet and then fits Zernike Optrical Coefficients.

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
    wf.plot()                  # Make vertical + horizontal plot


    radius = wf.getRadius()
    yscan = np.linspace(-radius,radius,11)     # x/y positions of points
    xscan = np.linspace(-radius,radius,11)

    ws = WavePointSet(radius)        # Start with blanks set of points
                               # Make grid of points
    for y in yscan:
        for x in xscan:
            if x*x + y*y <= radius*radius:   # Inside circle
                pt = Vector2d(x,y)
                wp = WavePoint(wavelength = 0.65).setWithWaveFront(wf,pt)
                ws.add(wp)                   # Add to wavepoint set


    #       Fit zernike to 4th orders
    zw = ws.fitZernike(4)
    tprint(repr(zw))
    tprint("Error is : ",str(ws.zerr))      # Show the fitting error for each component
    zw.plot()     # Plot to same graph
    #ws.plot()
    plt.show()    # Show the final plot


if __name__ == "__main__":
    main()