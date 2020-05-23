========================================
Point Spread Functions and Spot Diagrams
========================================

Set of classes to implement geometric psf and spot diagrams

There are two pairs of to support the GUI interface there being, the
first to records the current reference point option for, these being:

.. autofunction:: poptics.psf.setReferencePointOption

.. autofunction:: poptics.psf.getReferencePointOption

The options are:

====== ==============================
Option   PSF location
====== ==============================
  0      Paraxial location  (Default)
  1      Centered in paraxial plane
  2      Optimal in three dimensions
====== ==============================

The second is used by SpotDiagams to move to displayed pane, mostly used
by GUI interface. There are:

.. autofunction:: poptics.psf.setPlaneShift

.. autofunction:: poptics.psf.incrementPlaneShift

.. autofunction:: poptics.psf.getPlaneShift


Moment  Classes
===============

Class to implement moment analysis for PSF calcualtions to order 2.

.. autoclass:: poptics.psf.FixedMoments
   :members:

Psf Class
=========

Class to implment a simple geometric PSF being a being an elipse about
a specified golobal coordinate position.

.. autoclass:: poptics.psf.Psf
   :members:

SpotDiagram Class
=================

Form and plot SpotDigram from a RayPencil in a specifed OpticalPlane.
The actual diagram is rendered by the .draw() method so allowing the plane
to be easily changed, for example by the gui intreface.

.. autoclass:: poptics.psf.SpotDiagram
   :members:

Also see poptics.analysis.SpotAnalysis for a higher level class that makes
spot diagrams direct from lenses and systems with the need to form ray pencils
manually.


 

