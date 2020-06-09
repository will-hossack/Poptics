"""
Exaample program to read in a wavefront from a file, display the contents
and plot display the wavefront an an interferogram with optional x/y tilts
"""

from poptics.wavefront import WaveFront,Interferometer,AnnularMask
import matplotlib.pyplot as plt
from poptics.tio import tprint,getFloat



def main():
    #       Read the wavefront in from a .wf file and display it contents
    wave = WaveFront().fromFile()
    #wave.setMask(AnnularMask(wave.radius,0.7))    # Uncomment for annual mask

    tprint(repr(wave))

    #       Get the tilts
    xt = getFloat("Xtilt",0.0)
    yt = getFloat("Ytilt",0.0)

    #       Make the interferometed
    inter = Interferometer(wave)
    inter.setTilt(xt,yt)             # Set the tilts
    inter.draw()                     # Display
    plt.show()

if __name__ == "__main__":
    main()
