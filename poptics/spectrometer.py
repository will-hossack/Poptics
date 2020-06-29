"""
         Classes to implemeent various spectrometers

"""
from poptics.lens import OpticalGroup
from poptics.wavelength import MaterialIndex,AirIndex,getDefaultWavelength
from poptics.ray import IntensityRay,RayPencil
from poptics.surface import FlatSurface
from poptics.vector import Unit3d,Angle,Vector2d,Vector3d
import math
import numpy as np
from poptics.tio import getFilename,getExpandedFilename,getLogger
from matplotlib.pyplot import plot,xlabel,ylabel,title,grid
from scipy.special import j1

class Prism(OpticalGroup):
    """
    Class to make a simple prism being an equilateral triangle with the
    top of the prism being vertical and the base being parallel to the optical
    axis.

    :param group_pt: the centre of the prism (Default = (0,0,0))
    :type group_pt: Vector3d or float
    :param angle: prism angle in degrees (Default = 60)
    :type angle: float
    :param height: height of prism from base to peak in mm (Default = 40)
    :type height: float
    :param index: the refactive index (Default = "BK7")
    :type index: RefractiveIndex or str

    """
    def __init__(self,group_pt = 0.0, angle = 60.0, height = 40.0, index = "BK7"):
        OpticalGroup.__init__(self,group_pt)

        # Make the prism from two FlatSurfaces at suitable positions and
        # surface normals

        if isinstance(index,str):        # Sort out index
            self.n = MaterialIndex(index)
        else:
            self.n = index

        #       Variable needed below
        self.height = float(height)
        self.angle = math.radians(angle)    # Hold angle in radians
        self.tilt = 0.0

        #        Make surface normals to front and back faces
        fn = Unit3d(Angle(2*math.pi - self.angle/2))
        bn = Unit3d(Angle(self.angle/2))

        #         Poistion of front and back surfaces
        p = Vector3d(0.0,0.0,height*math.tan(self.angle/2)/2)

        #         Make the two surfaces and add then to the self (an OpticalGroup)
        #         Not need to specify type are refracting.
        front = FlatSurface(-p,fn,type = 1,index = self.n)
        self.add(front)
        back = FlatSurface(p,bn,type=1,index = AirIndex())
        self.add(back)

    def __str__(self):
        """
        The str function

        :return: inrmation on the prism
        """
        return "{0:s} a: {1:5.3f} h: {2:5.3f} n: {3:s}".format(str(self.getPoint()),\
                math.degrees(self.angle),self.height,self[0].refractiveindex.title)

    def setIndex(self,index):
        """
        Set (or reset) the refratcive index
        """
        if isinstance(index,str):
            index = MaterialIndex(index)
        self[0].refractiveindex = index

    def setTilt(self,tilt = None):
        """
        Set the tilt angle of the prism.

        If called with None will use the current value of tilt and angle and reset
        the surface to be consistent.

        :param tilt: the tilt angle of the prsim in radians (Default = None) reset
        :type: float
        """
        if tilt != None:
            self.tilt = tilt             # Update tilt if given
        #        Make surface normals to front and back faces allowing for the tilt
        fn = Unit3d(Angle(2*math.pi - self.angle/2 - self.tilt))
        bn = Unit3d(Angle(self.angle/2 - self.tilt))

        #         Poistion of front and back surfaces allowing for the tilt
        p = Vector3d(0.0,0.0,self.height*math.tan(self.angle/2)/2)
        p.rotateAboutX(-self.tilt)

        #      Update the locations and surface normals of the two faces.
        self[0].point = -p
        self[1].point = p
        self[0].normal = fn
        self[1].normal = bn
        return self



    def minDeviation(self,wavelength):
        """
        Get the angle of minium deviation at specified wavelength.

        Note this needs to take into account the AirIndex used in the package.

        :param wave: the wavelength
        :type wave: float
        :return: the minimum deviatation as a float in radians.

        """
        a = AirIndex().getValue(wavelength)
        nval = self.n.getValue(wavelength)/a    # Correct for air index
        sa = nval*math.sin(self.angle/2)
        s = math.asin(sa)
        return 2*s - self.angle           # Return radians.


    def maxResolution(self,wave = None):
        """
        Get the maximum resolution at specifed wavelength at angle of
        minimum deviation. This is given by d dn/d lambda where d is the maximium
        pathlength difference given by the size of the prism.

        :param wave: the wavelength
        :return: maximum resolution lambda / d lambda as float
        """

        d = 2000.0*self.height*math.tan(self.angle/2) # Max pathlength in microns.
        dn = self.n.getDerivative(wave)          # dn/dy of materail
        return d*dn    #


    def resolution(self, radius, wave = None):
        """
        Calcualte the resolution for a specifed input beam radius at
        angle on minimum deviation. It assumes that the resolution is limited
        by the beam radius and not the size of the prism.

        :param radius: radius of input beam
        :type radius: float
        :param wave: wavelength
        :type wave: float
        :return: resolution lamdba / d lambda as a float

        """
        dev = Prism.minDeviation(self,wave)
        alpha = dev/2 + self.angle/2

        #      Form path difference between top and bottom of the beam
        d = 4*radius*math.sin(self.angle/2)/math.cos(alpha)
        dmax = 2.0*self.height*math.tan(self.angle/2) # Length of bottom of prism
        if d > dmax:
            d = dmax
            print("Resolution limited by size of prism")


        dn = self.n.getDerivative(wave)    # dn/d lambda
        return 1000*d*dn                   # scale to microms



    def getInputPoint(self):
        """
        Get the input point in the centre of the first face

        :return: Point on front face in global coordinates
        """
        return self[0].getPoint()

    def getOutputPoint(self):
        """
        Get tyhe ooutput point in the centre of the second surface

        :return: Point on the back face in global coordinates.
        """
        return self[1].getPoint()

    def getOutputAngle(self,inAngle,wavelength = None):
        """
        High level method to get the output angle of a beam given
        input angle and wavelength.

        Ths methods traces a ray through the system but hide the mechanics and
        complications of doing this.

        :param inAngle: input angle in radians (from the optical axis)
        :type inAngle: float
        :param wavelength: the wavelength (Default = 0.55)
        :type wavelength: float
        :return: output angle in radians (typically -ve)
        """
        #        Get prism point and angle of input at Unit3d
        #
        pt = self.getInputPoint()
        u = Unit3d(Angle(inAngle))
        #         Make a ray and trace it
        ray = IntensityRay(pt,u,wavelength)
        ray *= self
        a = ray.getAngle()                 # The the ray Angle
        return a.theta*math.cos(a.psi)     # get in radians allowing for -ve


    def getWavelength(self, inAngle, outAngle, wavelengths = [0.25,1.0]):
        """
        Itterative methiod to get the wavelength given input and output angles.

        Note if impossible angles given or wavelength goes out of range, error message
        and NaN returned.

        :param inAngle: input angle in radians
        :type inAngle: float
        :param outAngle: output angle in radians
        :type outAngle: float
        :param wavelengths: range of allowable wavelengths [min,max]
        :type: wavelengths: list of length 2
        :return: the wavelength as a float, "NaN" if it fails to converge.

        """

        #        Get prism point and angle of input at Unit3d
        #
        pt = self.getInputPoint()
        u = Unit3d(Angle(inAngle))

        #         Guess at initial wavelngth
        wave = (wavelengths[1] - wavelengths[0])/2
        #         Make input ray at guess wavelength
        ray = IntensityRay(pt,u,wave)

        #       Parameters for seaerch
        delta = 0.1
        forward = True
        na = float("inf")   # New angle

        while abs(na - outAngle) > 1.0e-9/abs(outAngle) :
            nray = ray*self       #      New Ray through prism
            na = nray.getAngle()
            na = na.theta*math.cos(na.psi)    # In radians
            if na < outAngle:                       # Less that target
                wave += delta
                forward = True
            else:
                if forward:                   # Half step
                    delta *= 0.5
                forward = False
                wave -= delta
            if wave < wavelengths[0] or wave > wavelengths[1]:
                print("Out of wavelength range :")
                return float("nan")

            ray.wavelength = wave             # Update the wavelength of ray

        return ray.getWavelength()             # End of loop, so success, return value

    def draw(self):
        """
        Method to draw the prism

        :return: None

        """
        pt = self.getPoint()     # Centre of prism

        #         Form top,left,right corners
        top = Vector2d(pt.z, pt.y + self.height/2)
        d = self.height*math.tan(self.angle/2)
        left = Vector2d(pt.z - d , pt.y - self.height/2)
        right = Vector2d(pt.z + d, pt.y - self.height/2)


        top.rotate(self.tilt)
        left.rotate(self.tilt)
        right.rotate(self.tilt)

        #      Plot them out with plt.plot
        plot([top[0],left[0],right[0],top[0]],[top[1],left[1],right[1],top[1]],"k",lw=2.0)



