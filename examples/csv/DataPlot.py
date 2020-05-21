""" 
Simple Python programme to read in a multi collumn CSV fine and plot
the first two colums as a x/y graph. If there is a third colulm it
will be used for the y error bars.

"""


import matplotlib.pyplot as plt
import poptics.csvfile as f     # Local CVS reader
import poptics.tio as t


def main():

    file = t.getFilename("File","txt")  # get filename with .txt default 
    data = f.readCSV(file)              # Default csv read to array on np.array

    
    if data.shape[0] > 2:               # If three cols use errors
        yErr = data[2]                  # set yErr to column 2 
    else:
        yErr = None                     # Set to None

    #        Plot out data with errors bars and sensible titles.
    plt.errorbar(data[0],data[1],xerr=0.0,yerr=yErr,fmt="bx")
    plt.title("Data Plot: {0:s}".format(file))
    plt.xlabel("x value")
    plt.ylabel("y value")
    plt.show()

main()
