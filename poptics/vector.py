"""
    Set of classes to support two and three dimensional vector manipulation.
"""

import math
from random import uniform


class Vector2d(object):
    """
    Class to implement two dimensional vector with supporting classes and
    operator overloads.

    :param x: x component or pair of components.
    :type x: float or Vector2d or list or tuple
    :param y: y component (Default = 0.0)
    :type y: float
    """

    def __init__(self, x=0.0, y=0.0):
        """
        Constructor.
        """
        if isinstance(x, Vector2d):    # Vector given
            self.x = x.x
            self.y = x.y
        elif isinstance(x, (list, tuple)):
            self.x = float(x[0])
            self.y = float(x[1])
        else:                              # two numbers or nothing given
            self.x = float(x)         # Force to floats
            self.y = float(y)

    def set(self, x=0.0, y=0.0):
        """
        Method to set componets of the vector in various formats.

        :param x: x component or pair of components.
        :type x: float, Vector2d, list[x,y]
        :param y: x component (Default = 0.0)
        :type y: float

        """
        if isinstance(x, Vector2d):    # Vector given
            self.x = x.x
            self.y = x.y
        elif isinstance(x, (list, tuple)):
            self.x = float(x[0])
            self.y = float(x[1])
        else:                              # two numbers or nothing given
            self.x = float(x)         # Force to floats
            self.y = float(y)

    def __str__(self):
        """
        Implement str() to return a string with components in 8.4e format.
        """
        return "({0:8.4e} , {1:8.4e})".format(self.x, self.y)

    def __repr__(self):
        """
        Implments repr() to return a string with full call.
        """
        return "{} ".format(self.__class__.__name__) + str(self)

    def __len__(self):
        """
        Implement len() to return 2

        :return: int
        """
        return 2


    def __getitem__(self, key):
        """
        Implement indexing on read using [i] syntax.
        """
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("Vector2d invalid read index of : {0}".format(key))
    #
    def __setitem__(self,key,value):
        """
        Implement indexing on write using [i] syntax
        """
        if key == 0:
            self.x = float(value)
        elif key == 1:
            self.y = float(value)
        else:
            raise IndexError("Vector2d invalid write index of : {0}".format(key))

    def copy(self):
        """
        Return a copy.

        :return: copy of current Vector2d
        """
        return Vector2d(self)



    def polar(self):
        """
        Return a copy of the current vector in polar (r,theta) as a list.

        :return: list [r,theta]
        """
        r = self.abs()
        theta = math.atan2(self.y,self.x)
        return r,theta

    def rect(self):
        """
        Return a copy of the current vector as a  form assumeing it is in
        polar (r,theta) form.

        Note: there is NO checking, so if the current Vector is NOT in polar form
        you will get rubbish.
        """
        x = self.x*math.cos(self.y)
        y = self.x*math.sin(self.y)
        return Vector2d(x,y)
    #
    #
    def getComplex(self):
        """
        Get copy of vector as a complex.

        :return: a copy of the vector as a `complex`
        """
        return complex(self.x,self.y)
    #
    #
    def absSquare(self):
        """
        Return the absSquare of the vector2d as a float. Does not use pow or \*\*2
        """
        return self.x*self.x + self.y*self.y
    #
    #
    def absCube(self):
        """
        Calcualte absCube of the Vector2d as a float defined as abs(r)^3

        :return: float being absCude.

        """
        r = abs(self)
        return r*r*r

    #
    #
    def abs(self):
        """
        Return abs of vectors2d as a float.
        """
        return math.sqrt(self.absSquare())
    #
    #
    def __abs__(self):
        """
        Implement abs() method for vector2d
        """
        return math.sqrt(self.x*self.x + self.y*self.y)

    #
    #
    def normalise(self):
        """
        Method to normalised vector in place. Will return self so can be used in chain.
        Note: if current vector is abs() = 0, the current vector will be set inValid()

        :return: the current Vector2d normalsied to unity.
        """
        a = self.abs()
        if a != 0.0:      # Vector must be zero
            self /= a
        else:
            self.setInvalid()
        return self
    #
    #
    def setLength(self,d):
        """
        Method to set the length of a vector to specified length. Will return self.
        param d float length vector is set to.

        :param d: the target length
        :type d: float
        :return: the current Vector2d set to specified length.
        """
        a = self.abs()
        if a != 0.0:          # is current length not zero
            self *= (d/a)     # scale by multiply
        return self

    #
    def absNormalised(self):
        """
        Method to return length f vector and normalised vector as a pair

        :return: list [a,n] where a is abs of current Vector2d and n is normalsied Vector2d
        """
        a = self.abs()
        if (a == 0.0):
            return 0.0,Vector2d()
        else:
            n = self / a
            return a,n
    #
    #
    def negate(self):
        """
        Method to negate the current vector in place, will return self to can be used in chain.
        """
        self.x = -self.x
        self.y = -self.y
        return self
    #
    def __neg__(self):
        """
        Method to implement the __neg__ method to return a new -ve vector.
        Note current not changed.
        """
        return Vector2d(-self.x,-self.y)

    #
    #
    def round(self,figs = 0):
        """
        Method to round the current Vector2d to number of decimal figures.
        param figs number of figures to round to (default is 0)
        """
        self.x = round(self.x, figs)
        self.y = round(self.y, figs)
        return self
    #
    def __gt__(self,b):
        """
        Implement abs(self) > abs(b)
        """
        return abs(self) > abs(b)
    #
    def __ge__(self,b):
        """
        Implement abs(self> >= abs(b)
        """
        return abs(self) >= abs(b)
    #
    def __lt__(self,b):
        """
        Implement abd(self) < abs(b)
        """
        return abs(self) < abs(b)
    #
    def __le__(self,b):
        """
        Implement abs(self) <= abs(b)
        """
        return abs(self) <= abs(b)
    #
    #
    def setInvalid(self):
        """
        Method to set to invalid current vector2d to Invalid by setting both compoents
        to float("nan")
        """
        self.x = float("nan")
        self.y = float("nan")
        return self
    #
    #
    def isValid(self):
        """
        Method to deterime if Vector2d is valid, so .x != Nan
        """
        return not math.isnan(self.x)
    #
    #
    def __bool__(self):
        """
        Implment bool for logical test if Valid
        """
        return not math.isnan(self.x)
    #
    #
    def rotate(self,gamma):
        """
        Method to implementate a rotation in place.
        param gamma rotatian angle.
        """
        cos = math.cos(gamma)
        sin = math.sin(gamma)
        x = self.x*cos + self.y*sin
        y = self.y*cos - self.x*sin
        self.set(x,y)      # Set self
        return self
    #
    #
    def __iadd__(self,v):
        """
        Method to implement the += to add Vector2d to current in place, if v is a
        Vectord2d the components will be added, while if it is a float it will be
        added to each component.
        """
        if isinstance(v,Vector2d):
            self.x += v.x
            self.y += v.y
        else:
            self.x += v
            self.y += v
        return self         # Return self

    #
    #
    def __isub__(self,v):
        """
        Method to implement the -= to subtract Vector2d from current in place, if v is a
        Vectord2d the components will be subtrated, while if it is a float it will be
        subrtacted from each component.
        """
        if isinstance(v,Vector2d):
            self.x -= v.x
            self.y -= v.y
        else:               # assume is constant and sub the each element
            self.x -= v
            self.y -= v
        return self         # Return self

    #
    #
    def __imul__(self,v):
        """
        Method to implement the *= to multiply Vector2d by current in place, if v is a
        Vectord3d the component s will be multiplied, while if it is a float it will
        multiply each component.
        """
        if isinstance(v,Vector2d):
            self.x *= v.x
            self.y *= v.y
        else:
            self.x *= v
            self.y *= v
        return self

    #
    #
    def __itruediv__(self,v):
        """
        Method to implement the /= to divide current vector in place, if v is a
        Vectord2d the components will be divided, while if it is a float it will
        divide each component.
        """
        if isinstance(v,Vector2d):
            self.x /= v.x
            self.y /= v.y
        else:
            self.x /= v
            self.y /= v
        return self

    #
    def __add__(self, b):
        """
        Method to implments the c = self + b to add 2 Vector2d, of b is a float it
        will be added to each component.
        return new Vector2d
        """
        if isinstance(b,Vector2d):
            return Vector2d(self.x + b.x, self.y + b.y)
        else:
            return Vector2d(self.x + b , self.y + b)
    #
    #
    def __radd__(self, b):
        """
        Method to implments the c = b + self to add 2 Vector2d, of b is a float it will
        be added to each component.
        return new Vector2d
        """
        if isinstance(b,Vector2d):
            return Vector2d(self.x + b.x, self.y + b.y)
        else:
            return Vector2d(self.x + b , self.y + b)

    #
    #
    def __sub__(self, b):
        """
        Method to implments the c = self - b to add 2 Vector2d, of b is a float it
        will be added to each component.
        return new Vector2d
        """
        if isinstance(b,Vector2d):
            return Vector2d(self.x - b.x, self.y - b.y)
        else:
            return Vector2d(self.x - b , self.y - b)

    #
    #
    def __rsub__(self, b):
        """
        Method to implments the c = b - self to add 2 Vector2d, of b is a float it
        will be added to each component.
        return new Vector2d
        """
        if isinstance(b,Vector2d):
            return Vector2d(b.x - self.x, b.y - self.y)
        else:
            return Vector2d(b - self.x, b - self.y)
    #
    #
    def __mul__(self,b):
        """
        Method to implemnt c = self * b for b being Vector 2d or float, if float it
        is appled to each component.
        returns Vector2d.
        """
        if isinstance(b,Vector2d):
            return Vector2d(self.x * b.x, self.y * b.y)
        else:
            return Vector2d(self.x * b , self.y * b)
    #
    #
    def __rmul__(self,b):
        """
        Method to implemnt c = self * b for b being Vector 2d or float, if float
        it is appled to each component.
        returns Vector2d.
        """
        if isinstance(b,Vector2d):
            return Vector2d(self.x * b.x, self.y * b.y)
        else:
            return Vector2d(self.x * b , self.y * b)
    #
    #
    def __truediv__(self,b):
        """
        Method to implemnt c = self / b for b being Vector 2d or float, if float it
        is appled to each component.
        returns Vector2d.
        """
        if isinstance(b,Vector2d):
            return Vector2d(self.x / b.x, self.y / b.y)
        else:
            return Vector2d(self.x / b , self.y / b)
    #
    #
    def __rdiv__(self,b):
        """
        Method to implemnt c = b / self for b being Vector 2d or float, if float
        it is appled to each component.
        returns Vector2d.
        """
        if isinstance(b,Vector2d):
            return Vector2d(b.x / self.x, b.y / self.y)
        else:
            return Vector2d(b / self.x, b / self.y)
    #
    #
    def dot(self,b):
        """
        Method to get .dot product between current and specified Vector3d
        b second Vector2d
        return float the dot product
        """
        return self.x * b.x + self.y * b.y
    #
    #
    def distanceSquare(self, b):
        """
        Method to get distanceSquare between two Vector2ds Note does NOT use \*\*2 or pow

        :param b: the second Vector2d
        :type b: Vector2d:
        :return: float the square of the distance between vectors.

        """
        dx = b.x - self.x
        dy = b.y - self.y
        return dx*dx + dy*dy
    #
    #
    def distanceCube(self, b):
        """
        Method to get distanceCube between two Vector2ds Note does NOT use \*\*2 or pow
        param b the second Vector2d
        return float the square of the distance between vectors.
        """
        dx = abs(b.x - self.x)
        dy = abs(b.y - self.y)
        return dx*dx*dx + dy*dy*dy
    #
    #
    def distance(self,b):
        """
        Method to get distance between two Vector2ds Note does NOT use \*\*2 or pow

        :param b: the second Vector2d
        :type b: Vector2d
        :return: float the square of the distance between vectors.

        """
        return math.sqrt(self.distanceSquare(b))
    #
    #
    def errorSquare(self,b):
        """
        Method to set the normalsied square error between two vectors
        """
        a = self.absSquare()
        b = b.absSquare()
        ds = self.distanceSquare(b)
        n = a*b                    # Normalisation
        if n != 0.0:
            return ds/math.sqrt(n)
        elif a != 0.0:
            return ds/math.sqrt(a)
        elif b != 0.0:
            return ds/math.sqrt(b)
        else:
            return ds             # which must be zero
    #
    #
    def angleBetween(self,b):
        """
        Method to get the angle between two Vector2d
        param b second Vector2d
        param return float, angle in range -pi/2 and pi
        Note: is abs(current) and abs(b) is zero, zero is retunned
        """
        s = abs(self)*abs(b)
        if s == 0.0:
            return 0.0
        else:
            cq = self.dot(b)/s
            return math.acos(cq)
    #
    #     Method to get the area between two Vectors3d
    #     b second Vector3d
    #     return float, area defined by triangle formed by the two vectors
    #def areaBetween(self,b):
    #    v = self.cross(b)
    #    return 0.5*abs(v)
    #
    def inverseSquare(self,b, c = 1.0):
        """
        Method to get the vector from current to b scaled to inverse square of
        the distance between them, for implementation of inverse square law forces.
        """
        v = b - self
        s = c/v.absCube()
        v *= s
        return v