class PrismSpectrometer(Prism):
    """
    Class to exent the Prism class so add methods specific to a specrometer

    :param group_pt: reference point for prism, (Default = 0,0,0)
    :type group_pt: Vector3d or float
    :param angle: the prism angle in degrees (Default = 60)
    :type angle: float
    :param height: the height of the prism (Default = 40)
    :type height: float
    :param index: refractive index material of the prism (Default = "BK7")
    :type index: RefractiveIndex or str
    :param beam: the beam radius (Default = 10.0)
    :type beam: float
    """

    def __init__(self,group_pt = 0.0, angle = 60.0, height = 40.0, index = "BK7", beam = 10.0):
        """
        Constructor
        """
        Prism.__init__(self,group_pt, angle, height, index)  # Set underlying prism
        self.beam = beam                                     # the beam radius


    def __str__(self):
        """
        Standard str()
        """
        return Prism.__str__(self) + " beam : {0:6.3f}".format(self.beam)

    def setUpWavelength(self,wavelength):
        """
        Method to set the alignment wavelength, without call will be set to package default

        :param wavelength: the wavelength (Default = None) withh give default
        :type wavelength: float or None
        """
        if wavelength == None:
            self.wavelength = getDefaultWavelength()
        else:
            self.wavelength = wavelength
        return self


    def minDeviation(self,wavelength = None):
        """
        Method to get the minimum deviation, the default is the current setup
        wavelength, but this can be overridden by a supplied wavelength

        :return: float the minimum deviation in radians
        """
        if wavelength == None:
            wavelength = self.wavelength

        return Prism.minDeviation(self,wavelength)


    def resolution(self):
        """
        Method to get the resolution at the current setup wavelength

        :return: float the resoltion of prism with at setup wavelength and beam raidius
        """
        return Prism.resolution(self,self.beam,self.wavelength)

    def lineShape(self,peakAngle,width,angle):
        """
        Method to return the lineshape

        :param dw: the wavelength from peak
        :type dw: float
        :param width: width of line
        :type width: float
        :return: float
        """
        x = abs(peakAngle - angle)/width
        if x == 0.0:
            return 1.0
        else:
            return (2*j1(x)/x)**2



    def getSpectrum(self,wavelengths,intensities = 1.0):
        """
        Method to get output spctrum of angle for given array wavelengths
        and intensities.

        :param wavelengths: numpy array of wavelengths
        :type wavelength: np.ndarray
        :param intensities: numpy array of correspontiin intensities of constant
        :type intensities: np.ndarray or float
        :return: [angles,peaks,widths] as list of np.ndarray
        """

        if isinstance(intensities,(float,int)):    # If single value, make np array
            intensities = np.full(wavelengths.size,intensities)

        pt = self.getInputPoint()                 # Input point on prism
        ang = self.minDeviation()/2               # Angle of imput beam
        pencil = RayPencil().addRays(pt,ang,wavelengths,intensities) # Make pencil of rays
        pencil *= self                    # Put through prism

        #          Extarct the information about the rays into numpy arrays.
        angles = np.zeros(len(pencil))
        peaks = np.zeros(len(pencil))
        widths = np.zeros(len(pencil))

        for i,ray in enumerate(pencil):
            a = ray.getAngle()                    # Get the angle in theta,psi format
            angles[i] = a.theta*math.cos(a.psi)    # Extract -ve angle
            peaks[i] = ray.getIntensity()
            #       Note width is lambda/(pi*diameter) but 1,000 to convert nn -> um
            widths[i] = ray.getWavelength()/(2000*math.pi*self.beam)

        return angles,peaks,widths

    def getIntensitySpectum(self,wavelengths,intensities = 1.0):
        """
        Get an intensity spectum with suitable sampling taking into accound the
        lineshape of the sprectrometer.

        :param wavelengths: numpy array of wavelengths
        :type wavelength: np.ndarray
        :param intensities: numpy array of correspontiin intensities of constant
        :type intensities: np.ndarray or float
        :return: [fieldAngle,spectralOutput] at two np.ndarrays
        """
        angles,peaks,widths = self.getSpectrum(wavelengths,intensities)

        #      Get arnge of angles to calulate over
        minField = np.min(angles) - 10*np.max(widths)
        maxField = np.max(angles) + 10*np.max(widths)
        #       Sample finely enough to make peak widths visible, but least 400points
        npoints = max(int((maxField - minField)/np.min(widths)),400)

        #            Make the two two array for the output data
        fieldAngle = np.linspace(minField,maxField,npoints)
        spectralOutput = np.zeros(fieldAngle.size)

        #           Add each peak in turn
        for a,p,w in zip(angles,peaks,widths):

            for i,af in enumerate(fieldAngle):
                s = self.lineShape(a,w,af)       # Add the spectrometer lineshape
                spectralOutput[i] += p*s

        #    Return the two numpy arrays as a list
        return fieldAngle,spectralOutput


    def plotSpectrum(self,wavelengths,intensities = 1.0):
        """
        High level method to plot a spectrum to matplotlib frame with sensible
        plot defaults.

        :param wavelengths: numpy array of wavelengths
        :type wavelength: np.ndarray
        :param intensities: numpy array of correspontiin intensities of constant
        :type intensities: np.ndarray or float
        """

        fieldAngle,spectralOutput = self.getIntensitySpectum(wavelengths,intensities)

    #     Do the actual plot
        plot(np.degrees(fieldAngle),spectralOutput)
        grid()
        title("Spectral plot")
        xlabel("Angle in degrees")
        ylabel("Intensty")

    def fromFile(self,fn = None):
        """
        Read a spectrometer set up from a file. The filename will be appeneded with
        appended with a default extension of ".spec"

        :param fn: file name, (Default = None)
        :type fn: str

        File syntax is serise of commands (one per line) being

        ::

            point: x,y,z
            index: index_name
            angle: prism_angle (in degrees)
            height: prism_height (in mm)
            tilt: prism_tilt (in degrees)
            beam: beam_radius (in mm)
            setup: setup_wavelength (in um)

        Liner starting with # are ignored as comments
        """

        while True:

            if fn == None:
                fn = getFilename("Spectrometer file","spec")
            else:
                fn = getExpandedFilename(fn)   # Sort out logicals
            if not fn.endswith("spec"):        # Append ".spec" if not given
                 fn += ".spec"

            try:
                sfile= open(fn,"r")             # open file
                lines = sfile.readlines()
                sfile.close()
                break
            except FileNotFoundError:
                getLogger().error("Failed to find spectrometer file : " + str(fn))
                fn = None


        #          read file and process one line at a time
        #

        #           Read through line at a time
        for line in lines:

            line = line.strip()
            if not line.startswith("#") and len(line) > 0:   # Kill comments and blanks
                token = line.split()

                if token[0].startswith("point"):
                    v = eval(token[1])
                    self.setPoint(v)

                elif token[0].startswith("index"):
                    self.setIndex(token[1])

                elif token[0].startswith("angle"):
                    self.angle = math.radians(float(token[1]))
                    self.setTilt(self.tilt)          # Reset surfaces

                elif token[0].startswith("height"):
                    self.height = float(token[1])

                elif token[0].startswith("beam"):
                    self.beam = float(token[1])

                elif token[0].startswith("tilt"):
                    self.setTilt(math.radians(token[1]))

                elif token[0].startswith("setup"):
                    self.setUpWavelength(float(token[1]))

                else:
                    raise ValueError("Sprectometer: illegal key : {0:s}".format(token[0]))

        return self


