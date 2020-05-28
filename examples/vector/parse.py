"""
Parse angle test
"""

from poptics.vector import Vector3d,Unit3d,Angle
import math
from poptics.tio import getString


    



def main():
    
    a = Vector3d(1,2,3)
    b = a.set([4,5,6])
    print(repr(b))
    u = Unit3d().parseAngle("35","71")
    print(repr(u))
    
    s = getString("string")
    v = Unit3d().parseAngle(s)
    print(repr(v))

main()