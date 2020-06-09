"""
Exaample program to read in a wavefront from a file, and plot vertical and horizontal
plots
"""

import optics.wavefront as wf
import matplotlib.pyplot as plt
import tio as t


def main():
    #       Read the wavefront in from a .wf file and display it contents
    wave = wf.WaveFront().fromFile()
    t.tprint(repr(wave))

    wave.plot()
    plt.show()


if __name__ == "__main__":
    main()
