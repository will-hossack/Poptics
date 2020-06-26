"""
   Set of classes to analyse geometric PSF and produce spot diagrams.

"""
from poptics.wavelength import WavelengthColour,getDefaultWavelength
from poptics.surface import OpticalPlane
from poptics.vector import Vector2d,Vector3d
from matplotlib.pyplot import plot, scatter, axis, figure, axes, xlabel
from matplotlib.animation import FuncAnimation
import math


#                          So
ReferencePointOption = 0

def getReferencePointOption():
    """
    Get the current global reference point, mainly used for Gui interfacwe

    :return: the
    """
    return ReferencePointOption


def setReferencePointOption(opt = 0):
    """
    Set the global Reference Point Option

    :param opt: the reference point option. (0/1/2 only)
    :type opt: int
    """
    global ReferencePointOption
    ReferencePointOption = opt


PlaneShift = 0.0

def getPlaneShift():
    """
    Get the plane shift, mainly used buy GUI to moce the plane location on SpotDiagrams

    :return: the current plane shift as a float
    """
    return PlaneShift

def setPlaneShift(shift = 0.0):
    """
    Set the plane shift, mainly used by GUI

    :param shift: the plane shift (Default = 0.0), which resets the shift
    :type shift: float
    """
    global PlaneShift
    PlaneShift = shift

def incrementPlaneShift(delta):
    """
    Increment the plane shift by Delta

    :param delta: distance to increment the currennt plane shift
    :type delta: float
    """
    global PlaneShift
    PlaneShift += delta



class Moments(object):
    """
    Class to implment two dimensional moments
    """

    def __init__(self,order = 2):
        """
        Constructor with order only, defaults to 2
        """
        self.order = order
        self.xdim = order + 1
        #self.moment = array.array('d',[0.0]*(self.__index(0,order) + 1))
        self.moment = array.array('d',[0.0]*(self.xdim*self.xdim))
        self.points = 0


    #
    def get(self,m,n):
        """
        Method to get a momment value
        """
        #    return self.moment[self.__index(m,n)]
        return self.moment[m*self.xdim + n]

    #
    def addPoint(self,p,value):
        """
        Method to add a point
        """
        self.points += 1
        for k in range(0,self.order + 1):
            for n in range(0,k + 1):
                m = k - n
                # i = self.__index(m,n)
                v = value*math.pow(p.x,m)*math.pow(p.y,n)
                self.moment[m*self.xdim + n] += v
        return self

    #
    def addRay(self,ray,plane):
        """
        Method add ray or raypencil in speficied place
        """
        if isinstance(ray,list): # If list add all the valid rays
            for r in ray:
                if r:
                    self.addRay(r,plane)
        else:
            if ray:
                v = ray.pointInPlane(plane)
                self.addPoint(v,ray.intensity)
        return self


    #
    def centroid(self):
        m = self.get(0,0)
        return Vector2d(self.get(1,0)/m,self.get(0,1)/m)

    def radius(self):
        c = self.centroid()
        m = self.get(0,0)
        r = (self.get(2,0) + self.get(0,2))/m - c.absSquare()
        return r


    def __index(self,m,n):
        """
        Internal method to look up moments in list
        """
        ord = m + n
        return (ord*(ord + 1)/2 + n)


class FixedMoments(object):
    """
    Class to implment two dimensional moments to second order only.

    :param: pts list of points
    :type pts: list of Vector2d

    """
    def __init__(self,pts = None):
        """
        Constructor with order only, defaults to 2
        """
        self.m00 = 0.0
        self.m10 = 0.0
        self.m01 = 0.0
        self.m20 = 0.0
        self.m11 = 0.0
        self.m02 = 0.0
        self.points = 0

        #                    Add points is supplied
        if pts != None:
            for p in pts:
                self.addPoint(p)



    def addPoint(self,p,value = 1.0):
        """
        Method to add a point to moments.

        :param p: the point as Vector2d
        :type p: Vector2d
        :param value: value at the point (Default = 1.0)
        :type value: float
        """
        self.points += 1
        self.m00 += value
        self.m10 += value*p.x
        self.m01 += value*p.y
        self.m20 += value*p.x*p.x
        self.m11 += value*p.x*p.y
        self.m02 += value*p.y*p.y
        return self


    def centroid(self):
        """
        Get the centriod of the moments as a Vector2d.

        :return: centroid as a Vector2d

        """
        return Vector2d(self.m10/self.m00,self.m01/self.m00)

    def radius(self):
        """
        Get the the average radius of the momnnt distribution.

        :return: the radius as a float

        """
        c = self.centroid()
        r = (self.m20 + self.m02)/self.m00 - c.absSquare()
        return math.sqrt(r)

    def ellipse(self):
        """
        Calcualte the best fitting ellipse as a list. This assume the
        disstibution is symmetric about the centriod.

        :return: [major,minor,alpha] as a list of floats.

        """
        c = self.centroid()
        # Calcualte the central moments about centriod.
        u20 = self.m20/self.m00 - c.x*c.x
        u02 = self.m02/self.m00 - c.y*c.y
        u11 = self.m11/self.m00 - c.x*c.y

        # Form the ellipse parameters
        p = u20 + u02
        q = math.sqrt(4.0*u11*u11 + (u20 - u02)**2)
        major = math.sqrt(p + q)
        minor = math.sqrt(p - q)
        alpha = 0.5*math.atan2(2.0*u11 , (u20 - u02))

        return major,minor,alpha


    def area(self):
        """
        Cacualte the area (assuming it is an ellipse)

        :return: the area as a float

        """
        major,minor,alpha = self.ellipse()
        return math.pi*major*minor

    def eccentricity(self):
        """
        Eccenricity of the ellipse

        :return: the eccentricity as float

        """
        major,minor,alpha = self.ellipse()
        return math.sqrt(1.0 - (minor*minor)/(major*major))



