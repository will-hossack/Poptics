================
Analysis Classes
================

A set of classes to perform various analysis tasks of the lenses.


TargetPlane Class
=================

Class to implement an ImagePlane with a set or targets.

.. autoclass:: poptics.analysis.TargetPlane
   :members:

OpticalImage Class
==================

Class to represent an OpticalImage, being a ImagePlane with a greyscale
image held in a two dimensional numpy array.

.. autoclass:: poptics.analysis.OpticalImage
   :members:



ColourImage Class
=================

Class to represent a ColourImage, having the same charcteristics
as OpticicalImage but with each pixel being a [r,g,b] triplet.

.. autoclass:: poptics.analysis.ColourImage
   :members:

SpotAnalysis Class
==================

Perform a spot analysis of a lens system with eirher a collimated or source
beam. This is much easier to call that the optics.psf.SpotDiagram class.

.. autoclass:: poptics.analysis.SpotAnalysis
   :members:


KnifeEdgePlot class
===================

Class to implement the Knife Edge test for an infinite object.

.. autoclass:: poptics.analysis.KnifeTest
   :members:



	   

