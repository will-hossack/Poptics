"""
   Basic use of the file handing methods

Author: Will Hossack, The University of Edinburgh.
"""
import poptics.tio as t
import math

def main():

    n = t.getFilename("File Name","csv","$HOME/mydata")
    t.tprint("Name is : " ,n)

    file = t.openFile("File","r","jpg","$HOME/Desktop/wjh")

main()