class Psf(Vector3d):
    """
    Class to represent a geometric Psf as the best fitting ellipse. There area also methods to allow
    this to be calcualted from a RayPencil in a specified OpticalPlane.

    :param pos: centre of PSF (Default = (0,0,0))
    :type pos: Vector3d or float
    :param intensity: the intensity (Default = 1.0)
    :type intensity: float
    :param major: major axis of ellipse (Default = 1.0)
    :type major: float
    :param minor: minor axis of ellipse (Default = None), major values used
    :type minor:
    :param alpha: angle of ellipse (Default = 0.0)
    :type alpha: float
    :param wave: the wavelength, Default = None (gives the package default)

    """

    def __init__(self,pos = 0.0 , intensity = 1.0, major = 1.0, minor = None, alpha = 0.0, wavelength = None):
        """
        Constructor
        """

        if isinstance(pos,float):
            Vector3d.__init__(self,[0.0,0.0,pos])
        else:
            Vector3d.__init__(self,pos)
        self.intensity = 1.0
        self.major = major
        if minor == None:
            self.minor = self.major
        else:
            self.minor = minor
        self.alpha = alpha
        self.wavelength = getDefaultWavelength(wavelength)

    def __str__(self):
        """
        Implement str
        """
        return " {0:s} i: {1:7.4f} major: {2:7.4f} minor: {3:7.4f} alpha: {4:7.4f}".\
            format(Vector3d.__str__(self),self.intensity,self.major,self.minor,self.alpha)


    def eccentricity(self):
        """
        Get the Eccentricity of the ellipse.

        :return: eccentricity of ellipse as a float.
        """

        return math.sqrt(1.0 - (self.minor*self.minor)/(self.major*self.major))

    def area(self):
        """
        Area of PSF from elipse parameters.

        :return: area as float
        """
        return math.pi*self.major*self.minor


    def ellipse(self):
        """
        Get the ellipse parameters as a list [major,minor,alpha]

        :return: [major,minor,alpha] as list of floats.
        """
        return self.major,self.minor,self.alpha


    def setWithRays(self,pencil,plane):
        """
        Set PSF from RayPencil in a specifed OpticalPlane, note this work
        for curved planes, such as optics.surface.SphericalOpticalPlane
        as well as the normal flat planes.

        :param pencil: The RayPencil (note only valid rays are considered)
        :type pencil: RayPencil
        :param plane: The OpticalPlane, of if float OpticalPlane as (0,0,plane)
        :type plane: OpticalPlane or float or None

        This is th main used method to calcaute a psf in a plane.
        """

        if isinstance(plane,float) or isinstance(plane,Vector3d):
            plane = OpticalPlane(plane)
        #          Form the moments

        moments = FixedMoments()    # Initialse
        for r in pencil:
            if r:
                pt = r.pointInPlane(plane)
                moments.addPoint(pt)
                self.wavelength = r.wavelength

        # Get the poisting of the centre of the Psf from the moments.
        self.set(plane.getSourcePoint(moments.centroid()))
        # Get the other parameters from the moments.
        self.major,self.minor,self.alpha = moments.ellipse()
        return self


    def optimalArea(self,pencil,plane):
        """
        Method to find the optimal area PSF from a raypencil starting
        as the guess locaion plane.

        This uses a simple itterative search bit provided that a reasonable guess is
        given for the inituial plane it converes quickly. The initial guess would normally
        be the paraxial image plane.

        :param pencil: the pencil or rays
        :param plane: the guess at the optimal plane, typically the paraxial plane.
        :return: the optimal psf

        Note the rays in the pencil are NOT changed.
        """
        if isinstance(plane,float) or isinstance(plane,Vector3d):
            plane = OpticalPlane(plane)

        #            set with initial condition tio local psf.
        psf = self.setWithRays(pencil,plane)
        area = psf.area()
        wave = pencil[0].wavelength/1000   # Wavelengh in mm
        delta = -0.25                      # Initial plane movement (usually it optmimal is short)
        deltaReduced = True                # reversal flag

        #            Loop looking for best
        while True:
            pl = plane.incrementSurface(delta)   # Increment plane by delta
            self = Psf().setWithRays(pencil, pl) # Make new psf
            na = self.area()
            if na < area :             # Accept
                plane = pl             # Accept plane
                area = na
                deltaReduced = False
                if abs(delta) < wave:
                    break
            else:                      # Dont accept
                if deltaReduced:       # Delta not reduced last time
                    delta = -delta
                    deltaReduced = False
                else:
                    delta *= 0.25      # Reduce delta
                    deltaReduced = True
        #
        #        Found best PSF, in self, just return

        return self


    def draw(self,colour = "k"):
        """
        Draw the psf as an ellipse to the current plot axis.

        :param colour: The colour (Default = "k")
        :type colour: str or valid Color.
        """

        n = 20
        dtheta = 2*math.pi/n
        xval = []
        yval = []

        for i in range(0,n + 1):
            theta = i*dtheta
            v = Vector2d(self.major*math.cos(theta),self.minor*math.sin(theta))
            v.rotate(-self.alpha)
            v += Vector2d(self.x,self.y)
            xval.append(v.x)
            yval.append(v.y)


        plot(xval,yval,color = colour)
        plot([self.x],[self.y],color = colour,marker='x')


