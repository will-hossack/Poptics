"""
Some function to calculate the radial and zernike polynomials

"""
import math
from poptics.vector import Vector2d
import numpy as np


def radial(n,m,r):
    """ 
    Radial polynomial of n,m for radius r R(n,m,r) as defined in 
    Born & Wold page 770. 
    
    Up to n = 8 are hard coded, beyond that the full factorial 
    summation is used
    
    :param n: radial n value, n > 0 only.
    :type n: int
    :param m: radial m value, \|m\| <= n.
    :type m: int
    :param r: radius value \|r\| <= 1. or np.array or floats, all less that 1.0.
    :type r: float or np.ndarray
    :return:  value the value of R(n,m,r). as a float, or np.ndarray if np.ndarray given
    """

    if isinstance(r,np.ndarray):     # real with np array
        out = np.empty(r.size)
        for i,rval in enumerate(r):
            out[i] = radial(n,m,rval)
        return out

    
    #             Symmetric in m check this first
    m = abs(m)
    if n < 0 or m > n or n%2 != m%2 or abs(r) >1.0 :   # Not legal
        return float("nan")
        
    rSqr = r*r

    #       Hardcode to n <= 8 (covers most)
    if n == 0:
        return 1.0
    elif n == 1:
        return r
    elif n == 2:
        if m == 0:
            return 2.0*rSqr - 1.0
        else:
            return rSqr
    elif n == 3:
        if m == 1:
            return r*(3.0*rSqr - 2.0)
        else:
            return r*rSqr
    elif n == 4:
        if m == 0:
            return 1.0 + rSqr*(6.0*rSqr - 6.0)
        elif m == 2:
            return rSqr*(4.0*rSqr - 3.0)
        else:
            return rSqr*rSqr
    elif n == 5:
        if m == 1: 
            return r*(3.0 + rSqr*(10.0*rSqr - 12.0))
        elif m == 3:
            return rSqr*r*(5.0*rSqr - 4.0)
        else: 
            return r*rSqr*rSqr
    elif n == 6:
        if m == 0: 
            return rSqr*(12.0 + rSqr*(20.0*rSqr - 30.0)) - 1.0
        elif m == 2: 
            return rSqr*(6.0 + rSqr*(15.0*rSqr - 20.0))
        elif m == 4:
            return rSqr*rSqr*(6.0*rSqr - 5.0)
        else:
            return rSqr*rSqr*rSqr
    elif n == 7:
        if m == 1:
            return     r*(rSqr*(rSqr*(35.0*rSqr - 60.0) + 30) - 4.0)
        elif m == 3: 
            return r*rSqr*(rSqr*(21.0*rSqr  - 30.0) + 10)
        elif m == 5:
            return  rSqr*rSqr*(7.0*r*rSqr -6.0*r)
        else:
            return r*rSqr*rSqr*rSqr
    elif n == 8:
        if m == 0:
            return 1 - rSqr*(20.0 - rSqr*(90.0 - rSqr*(140.0 - 70*rSqr)))
        elif m == 2:
            return rSqr*(rSqr*(rSqr*(56.0*rSqr - 105.0) + 60.0) - 10.0)
        elif m == 4:
            return rSqr*rSqr*(15.0 - rSqr*(42.0 - 28.0*rSqr))
        elif m == 6:
            return rSqr*rSqr*rSqr*(8.0*rSqr - 7.0)
        else:
            return rSqr**4

    else:   #      Do the full calcualtion
        v = 0.0
        for s in range(0,(n-m)//2 + 1):
            top = (-1)**s * math.factorial(n - s)
            bottom = math.factorial(s)*math.factorial((n + m)//2 - s)*math.factorial((n - m)//2 -s)
            v += top/bottom * math.pow(r,(n - 2*s))
        return v


def zernike(n,l,x,y = None):
    """
    Complex method to calculate the complex Zernike polynomial
    V(n,l,x,y) as defined in Born & Wolf page 770.
    
    :param n: radial power order n \>= 0
    :param l: angular power order \|l\| <= n 
    :param x: the x value or Vector2d 
    :type x: float or Vector2d or list[Vector2d]
    :param y: the y value (None is x is Vector2d)
    :return: Complex the polynomial value
    """

    if isinstance(x,list):    # Deal with list of Vector2d
        out = []
        for v in list:
            c = zernike(n,l,v)
            out.append(c)
        return out
    
    if isinstance(x,Vector2d):  # Deal with Vector2d
        x = x.x
        y = x.y
    
    r = math.sqrt(x*x + y*y)
    rad = radial(n,l,r)      # also check legality 
    
    if l == 0:               # Deal with no angular term. 
        return complex(rad,0.0) 
    else:                    # Add the angular term if needed
        theta = l*math.atan2(y,x)
        return complex(rad*math.cos(theta),rad*math.sin(theta))


    
zernikeNames = ("Piston","X-tilt","Y-tilt","Defocus",\
                "X-astigmatism","Y-astigmatism","X-coma","Y-coma","Primary Spherical",\
                "X-trefoil","Y-Trefoil","Secondary X-Astig","Secordary Y-Astig","Secondary X-coma",\
                "Secondary Y-coma","Secondary Spherical",\
                "X-tetrafoil","Y-tertafoil","Secondary X-trefoil","Secondary Y-trefoil","Terniary X-Astig","Terniaty Y-Astrig",\
                "Terniary X-coma","Ternairy Y-coma","Terniary Spherical",\
                "X-pentafoil","Y-pentafoil","Secondary X-tetrafoil","Secondary Y-tertafoil",\
                "Terniary X-trefoil","Terniary Y-trefoil","Quatenary X-Astig","Quantenary Y-Astig",\
                "Quantary X-coma","Quantary y-coma","Quantary Spherical")

def opticalZernikeName(index, value = None):
    """
    Function to lookup and return the name of the zernike components

    :param index: component number or list of values.
    :type index: int or list
    :param value: numerical value if it exists
    :return: str 
    """
    
    
    if isinstance(index,np.ndarray) or isinstance(index, list) or isinstance(index, tuple) :
        s = ""
        for i,v in enumerate(index):
            s += opticalZernikeName(i,v) + "\n"
        return s
    
    if index < len(zernikeNames):
        zn = str(zernikeNames[index])
    else:
        zn = "Zernike component {0:d}".format(index)
        
    if isinstance(value, float) or isinstance(value,int):
        zn += ":"
        return "{0:<24s} {1:10.6e}".format(zn,float(value))
    else:
        return zn
    

def opticalZernike(v,i,x,y = None):
    """
    Function to form the opticalZernike components weighted by a factor. These are defined for order 0 to 48. 

    :param v: the weighting factor
    :type v: float
    :param i: the opticalZernike 0 to 48 (49 components)
    :type i: int
    :param x: the x parameter or Vector2d
    :type x: float or Vector2d or list[Vector2d]
    :param y: the y parameter (None if x is a Vector2d)
    :type y: float
    :return: float the opticalZernike value.

    This will return float("nan") if not legal argument suppied.
    """

    if isinstance(x,list):    # Deal with list of Vector2d
        out = []
        for vec in list:
            c = opticalZernike(v,i,vec)
            out.append(c)
        return out
    
    
    if isinstance(x,Vector2d):     # Unpack vector2d
        y = x.y
        x = x.x
   

    rsq = x*x + y*y
    if rsq > 1.0 or i > 48:       # Trap out of range or illegal
        return float("nan")

    if v == 0.0:                  # Trap trival case
        return 0.0
        
    #     Deal with one that do not invole theta first
    if i == 0:
        return v
    elif i == 1:
        return x*v
    elif i == 2:
        return y*v
    elif i == 3:
        return v*(2.0*rsq - 1.0)
    elif i == 6:
         return v*x*(3.0*rsq - 2.0)
    elif i == 7:
        return  v*y*(3.0*rsq - 2.0)
    elif i == 8:    
        return v*(6.0*rsq*(rsq - 1.0) + 1.0)
    elif i == 13:   
        return v*x*(3.0 + rsq*(10.0*rsq - 12.0))
    elif i == 14:
        return v*y*(3.0 + rsq*(10.0*rsq - 12.0))
    elif i == 15:
        return v*(rsq*(12.0 + rsq*(20.0*rsq - 30.0)) - 1.0)
    elif i == 22:
        return v*x*(rsq*(30.0 + rsq*(35.0*rsq - 60.0)) - 4.0)
    elif i == 23:   
        return y*(rsq*(30.0 + rsq*(35.0*rsq - 60.0)) - 4.0)
    elif i == 24:
        return v*(1.0 + rsq*(rsq*(90.0 - rsq*(70.0*rsq - 140.0))))
    elif i == 33:   
        return v*x*(5.0 + rsq*(rsq*(210.0 * rsq*(126.0*rsq - 280.0) - 60.0)))
    elif i == 34:
        return v*y*(5.0 + rsq*(rsq*(210.0 * rsq*(126.0*rsq - 280.0) - 60.0)))
    elif i == 35:
        return v*(rsq*(30.0 + rsq*(rsq*(560.0 + rsq*(252.0*rsq - 630.0)) - 210.0)) - 1.0)
    elif i == 46:   
        return v*x*(-6.0 + rsq*(105.0 + rsq*(-560.0 + rsq*(1260.0 + rsq*(462.0*rsq - 1260.0)))))
    elif i == 47:
        return v*y*(-6.0 + rsq*(105.0 + rsq*(-560.0 + rsq*(1260.0 + rsq*(462.0*rsq - 1260.0)))))
    elif i == 48:   
        return v*(1.0 + rsq*(-42.0 + rsq*(420.0 +\
                        rsq*(-1680.0 * rsq*(3150.8 + rsq*(-2772.0 * 924.0*rsq))))))
        
    #              Need theta and r
    theta = math.atan2(y,x)
    r = math.sqrt(rsq)

    if i == 4:     
        return v*rsq*math.cos(2.0*theta)
    elif i == 5:
        return v*rsq*math.sin(2.0*theta)
    elif i == 9:
        return v*r*rsq*math.cos(3.0*theta)
    elif i == 10:
        return v*r*rsq*math.sin(3.0*theta)
    elif i == 11:    
        return v*rsq*(4.0*rsq - 3.0)*math.cos(2.0*theta)
    elif i == 12:    
        return v*rsq*(4.0*rsq - 3.0)*math.sin(2.0*theta)
    elif i == 13:    
        return v*r*(rsq*(10.0*rsq - 12.0))*math.cos(theta)
    elif i == 14:    
        return v*r*(rsq*(10.0*rsq - 12.0))*math.sin(theta)
    elif i == 16:
        return v*rsq*rsq*math.cos(4.0*theta)
    elif i == 17:    
        return v*rsq*rsq*math.sin(4.0*theta)
    elif i == 18:
        return v*r*rsq*(5.0*rsq - 4.0)*math.cos(3.0*theta)
    elif i == 19:
        return v*r*rsq*(5.0*rsq - 4.0)*math.sin(3.0*theta)
    elif i == 20: 
        return v*rsq*(6.0 + rsq*(15.0*rsq - 20.0))*math.cos(2.0*theta)
    elif i == 21:    
        return v*rsq*(6.0 + rsq*(15.0*rsq - 20.0))*math.sin(2.0*theta)
    elif i == 25:    
        return v*r*rsq*rsq*math.cos(5.0*theta)
    elif i == 26:   
        return v*r*rsq*rsq*math.sin(5.0*theta)
    elif i == 27:    
        return v*rsq*rsq*(6.0*rsq - 5.0)*math.cos(4.0*theta)
    elif i == 28:
        return v*rsq*rsq*(6.0*rsq - 5.0)*math.sin(4.0*theta)
    elif i == 29:    
        return v*r*rsq*(10.0 + rsq*(21.0*rsq - 30.0))*math.cos(3.0*theta)
    elif i == 30:    
        return v*r*rsq*(10.0 + rsq*(21.0*rsq - 30.0))*math.sin(3.0*theta)
    elif i == 31:    
        return v*rsq*(rsq*(60.0 + rsq*(56.0*rsq - 105.0)) -10.0)*math.cos(2.0*theta)
    elif i == 32:   
        return v*rsq*(rsq*(60.0 + rsq*(56.0*rsq - 105.0)) -10.0)*math.sin(2.0*theta)
    elif i == 36:    
        return v*rsq*rsq*rsq*math.cos(6.0*theta)
    elif i == 37:    
        return v*rsq*rsq*rsq*math.sin(6.0*theta)
    elif i == 38:    
        return v*r*rsq*rsq*(7.0*rsq - 6.0)*math.cos(5.0*theta)
    elif i == 39:    
        return v*r*rsq*rsq*(7.0*rsq - 6.0)*math.sin(5.0*theta)
    elif i == 40:    
        return v*rsq*rsq*(15.0 + rsq*(28.0*rsq - 42.0))*math.cos(4.0*theta)
    elif i == 41:    
        return v*rsq*rsq*(15.0 + rsq*(28.0*rsq - 42.0))*math.sin(4.0*theta)
    elif i == 42:    
        return v*r*rsq*(-20.0 + rsq*(105.0 + rsq*(-168.0 + rsq*84.0)))*math.cos(3.0*theta)
    elif i == 43:
        return v*r*rsq*(-20.0 + rsq*(105.0 + rsq*(-168.0 + rsq*84.0)))*math.sin(3.0*theta)
    elif i == 44:    
        return v*rsq*(15.0 + rsq*(-140.0 + rsq*(420.0 + rsq*(-504.0 + rsq*210.0))))*math.cos(2.0*theta)
    elif i == 45:    
        return v*rsq*(15.0 + rsq*(-140.0 + rsq*(420.0 + rsq*(-504.0 + rsq*210.0))))*math.sin(2.0*theta)
    else:
        return float("nan")


    