#
#
class Vector3d(object):
    """
    Class to implement three dimensional vectors.

    :param x: x component, Vector3d r of a list of floats. (default = 0.0)
    :type x: float or Vector3d or list or tuple
    :param y: y component (default = 0.0)
    :type y: float
    :param z: z component (default = 0.0)
    :type z: float

    If x is a Vector3d or list/tuple then the contents of the y and z parameters
    will not be accessed.

    """
    #
    #
    def __init__(self,x = 0.0, y = 0.0, z = 0.0):
        if isinstance(x,Vector3d):    # Vector given
            self.x = x.x
            self.y = x.y
            self.z = x.z
        elif isinstance(x,(list,tuple)):
            self.x = float(x[0])
            self.y = float(x[1])
            self.z = float(x[2])
        else:                              # three numbers or nothing given
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)



    def set(self,x = 0.0 , y = 0.0, z = 0.0):
        """
        Method to set vector with various augument types.

        :param x:  x component, Vector3d r of a list of floats. (default = 0.0)
        :type x: float or Vector3d or list or tuple
        :param y: y component (default = 0.0)
        :type y: float
        :param z: z component (default = 0.0)
        :type z: float

        """
        if isinstance(x,Vector3d):    # Vector given
            self.x = x.x
            self.y = x.y
            self.z = x.z
        elif isinstance(x,(list,tuple)):
            self.x = float(x[0])
            self.y = float(x[1])
            self.z = float(x[2])
        else:                              # three numbers or nothing given
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)

        return self

    #
    def __str__(self):
        """
        Implement str() with components formatted with 8.4e
        """
        return "({0:8.4e} , {1:8.4e}, {2:8.4e})".format(self.x,self.y,self.z)
    #
    def __repr__(self):
        """
        Impment repr() with class name and components formatted with 8.4e
        """
        return "{}: ".format(self.__class__.__name__) + str(self)
    #
    #
    def __len__(self):
        """
        Get len() defined at 3
        """
        return 3
    #
    #
    def __getitem__(self,key):
        """
        Implement indexing on read in [i] syntax.
        """
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        else:
            raise IndexError("Vector3d invalid read index of : {0:d}".format(key))
    #
    #
    def __setitem__(self,key,value):
        """
        Implement indexing on write in s[i] syntax.
        """
        if key == 0:
            self.x = float(value)
        elif key == 1:
            self.y = float(value)
        elif key == 2:
            self.z = float(value)
        else:
            raise IndexError("Vector3d invalid write index of : {0:d}".format(key))
    #
    #
    def copy(self):
        """
        Return a copy of the current Vector3d.

        :return: deep copy current Vector3d

        """
        return Vector3d(self)
    #
    #
    def polar(self):
        """
        Return a thecurrent vector in polar form as a list.

        :return: value of current Vector3d as a [r,theta,psi] as a list

        """
        r = abs(self)
        if r != 0.0 :
            theta = math.acos(self.z/r)
            psi = math.atan2(self.x,self.y)
            return r,theta,psi
        else:
            return 0.0,0.0,0.0

    def polarDegrees(self):
        """
        Return the currennt vector in polar forms with angle in degrees.

        :return: list of [r,theta,psi] in degrees
        """
        r, theta, psi = self.polar()
        return r, math.degrees(theta), math.degrees(psi)

    def setPolar(self,r = 0.0, theta = 0.0, psi = 0.0):
        """
        Set the current vector using r,theta,psi format

        :param r: r component (Default = 0.0)
        :type r: float
        :param theta: theta component (angle from z axis) (Default = 0.0)
        :type theta: float
        :param psi: psi component (angle from x axis) (Default = 0.0)
        :type psi: float

        """
        sinTheta = math.sin(theta)
        self.x = r*sinTheta*math.sin(psi)
        self.y = r*sinTheta*math.cos(psi)
        self.z = r*math.cos(theta)
        return self;

    def setPolarDegrees(self,r = 0.0, theta = 0.0, psi = 0.0):
        """
        Set the current vector using r,theta,psi format in degrees

        :param r: r component (Default = 0.0)
        :type r: float
        :param theta: theta component (angle from z axis) (Default = 0.0)
        :type theta: float
        :param psi: psi component (angle from x axis) (Default = 0.0)
        :type psi: float

        """
        return self.setPolar(r,math.radians(theta),math.radians(psi))


    def unitPair(self):
        """
        Get the abs() and Unit3d() of current Vector3d as a list.

        :return: [abs(self),Unit3d(self)]

        """
        return abs(self),Unit3d(self)

    #
    #
    def absSquare(self):
        """
        Get absSquare of the vector3d as a float. Note does NOT use pow or \*\*2

        :return: abssquared of vector

        """
        return self.x*self.x + self.y*self.y + self.z*self.z


    def absCube(self):
        """
        Get the absCube of the Vector3d as a float defined abs(r)^3

        :return: the cube of the absolute values as a float.

        """
        r = abs(self)
        return r*r*r


    def __abs__(self):
        """
        Implement abs() to return the abs length of Vector3d as a float.
        """
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def normalise(self):
        """
        Method to normalised vector in place.

        Note: if abs() = 0, the current vector will be set inValid()
        """
        a = abs(self)
        if a != 0.0:      # Vector must be zero
            self /= a
        else:
            self.setInvalid()
        return self


    def setLength(self,d):
        """
        Method to set the length (or abs) of the current vector to specified length
        by scaling.
        param d float length vector is set to.
        """
        a = self.abs()
        if a != 0.0:          # is current length not zero
            self *= (d/a)     # scale by multiply
        return self
    #
    #
    def absNormalised(self):
        """
        Method to return abs() and normalsied copy of current vector as a
        list pair (current vector not changed)
        return [a,n] where a abs() and n is normalsied Vector3d
        """
        a = self.abs()
        if (a == 0.0):
            return 0.0,Vector3d()
        else:
            n = self / a
            return a,n
    #
    #
    def negate(self):
        """
        Method to negate the current vector in place.
        """
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z
        return self
    #
    def __neg__(self):
        """
        Implement the __neg__ method to return a new vector being the -ve of the current.
        Note current not changed.
        """
        return Vector3d(-self.x,-self.y,-self.z)

    #
    #
    def round(self,figs = 0):
        """
        Method to round the current Vector2d to number of decimal figures.
        param figs number of figures to round to (default is 0)
        """
        self.x = round(self.x, figs)
        self.y = round(self.y, figs)
        self.z = round(self.z, figs)
        return self
    #
    #
    def __gt__(self,b):
        """
        Implement > to compare abs() of each vectors
        """
        return abs(self) > abs(b)
    #
    #
    def __ge__(self,b):
        """
        Implement >= to compare abs() of each vector
        """
        return abs(self) >= abs(b)
    #
    #
    def __lt__(self,b):
        """
        Implement < to compare abs() of each vector.
        """
        return abs(self) < abs(b)
    #
    #
    def __le__(self,b):
        """
        Implement <= to compare abs() of each vector.
        """
        return abs(self) <= abs(b)

    #
    #
    def setInvalid(self):
        """
        Method to set current vector3d to Invalid by setting all three
        compoents to float("nan").
        """
        self.x = float("nan")
        self.y = float("nan")
        self.z = float("nan")
        return self

    def random(self,mag = 1.0):
        """
        Set current vetor3d to random within a sphere of specified magnitude
        param mag (float) the specified magnitude, defaults to 1.0
        """
        magSqr = mag*mag
        while True:              # Set random point
            self.x = uniform(-mag,mag)
            self.y = uniform,(-mag,mag)
            self.z = uniform(-mag,mag)
            if self.absSquare() <= magSqr:   # Test if it within sphere, else try again
                break

        return self
    #
    #
    def isValid(self):
        """
        Method to test if vector is Valid

        :return: bool True for Valid, else False

        """
        return not math.isnan(self.x)
    #
    def __bool__(self):
        """
        Implement the logical bool test if a vector is valid. True is self.n != Nan
        """
        return not math.isnan(self.x)
    #
    #
    def rotateAboutX(self,alpha):
        """
        Method to implementate rotation about x axis in place.
        param alpha rotatian about x axis in radians
        """
        cos = math.cos(alpha)
        sin = math.sin(alpha)
        y = self.y*cos + self.z*sin
        z = self.z*cos - self.y*sin
        self.y = y                      # Overwrite y
        self.z = z                      # Overwrite z
        return self
    #
    #
    def rotateAboutY(self,beta):
        """
        Method to implementate a rotation about y axis in place.
        param beta rotatian about y axis in radians.
        """
        cos = math.cos(beta)
        sin = math.sin(beta)
        x = self.x*cos - self.z*sin
        z = self.x*sin + self.z*cos
        self.x = x                      # Overwrite x
        self.z = z                      # Overwrite z
        return self
    #
    #
    def rotateAboutZ(self,gamma):
        """
        Method to implementate a rotation about z axis in place.
        param gamma rotatian about z axis in radians.
        """
        cos = math.cos(gamma)
        sin = math.sin(gamma)
        x = self.x*cos + self.y*sin
        y = self.y*cos - self.x*sin
        self.x = x                      # Overwrite x
        self.y = y                      # Overwrite y
        return self
    #
    #       General Rotate about x , y, z. The rotation order is x,y then z
    #       alpha rotation ablut x axis
    #       beta rotation about y axis
    #       gamma rotation about z axis
    #
    def rotate(self,alpha,beta,gamma):
        """
        Method to implmeent general Rotate about x , y, z in place.
        The rotation order is x,y then z.
        param alpha rotation about x axis in radians
        param beta rotation about y axis in radians
        param gamma rotation about z axis in radians
        """
        self.rotateAboutX(alpha)
        self.rotateAboutY(beta)
        self.rotateAboutZ(gamma)
        return self
    #
    #
    def __iadd__(self,v):
        """
        Method to implement the += to add Vector3d to current in place, if v is a
        Vectord3d the components will be added, while if it is a float it will be
        added to each component.
        """
        if isinstance(v,Vector3d):
            self.x += v.x
            self.y += v.y
            self.z += v.z
        else:               # assume is constant and add the each element
            self.x += v
            self.y += v
            self.z += v
        return self         # Return self

    #
    #
    def __isub__(self,v):
        """
        Method to implement the -= to subtract Vector3d from current in place, if v is
        a Vectord3d the components will be subtrated, while if it is a float it will
        be subrtacted from each component.
        """
        if isinstance(v,Vector3d):
            self.x -= v.x
            self.y -= v.y
            self.z -= v.z
        else:               # assume is constant and sub the each element
            self.x -= v
            self.y -= v
            self.z -= v
        return self         # Return self

    #
    #
    def __imul__(self,v):
        """
        Method to implement the *= to multiply Vector3d by current in place, if v is a
        Vectord3d the components will be multiplied, while if it is a float it will
        multiply each component.
        """
        if isinstance(v,Vector3d):
            self.x *= v.x
            self.y *= v.y
            self.z *= v.z
        else:
            self.x *= v
            self.y *= v
            self.z *= v
        return self

    #
    #
    def __itruediv__(self,v):
        """
        Method to implement the /= to divide current vector in place, if v is a
        Vectord3d the components will be devided, while if it is a float it will
        divide each component.
        """
        if isinstance(v,Vector3d):
            self.x /= v.x
            self.y /= v.y
            self.z /= v.z
        else:
            self.x /= v
            self.y /= v
            self.z /= v
        return self
    #
    #
    def __add__(self, b):
        """
        Implement c = self + b for Vector3d, if b is float, then it will be added to
        each component.
        returns new Vector3d
        """
        if isinstance(b,Vector3d):
            return Vector3d(self.x + b.x, self.y + b.y, self.z + b.z)
        else:
            return Vector3d(self.x + b , self.y + b, self.z + b)
    #
    #
    def __radd__(self, b):
        """
        Impement c = b + self for b not a Vector3d, (typically a float)
        returns new Vector3d
        """
        if isinstance(b,Vector3d):
            return Vector3d(self.x + b.x, self.y + b.y, self.z + b.z)
        else:
            return Vector3d(self.x + b , self.y + b, self.z + b)

    #
    #
    def __sub__(self, b):
        """
        Implement c = self - b for Vector3d, if b is float it will be subtracted
        from each element.
        returns new Vector3d
        """
        if isinstance(b,Vector3d):
            return Vector3d(self.x - b.x, self.y - b.y, self.z - b.z)
        else:
            return Vector3d(self.x - b , self.y - b, self.z - b)
    #
    #
    def __rsub__(self, b):
        """
        Implement c = b - self for Vector3d, if b is float it will be subtracted
        from each element.
        returns new Vector3d
        """
        if isinstance(b,Vector3d):
            return Vector3d(b.x - self.x, b.y - self.y, b.z - self.z)
        else:
            return Vector3d(b - self.x , b - self.y, b - self.z)
    #
    #
    def __mul__(self,b):
        """
        Implement c = self * b for Vectors3d, if b is float it will multiply each element.
        return new Vector3d
        """
        if isinstance(b,Vector3d):
            return Vector3d(self.x * b.x, self.y * b.y, self.z * b.z)
        else:
            b = float(b)
            return Vector3d(self.x * b , self.y * b, self.z * b)
    #
    #
    def __rmul__(self,b):
        """
        Implement c = b * self for Vector3d, if b is float it will multiply each element.
        """
        if isinstance(b,Vector3d):
            return Vector3d(self.x * b.x, self.y * b.y, self.z * b.z)
        else:
            b = float(b)
            return Vector3d(self.x * b , self.y * b, self.z * b)
    #
    #
    def __truediv__(self,b):
        """
        Implement c = self / b for Vector3d, if b is float it will divide each element
        """
        if isinstance(b,Vector3d):
            return Vector3d(self.x / b.x, self.y / b.y, self.z / b.z)
        else:
            return Vector3d(self.x / b , self.y / b, self.z / b)
    #
    #
    def __rtruediv__(self,b):
        """
        Implement c = b / self for Vector3d, if b is float it will divide each element
        """
        if isinstance(b,Vector3d):
            return Vector3d(b.x / self.x, b.y / self.y , b.z / self.z )
        else:
            return Vector3d(b / self.x, b / self.y, b / self.z )


    def propagate(self,d,u):
        """
        Return a new vectors that is self + d*u.
        Added for efficency in optical calcualations.

        :param d: distance
        :type d: float
        :param u: direction
        :type: Unit3d
        :return: new Vector3d

        """
        return Vector3d(self.x + d*u.x , self.y + d*u.y, self.z + d*u.z)

    def dot(self,b):
        """
        Method to form the .dot product of self . b
        returns float the dot product.

        :param b: the other Vector3d
        :type b: Vector3d
        :return: dot product as a float.
        """
        return self.x * b.x + self.y * b.y + self.z * b.z


    def cross(self,b):
        """
        Method to form the cross product c = self x b
        return Vector3d the cross product
        """
        tx = self.y*b.z - self.z*b.y
        ty = self.z*b.x - self.x*b.z
        tz = self.x*b.y - self.y*b.x
        return Vector3d(tx,ty,tz)



    def distanceSquare(self, b):
        """
        Method to get distanceSquare between two Vector3d, Note does NOT use \*\*2 or pow.

        :param b: the second Vector3d
        :type b: Vecftor3d
        :return: float the square of the distance between vectors

        """
        dx = b.x - self.x
        dy = b.y - self.y
        dz = b.z - self.z
        return dx*dx + dy*dy + dz*dz
    #
    #
    def distanceCube(self, b):
        """
        Method to get distanceCube between two Vector3d.
        Note does NOT use \*\*2 or pow.

        :param b: the second Vector3d
        :type b: Vector3d:
        :return: float the cube of the distance between vectors.

        """
        dx = abs(b.x - self.x)
        dy = abs(b.y - self.y)
        dz = abs(b.z - self.z)
        return dx*dx*dx + dy*dy*dy + dz*dz*dz
    #
    #
    def distance(self,b):
        """
        Method to det the distance between two Vector3d.

        :param b: second Vector3d
        :type b: Vector3d
        :return: float distance between two vectors.
        """
        return math.sqrt(self.distanceSquare(b))
    #
    #
    def errorSquare(self,b):
        """
        Method to get the normalsied square error between two Vector3d

        :param b: Vector3d, the second vector
        :return: float the normalsied square error
        """
        a = self.absSquare()
        b = b.absSquare()
        ds = self.distanceSquare(b)     # square distance
        n = a*b                         # Normalisation
        if n != 0.0:
            return ds/math.sqrt(n)
        elif a != 0.0:
            return ds/math.sqrt(a)
        elif b != 0.0:
            return ds/math.sqrt(b)
        else:
            return ds             # which must be zero
    #
    #
    def angleBetween(self,b):
        """
        Method to get the angle between two Vector3d

        :param b: second Vector3d
        :type b: Vector3d
        :return: float, angle in range -pi/2 and pi/2

        Note: is abs(current) and abs(b) is zero, zero is returned.
        """
        s = abs(self)*abs(b)
        if s == 0.0:
            return 0.0
        else:
            cq = self.dot(b)/s
            return math.acos(cq)
    #
    #
    def areaBetween(self,b):
        """
        Method to get the area between two Vectors3d defined by a = 0.5 * abs (self x b)

        :param b: second Vector3d
        :type b: Vector3d
        :return: float area defined by triangle formed by the two vectors
        """
        v = self.cross(b)
        return 0.5*abs(v)
    #
    #
    def inverseSquare(self,b,c = 1.0):
        """
        Method to get the Vector3d from current to Vector3d by scaled by inverse square of
        the distance between them, for implementation of inverse square law forces.
        Formula implemented is        v = c\*(b - self) \|b - self \|^3

        :param b: the second vector
        :type b: Vector3d
        :param c: scaling factor, (Defaults to 1.0)
        :type c: float
        :return: the scaled Vector3d
        """
        v = b - self
        s = c/v.absCube()
        v *= s
        return v
