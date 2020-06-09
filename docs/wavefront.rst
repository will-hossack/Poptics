==================
Wavefront analysis
==================

The module contains a set of classes to calculate, analyes and display


WaveFront class
===============

General class to hold an analyic wavefront. This class defines most of the display and analysis
methods for wavefronts but it normally used via one of the extending classes that sepecify the
actual wavefront.

.. autoclass:: poptics.wavefront.WaveFront
   :members:

KingslakeWaveFront class
========================

Class to implements a single Kingslake formulation of the wavefront as
definited in Malacara. Useful for testing and comparision with standard results.

.. autoclass:: poptics.wavefront.KingslakeWaveFront
   :members:

ZernikeWaveFront class
======================

Class to implement a ZernikeWaveFront specified by the Zernike Optical polynomials. This is
the wavefront typically used in data fitting.

Note: calcualtions, and especially OTF calculations, can be rather slow due to the computational
cost calculating the Zernike polynomials.

.. autoclass:: poptics.wavefront.ZernikeWaveFront
   :members:

SeidelWaveFront Class
=====================

Class to implement Seidel wavefront with the 6 parameters correspomnd to the six Seidel aberrations
terms.

.. autoclass:: poptics.wavefront.SeidelWaveFront
   :members:

PolynomialWaveFront Class
=========================

Class to specify a wafefron with x/y polynomials. This is an extension of the KingslakeWaveFront and is
added for completeness. It is not really used since cartestian polynomials are are not orthogonal so are not
really possible to fit to reliably. 

.. autoclass:: poptics.wavefront.PolynomialWaveFront
   :members:


WaveFront Mask Classes
======================

Wavefronts are defined across a circular aperture, this typically being the exit aperture of
a lens or optical system. To account for some exit aperure being partically onscured there
is the option to add a logical mask to the wave front. These are:

.. autoclass:: poptics.wavefront.CircularMask
   :members:

This is the default mask that is applied to all wavefront as is added to each of the above
wavefronts automatically. Ths second is


.. autoclass:: poptics.wavefront.AnnularMask
   :members:

Which has central stop as found on many mirror telescope system.




WavePoint class
===============

Class to implenet a WavePoint. Mainly used intrnally 

.. autoclass:: poptics.wavefront.WavePoint
   :members:


WavePointSet class
==================

Class to implement a set (list) of Wavepoints in a plane with additional methods
to analyse them. Mainly used internally.

.. autoclass:: poptics.wavefront.WavePointSet
   :members:



 
WaveFrontAnalysis Class
=======================

.. autoclass:: poptics.wavefront.WaveFrontAnalysis
   :members:


Interferometer Class
====================

Class to implement an virtual interferometer to view the wavefront as a
Twyman Green fringe pattern.

.. autoclass:: poptics.wavefront.Interferometer
   :members:

 
