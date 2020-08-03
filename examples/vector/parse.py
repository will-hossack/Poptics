"""
Parse angle test
"""

from poptics.vector import Vector3d,Unit3d
from poptics.tio import getString,getUnit3d






def main():

    a = Vector3d(1,2,3)
    b = a.set([4,5,6])
    print(repr(b))
    u = Unit3d().parseAngle("35","71")
    print(repr(u))

    v = getUnit3d("Direction")
    print(repr(v))

main()