#
#


#
class Unit3d(Vector3d):
    """
    Class to hold a unit Vector3d, it extends Vector3d with automormalsiation on creation and extra  methods
    to support optical ray calcualtions.

    :param x: x componen, Angle, list[]  (default = 0.0)
    :param y: the y component (default = 0.0)
    :param z: the z component (default = 0.0)

    If parameter is NOT a Unit3d or Angle it is automatically normalsied to unit.
    Note if (0,0,0) or () suppled, the Unit3d will be set to inValid.

    """

    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        """
        Constructor to create and set Unit3d.

        """
        if isinstance(x,Angle):          # Angle passed
            st = math.sin(x.theta)
            xl = st*math.sin(x.psi)
            yl = st*math.cos(x.psi)
            zl = math.cos(x.theta)
            Vector3d.__init__(self,xl,yl,zl)

        elif isinstance(x,Unit3d):       #  Unit3d passed, just copy
            Vector3d.__init__(self,x)

        else:                                 # Pass to Vector3d to deal with the others
            Vector3d.__init__(self, x, y, z)
            self.normalise()                  # Force normalisation


    def set(self,x = 0.0, y = 0.0, z = 0.0):
        """
        Method to actually set the Unit 3d
        """

        if isinstance(x,Angle):          # Angle passed
            st = math.sin(x.theta)
            xl = st*math.sin(x.psi)
            yl = st*math.cos(x.psi)
            zl = math.cos(x.theta)
            Vector3d.set(self,xl,yl,zl)

        elif isinstance(x,Unit3d):       #  Unit3d passed, just copy
            Vector3d.set(self,x)

        else:                                 # Pass to Vector3d to deal with the others
            Vector3d.set(self, x, y, z)
            self.normalise()                  # Force normalisation


        return self



    def parseAngle(self,*args):
        """
        Method to parse angle set Unit3d and return it. This accepts a much more
        extensive set of angle defintions, so basically anything that cen be interepeted
        as an "angle". So Unit3d, Angle, Vector3d, listir tuple if (x,y,z), list or tuple
        of (theta,psi). Angle is float for radians and str() for degrees.

        :param args: brtween 1 and 3 args.

        Note: this method is rather compuationally slow, it is design to
        parsse command inputs rather than bening used in calcualtions.
        """

        if len(args) == 0:       # No args sent
            return self.setInvalid()

        if len(args) == 1:       # 1 argument
            fa = args[0]         # Deal with one arg of

            if isinstance(fa,(Unit3d,Vector3d,Angle)):
                return self.set(fa)

            elif isinstance(fa,(list,tuple)):  # list or tuple
                if len(fa) ==  3:
                    return self.set(fa)          # x,y,z as list
                elif len(fa) == 2:
                    theta,psi = fa
                    if isinstance(theta, str):
                        theta = math.radians(float(theta))
                    if isinstance(psi, str):
                        psi = math.radians(float(psi))
                    return self.set(Angle(theta,psi))   # theta,psi as list
                else:
                    theta = fa[0]
                    if isinstance(theta,str):
                        theta = math.radians(float(theta))
                    return self.set(Angle(theta)) # theta only

            elif isinstance(fa,(float,int)):
                return self.set(Angle(fa))

            elif isinstance(fa,str):
                fa = math.radians(float(fa))
                return self.set(Angle(fa))
            else:
                return self.setInvalid() # Rubbish sent,

        if len(args) == 2:       # Two args so must be angle
            theta = args[0]
            psi = args[1]

            if isinstance(theta,str):               # If str convert degrees to radians
                theta = math.radians(float(theta))
            if isinstance(psi,str):
                psi = math.radians(float(psi))
            return self.set(Angle(theta,psi))         # Return required
        else:

            return self.set(*args)                    # Pass 3 args to Unit3()




    def copy(self):
        """
        Return copy of current Unit3d.
        """
        return Unit3d(self)


    def random(self):
        """
        Set the current Unit3d random a random point in a three-dimensional unit sphere.

        :return: self
        """
        u = Unit3d(Angle().random())         # get random Unit3d
        self.set(u)
        return self

    def setPolar(self, theta = 0.0, psi = 0.0):
        """
        Set the current unit3d  using theta,psi format

        :param theta: theta angle in radians
        :type theta: float
        :param psi: the psi angle in radians
        :type psi: float
        """
        sinTheta = math.sin(theta)
        self.x = sinTheta*math.sin(psi)
        self.y = sinTheta*math.cos(psi)
        self.z = math.cos(theta)
        return self

    def setPolarDegrees(self, theta = 0.0, psi = 0.0):
        """
        Set the current unit3d  using theta,psi format in degrees

        :param theta: theta component (angle from z axis) (Default = 0.0)
        :type theta: float
        :param psi: psi component (angle from x axis) (Default = 0.0)
        :type psi: float
        """
        return self.setPolar(math.radians(theta),math.radians(psi))


    def getAngle(self):
        """
        Method to get the current Unit3d as an Angle
        """
        return Angle(self)



    def reflection(self,n):
        """
        Method to refect current Unit3d from a surface specified by its surface normal.

        :param n: the surface normal.
        :type n: Unit3d
        :return: True of all isValid()

        """
        self -= 2.0*self.dot(n)*n
        return self.isValid()

    #
    #
    def refraction(self, n, ratio):
        """
        Method to refract the current Unit3d through a suface with surface
        specified by its surface normal.

        :param n: the surface normal of the surface.
        :type n: Unit3d
        :param ratio: the ration of refractice index at the boundary.
        :type ratio: float
        :return: True, if all successful, False if fails. current will be set inValid is n is inValid  but NOT if failure is due to exceeding critical angle.

        """
        #              Check for validity
        if (not self) or (not n) or math.isnan(ratio) :
            self.setIvalid()
            return False

        if ratio == 1.0:       # Nothing to do,
            return True
        else:
            a = 1.0/ratio
            b = self.dot(n)
            c = 1.0 - a*a*(1.0 - b*b)

            if c < 0:
                return False   #   Above critical
            else:
                c = math.copysign(math.sqrt(c),b)
                d = c - a*b
                self.x = self.x*a + n.x*d
                self.y = self.y*a + n.y*d
                self.z = self.z*a + n.z*d
                return True    # Success