class Grating(OpticalGroup):
    """
    Class to for a simple diffratcion grating with a transmission grating on
    a glass substrate
    """

    def __init__(self,group_pt = 0.0, pitch = 2.0, thickness = 5.0, height = 10.0, angle = 0.0):
        OpticalGroup.__init__(self,group_pt)


        self.height = height
        self.pitch = pitch
        n = MaterialIndex("BK7")

        # Surface normal to back and from surfaces
        u = Unit3d(Angle(-angle))
        p = 0.5*thickness*u
        print(str(p))

        front = FlatSurface(-p,u,type = 1,index = n)
        self.add(front)
        back = FlatSurface(p,u,type=1,index = AirIndex())
        self.add(back)


    def draw(self):

        fpt = self[0].getPoint()
        print(str(fpt))
        bpt = self[1].getPoint()
        print(str(bpt))
        sn = self[0].getNormal()
        print(repr(sn))

        xf = [fpt.z - self.height*sn.y/2, fpt.z, fpt.z + self.height*sn.y/2]
        yf = [fpt.y + self.height*sn.z/2, fpt.y, fpt.y -self.height*sn.z/2]
        print(str(xf))
        print(str(yf))

        plot(xf,yf,"k",lw = 2.0)

        xf = [bpt.z - self.height*sn.y/2, bpt.z, bpt.z + self.height*sn.y/2]
        yf = [bpt.y + self.height*sn.z/2, bpt.y, bpt.y -self.height*sn.z/2]

        plot(xf,yf,"k",lw = 2.0)