class SpotDiagram(object):
    """
    Class to plot spot disgrams to matploolib panel. The conctructor just setup the
    class, use the .draw() method to render the diaagram in the required plane.

    :param pencil: the RayPencil

    Note: the RayPencil is not changed
    """

    def __init__(self,pencil):
        """
        Constrcutor
        """
        self.raypencil = pencil       # Record the RayPencil


    def draw(self,plane,drawpsf = True):
        """
        Draw the spot disagram to the current active MatPlotLib as circles
        with the centre given my the wavelelength of the first ray.

        :param plane: the plane where the diagram is located.
        :param drawpsf: draw the geometric psf on the disgram, (default = True)

        """

        # Make an optical plane if needed
        if isinstance(plane,float) or isinstance(plane,Vector3d):
            plane = OpticalPlane(plane)

        xData = []           # X and Y point locations
        yData = []

        for r in self.raypencil:
            if r:
                pt = r.pointInPlane(plane)     # Find the point in the plane
                xData.append(pt.x)
                yData.append(pt.y)

        #     Get the colour of the ray as a hex string
        col = WavelengthColour(self.raypencil[0].wavelength)
        #     Scatter plot to the current figure
        axis('equal')
        scatter(xData,yData,color=col,marker='o')
        if drawpsf:                            # Make a psf if required and plot it
            psf = Psf().setWithRays(self.raypencil,plane)
            psf.draw()


class SpotAnimation(SpotDiagram):
    """
        Class to animate a SpotDiagram
    """
    def __init__(self,pencil):
        super(SpotAnimation,self).__init__(pencil)

        #                        Set up plot and axis
        self.fig = figure()
        self.ax = axes()
        self.ax.axis("equal")
        self.ln, = self.ax.plot([],[])




    def animate(self, i):
        """
        The main animate function to draw / redra the diagram
        """



        self.ax.figure.clear()     # Clear the current figure
        self.draw(self.plane + self.startPlane,True)
        self.ax.axis("equal")
        xlabel("Plane : {0:6.3f}".format(self.plane))
        self.ax.figure.canvas.draw() # Display new fugure

        #      Update plane reversing if needed
        if abs(self.plane) > self.zrange:
            self.delta = -self.delta
        self.plane += self.delta

        #                       Return the plot
        return self.ln,



    def run(self, plane, zrange, delta = 0.1, frameinterval = 200):
        """
        The run method

        :param plane: starting plane
        :param zrange: range of animation
        :param delta: shift between frames
        :param interval: time interval in msecs
        """
        self.startPlane = plane
        self.zrange = zrange
        self.delta = delta
        self.plane = 0.0

        # Call the animation
        anim = FuncAnimation(self.fig, self.animate,repeat = True, \
                             interval = frameinterval, blit = True)