#
#
class Angle(object):
    """
    Class Angle to hold a angle in theta / phi format. theta is angle wrt z-axis and psi is
    rotation angle wrt y-axis.

    :param theta: the theta angle wrt to z-axis in radians (default = 0.0)
    :type theta: float or Angle
    :param psi: the psi angle wrt to y-axis in radians (default = 0.0)
    :type psi: float

    Note all angles in radians.
    """

    def __init__(self,theta = 0.0,psi = 0.0):
        """
        Constructor to set two angles

        """

        if isinstance(theta,Angle):                # Deal with Angle
            self.theta = theta.theta
            self.psi = theta.psi

        elif isinstance(theta,Vector3d):          # Deal with Vector3d or Unit3d
            r = abs(theta)
            if r != 0.0 :
                self.theta = math.acos(theta.z/r)
                self.psi = math.atan2(theta.x , theta.y)
            else:
                self.theta = 0.0
                self.psi = 0.0

        elif isinstance(theta,(list,tuple)):  # Deal with list or truple
            self.theta = float(theta[0])
            self.psi = float(theta[1])

        else:                                          # Finally two floats
            self.theta = float(theta)
            self.psi = float(psi)
    #
    #
    def __str__(self):
        """
        Implement the str() method to format theta and psi with 8.4e format.
        """
        return "({0:8.5e}, {1:8.5e})".format(self.theta,self.psi)
    #
    #
    def __repr__(self):
        """
        Implement the repr() method to format Angle with 8.4e fomat and class name.
        """
        return "{}: ".format(self.__class__.__name__) + str(self)


    def copy(self):
        """
        Return a copy if current Angle()
        """
        return Angle(self)

    def setInvalid(self):
        """
        Method to set current Angle to Invalid by setting all theta and psi to float("nan").
        """
        self.theta= float("nan")
        self.psi = float("nan")
        return self

    def isValid(self):
        """
        Method to test if Angle is Valid

        :return: bool True for Valid, else False

        """
        return not math.isnan(self.theta)

    def __bool__(self):
        """
        Implement the logical bool test if a Angle is valid. True is self.n != Nan
        """
        return not math.isnan(self.theta)



    def setDegrees(self,theta = 0.0, psi = 0.0):
        """
        Set the Angle in degrees
        param theta, theta angle or list/truple of length 2
        param psi, psi
        """
        if isinstance(theta,list) or isinstance(theta,tuple):
            self.theta = math.radians(theta[0])
            self.psi = math.radians(theta[1])
        else:             # Flaots given
            self.theta = math.radians(theta)
            self.psi = math.radians(psi)
        return self


    def getDegrees(self):
        """
        Get the angle as a tuple of flaots in degrees.
        """
        return math.degrees(self.theta) , math.degrees(self.psi)

    def getUnit3d(self):
        """
        Get the equivalient Unit3d
        """
        return Unit3d(self)

    def random(self):
        """
        Set the current angle to random with theta in range 0 -> pi and psi is range 0 - 2pi
        """
        self.theta = uniform(0.0,math.pi)
        self.psi = uniform(0,2.0*math.pi)
        return self

