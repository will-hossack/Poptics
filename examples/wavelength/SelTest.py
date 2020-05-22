import poptics.wavelength as w
from poptics.tio import getFloat, tprint
import matplotlib.pyplot as plt

def main():



    l0 = getFloat("Lambda_0",0.08)
    beta = getFloat("Beta",1.25)
    index = w.Sellmeier(beta,l0)

    nd = index.getNd()
    vd = index.getVd()
    tprint("Nd index : ",nd," Abbe No: ",vd)

        
    index.draw()
    plt.show()
    
main()

