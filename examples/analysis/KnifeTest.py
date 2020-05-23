"""
    Simple appliaction to perform a Focul Knife Edge test of
    a specified lens .

Author: Will Hossack, The University of Edinburgh
"""
from poptics.lens import DataBaseLens
from poptics.analysis import KnifeTest
import matplotlib.pyplot as plt
import math
from poptics.tio import getFloat,getInt

def main():

    #         Get the lens from database
    lens = DataBaseLens()
    angle = math.radians(getFloat("Ray Angle in degrees"))
    opt = getInt("Focal Option",1)
    kangle = math.radians(getFloat("Knife angle in degrees",0.0))
    kt = KnifeTest(lens,angle,opt)
    knife = getFloat("Knife",0.0)
    kt.setKnife(knife,kangle)
    kt.getImage().draw()
    plt.show()

main()
    
