"""
    Print out the names of the 36 Optical Zernike coefficients alls set to zero
"""

from poptics.zernike import opticalZernikeName

def main():

    #      Make a list of zero with 36 elements
    z = [0.0]*36

    #      Do a print
    print(opticalZernikeName(z))


if __name__ == "__main__":
    main()