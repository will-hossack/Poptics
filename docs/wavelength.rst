=================
Wavelength Module
=================

This module deal with the wavelnegth dependent features in particular refractive and
intensity spectrums.

Wavelength Value
=================

There are a set of globals defined covering the standard wavelength. All are in microns.

.. automodule:: poptics.wavelength
   :members: Default,Red,Green,Blue,BlueLimit,RedLimit,BlueColourMatch,GreenColourMatch,RedColourMatch,Mercury_i,Mercury_h,Cadmium_F,Hydrogen_F


Default and Design Wavelength
=============================

The package had two default wavelength, this is the default wave length used in simulations and
the design wavelength which is the default for paraxial calcualtions. These are controlled
by six functions

.. autofunction:: poptics.wavelength.getInitialDefaultWavelength

This function is automatically called on startup with the values being held in the global float,

- **poptics.wavelength.Default**

This should be accessed via the fuction

.. autofunction:: poptics.wavelength.getDefaultWavelength


This default can be changed with a call to:

.. autofunction:: poptics.wavelength.setDefaultWavelength

which updates the global variable.

There is an exaclty equivalent set of methods for the design wavelength, these being

.. autofunction:: poptics.wavelength.getInitialDesignWavelength

which is automatically called on start up with the result being places in global variable.

- **optics.wavelength.Design**

This should be accessed via the fuction

.. autofunction:: poptics.wavelength.getDesignWavelength

This default can be changed with a call to

.. autofunction:: poptics.wavelength.setDesignWavelength

which updates the global variable.

There is an aditional pair of functions mainly used in the GUI interface to
handle the current wavelength, these being

.. autofunction:: poptics.wavelength.getCurrentWavelength

which return the Current Wavelength, initially set the the Default Wavelength,
and the corresponding fundtion to set the current wavelength.

.. autofunction:: poptics.wavelength.setCurrentWavelength

Note the default wavelength used by the various classes is the *Default* and *Design* wavelengths
and NOT the *CurrentWavelength*.


WaveLength Class
================

This an abstarct class that defines the main methods for for all the wavelength classes. 

.. autoclass:: poptics.wavelength.WaveLength
   :members:

Refractive Index Class
======================

Refratcive Index is a abstarct class that extents Wavelength and adds methods to calcuate the refractive
index at standard wavelengths (Nd and Ne) and the Abbe numners (Vd and Ve).

.. autoclass:: poptics.wavelength.RefractiveIndex
   :members:

FixedIndex Class
================

Class to implement a basic fixed index which is independent of wavelength.

.. autoclass:: poptics.wavelength.FixedIndex
   :members:

AirIndex Class
==============

Class to implement the refactive index of air, this can either be fixed or calcualte by InfoIndex with Cauchy
coefficience or fixed at preset value (typically 1.0). 

.. autoclass:: poptics.wavelength.AirIndex
   :members:

The switch beween fixed and variable for the whole package. Note for large scale calcualtions, for example
simulation of an image it is computationally useful to switch to fixed index.
      
.. autofunction:: poptics.wavelength.setFixedAirIndex

CauchyIndex Class
=================

Class to implement the simple Cauchy refractive index which can be specified by either:

- the three Cauchy paramters, (a,b,c)
- the Nd and Vd values
- the 6 digit type integer XXXYYY where Nd = 1.XXX and Vd = Y.YY

.. autoclass:: poptics.wavelength.CauchyIndex
   :members:

Sellmeier Class
===============

 Class to implement a simple two parameter Sellmeier index with only alpha and lambda_0 terms, it is
 inplemented as a simplied case of InfoIindex. 

 .. autoclass:: poptics.wavelength.Sellmeier
    :members:

MaterialIndex Class
===================

Class to implement a materail refractive index where the paramteers are
looked up in an internal database in the same format used in RefrativeIndex.info.
All the standard class type are includes, see MaterialData for details.

.. autoclass:: poptics.wavelength.MaterialIndex
   :members:

This is the main user interface for the refractive index of of materails. Also if this class is called
with default (None) parameter, the user will be prompted at the keyboard.

This example code will prompt the user for a index and plot index against wavelnegth in a default plot.

.. code-block:: python

   from poptics.wavelength import MaterialIndex
   import matplotlib.pyplot as plt
   #       Get a material index, the defaut is to prompt for key
   index = MaterialIndex()
   index.draw()
   plt.show()

        
InfoIndex class
===============

Class to implement the refractive index calculations in the format used by RefrativeIndex.info site, this is mainly interval
class used by the MaterialIndex, AirIndex and CauchyIndex to do the actual calculations.

.. autoclass:: poptics.wavelength.InfoIndex
   :members:

Spectrum Class
==============

Class to implment a constant spectrum independant of wavelength.

.. autoclass:: poptics.wavelength.Spectrum
   :members:


GuassianSpectrum Class
======================

Class to implement a single peak Gaussian spectum

.. autoclass:: poptics.wavelength.GaussianSpectrum
   :members:

PhotopicSpectrum Class
======================

Class to implement the Photopic (high brightness) spectral response of the eye. Modelled as a Guassian.

.. autoclass:: poptics.wavelength.PhotopicSpectrum
   :members:


ScotopicSpectrum Class
======================

Class to implement the Scotopic (dark adapted) spectral response of the eye. Modelled as a Guassian.

.. autoclass:: poptics.wavelength.ScotopicSpectrum
   :members:


TriColourSpectrum Class
=======================

Class to implement a three colour spectrum with peaks as Red, Green and Blue. All peaks are the same width.

.. autoclass:: poptics.wavelength.TriColourSpectrum
	       :members:



PlanckSpectrum Class
=====================

Class to implement the Plank temperture dependand specturm.

.. autoclass:: poptics.wavelength.PlanckSpectrum
   :members:

OpticalFilter Class
===================

As class to implement a wavelength dependent filter that can be added to any Spectrum. The main class just
defines overall transmission; this is used via the extending classes.

.. autoclass:: poptics.wavelength.OpticalFilter
	       :members:

LongPassFilter Class
====================

Implment a long pass filter, to passes wavelength longer that the specified cutoff. The width is 10-90% transmission
width and the transistion is modelled by a arctan.

.. autoclass:: poptics.wavelength.LongPassFilter
	       :members:


ShortPassFilter Class
=====================

Implment a short pass filter, to passes wavelength shorter that the specified cutoff.
The width is 10-90% transmission
width and the transistion is modelled by a arctan.

.. autoclass:: poptics.wavelength.ShortPassFilter
	       :members:

BandPassFilter Class
====================

Implement a band pass filter with short and long cutoff wavelnegth. The with is 10-90% and is the
same for short and long cutoffs. The sharp is modelled by a arctan.

.. autoclass:: poptics.wavelength.BandPassFilter
	       :members:

FilterStack Class
=================

Class to implement a stack of filters.

.. autoclass:: poptics.wavelength.FilterStack
	       :members:


Colour Support Functions
========================

There are two support functions used in graph these being

.. autofunction:: poptics.wavelength.WavelengthColour



.. autofunction:: poptics.wavelength.RefractiveIndexColour