#
class Axis3d(object):
    """
     Axis3d class that define a coordinate axis system with origin and axis vectors
    """
    #
    #
    def __init__(self,origin = Vector3d(), u1_or_axis = Unit3d(1,0,0), \
                 u2 = Unit3d(0,1,0), u3 = Unit3d(0,0,1)):
        """
        Constructor for Axis3d
        param origin Vector3d the axis origin (defaults to (0,0,0))
        param u1_or_axis the u1 Unit3d vector, (defaults to (1,0,0))
        param u2 Unit3d u2 unit vector (defaults to (0,1,))
        param u3 Unit3d u3 unit vectors (defaults to (0,0,1)
        OR
        u1_or_axis list[] of three vectors

        Note:      supplied u_i vectors will be automatically normalsied
        """
        self.origin = Vector3d(origin)
        self.axis = []
        if (isinstance(u1_or_axis,list)):    # Axis supplied as a list.
            for a in u1_or_axis:
                self.axis.append(Unit3d(a))
        else:                                # Supplied at 3 vectors
            self.axis.append(Unit3d(u1_or_axis))
            self.axis.append(Unit3d(u2))
            self.axis.append(Unit3d(u3))
    #
    #
    def __repr__(self):
        """
        Implement the repr() method to show state of axis"
        """
        return "Axis: Orgin at : {0:s}\n{1:s}\n{2:s}\n{3:s}".\
        format(self.origin,self.axis[0],self.axis[1],self.axis[2])

    #
    #
    def transform(self,vec):
        """
        Method to transform a Vectors3d into this axis
        param vec Vector3d to be transformned
        return new Vector3d in the new axis
        """

        if isinstance(vec,Unit3d):
            x = vec.dot(self.axis[0])   # x component
            y = vec.dot(self.axis[1])   # y component
            z = vec.dot(self.axis[2])   # z component
            return Unit3d(x,y,z)
        else:
            v = vec - self.origin     # Shift the origin first
            x = v.dot(self.axis[0])   # x component
            y = v.dot(self.axis[1])   # y component
            z = v.dot(self.axis[2])   # z component
            return Vector3d(x,y,z)




