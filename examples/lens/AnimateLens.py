"""
    Example to annimate a collimated ray pencil varying in in angle

"""
from poptics.lens import DataBaseLens
from poptics.wavelength import getDefaultWavelength
from poptics.ray import RayPencil,RayPath
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math




class LensAnimation(object):
    """
        Basic lens annimation for for collimated beam
    """
    def __init__(self,lens,wavelength = None):
        self.lens = lens
        self.wavelength = getDefaultWavelength(wavelength)
        self.op = lens.backFocalPlane()

        self.angle = 0.0                   # Control variables
        self.delta = math.radians(1.0)
        self.anglerange = math.radians(10)

        #                        Set up plot and axis
        self.fig = plt.figure()
        self.ax = plt.axes()
        self.ax.axis("equal")
        self.ln, = self.ax.plot([],[])




    def animate(self, i):
        """
        The main animate function to draw / redra the diagram
        """

        #     make a pencil of the right wavelengh and propagate throgh lens to back focal plane
        pencil = RayPencil().addBeam(self.lens,self.angle,"vl",wavelength = self.wavelength)\
            .addMonitor(RayPath())
        pencil *= self.lens
        pencil *= self.op


        self.ax.figure.clear()     # Clear the current figure
        self.lens.draw()           # Draw new diagram
        self.op.draw()
        pencil.draw()
        self.ax.axis("equal")
        self.ax.figure.canvas.draw() # Display new fugure

        #      Update the angle (reversing when it reached angle_range)
        if abs(self.angle) > self.anglerange:
            self.delta = -self.delta
        self.angle += self.delta

        #                       Return the plot
        return self.ln,



    def run(self, anglerange = 10.0 , delta = 1.0):
        """
        The run method

        :param anglerange: the range of angles in degrees
        :param delta: angle between frames

        """

        self.angle = math.radians(anglerange)
        self.anglerange = math.radians(anglerange)
        self.delta = math.radians(delta)

        # Call the animation
        anim = FuncAnimation(self.fig, self.animate,repeat = True, \
                             interval = 200, blit = True)





def main():

    #
    #      Read lens in from database
    #
    lens = DataBaseLens("Gauss-F1.5")
    lens.setIris(0.7)           # Set iris to 0.7 of max

    an = LensAnimation(lens,0.61)
    an.run(20.0)
    plt.show()

main()










