"""
   basic use of the tio input/output module

Author: Will Hossack, The Univesrity of Edinburgh
"""

from poptics.tio import getFloat,getBool,getInt,getComplex,tprint


def main():
    #     Get a float with default and range checking
    f = getFloat("Give a float",3.0,0.0,5.0)
    tprint("Float is : ", f)

    #     Get a logical within a if statemnet
    if getBool("Logical",True):
        tprint("True")
    else:
        tprint("False")

    #     Get an integer with no default but range ckecking
    i = getInt("Integer Value",min = 5,max = 10)
    tprint("Integer Value is : ", i)

    # Get a complex with default and range check of maximum absolute value
    c = getComplex("Complex Number",3+4j, maxabs = 100.0)
    tprint("Complex is : ", c)


main()

