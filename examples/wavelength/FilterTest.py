
"""
       Test the optical filter classes

"""

import matplotlib.pyplot as plt
import poptics.tio as tio
import poptics.wavelength as wave



def main():


    wl = tio.getFloat("Long Cut off",0.4)
    ws = tio.getFloat("Short Cut off",0.5)
    dw = tio.getFloat("dw",0.01)



    short = wave.ShortPassFilter(ws,dw)
    long = wave.LongPassFilter(wl,dw)
    stack = wave.FilterStack(short,long)


    tio.tprint(long.getValue(wl + dw/2),"   ", long.getValue(wl - dw/2))
    tio.tprint(short.getValue(ws + dw/2),"   ", short.getValue(ws - dw/2))


    notch = wave.NotchFilter(0.5)

    spectrum = wave.Spectrum()
    spectrum.addFilter(notch)
    spectrum.draw()



    plt.show()

main()

