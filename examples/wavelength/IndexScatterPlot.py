
"""
        Scatter plot of Nd/Vd for materails in the DataBase
"""

from poptics.material import MaterialData
from poptics.wavelength import MaterialIndex
import matplotlib.pyplot as plt

def main():

    #      Get the list of materails
    mlist = MaterialData().getList()
    print(str(mlist))

    nData = []
    vData = []

    for key in mlist[3:]:                   # Ignore first 3 (air/helium/water)
        index = MaterialIndex(key)          # Get the material
        nData.append(index.getNd())         # Get Nd and Vd to list
        vData.append(index.getVd())

    #       Do the plot
    plt.scatter(nData,vData)
    plt.title("Plot of Vd against Nd")
    plt.xlabel("Nd of Material")
    plt.ylabel("Vd of Material")
    plt.grid()
    plt.show()



if __name__ == "__main__" :
    main()
