===============
Surface Classes
===============

Set of classes to respesent various types of optical planes and surfaces.
These class types are the main obects used in tracing of rays.


Surface Constants
=================

The following constants define surface types:

* **Clear** surfaces that do not change rays paths, these include image planes,
  apertures, input / output plane etc

* **Refrating** surfaces, flat or curved glass surfaces that refract rays; these must be specified with a refractive index on the
  *image side*.

* **Reflecting** surfaces, flat or curved mirrored surfaces.

* **Blocked** to represent a blocked rays.

.. automodule:: poptics.surface
   :members: Clear,Refracting,Reflecting,Blocked


Surface Class
=============

Abstract base class to give represent a general surface. This class defines

* Surface reference point being a Vector3d that defines the location of the centre of the surface.

* Optical Group that the surface belongs to, may be *None*.

* Type of surface.

* Refractive index on the image side, which may be *None*.

.. autoclass:: poptics.surface.Surface
   :members:

This class in never called ditectly by users, it is always called via on of the edtending classes.

FlatSurface Class
=================

Class to represent a general Flat optical surface with specified surface normal.

.. autoclass:: poptics.surface.FlatSurface
   :members:

This not normally used in systems that consist of lenses, but us used in poptics.lens.Prism class.

OpticalPlane Class
==================

Class to represent a flat optical plane pertendicular to the optical axis with fixed surface normal along the optical axis.

.. autoclass:: poptics.surface.OpticalPlane
   :members:

CircularAperture Class
======================

Class to represent a circular aperture of specifed fixed radius.

.. autoclass:: poptics.surface.CircularAperture
   :members:


AnnularAperture Class
=====================

Class to represent a circular annular aperture of specifed fixed inner and outer radius.

.. autoclass:: poptics.surface.AnnularAperture
   :members:

  
IrisAperture Class
======================

Class to represent a circular iris aperture of variable radius specified by a maximum radius and open ration.

.. autoclass:: poptics.surface.IrisAperture
   :members:


KnifeAperture Class
=======================

Class to implement a knife edge aperture for knife-edge test.

.. autoclass:: poptics.surface.KnifeAperture
   :members:

This is not normally called directly but used via the poptics.analysis.KnifeTest.

ImagePlane Class
================

Class to represent an image plane, this is the same as OpticalPlane but wuth additial size information.
This affets the .draw() method, and should be used for input and output image planes.

.. autoclass:: poptics.surface.ImagePlane
   :members:

QuadricSurface Class
====================

Class to represent a quadratic surface; this is main class for all curved refracting optical surfaces but is normaally called
via the extending classes to give spherical or parabilic surfaces.

.. autoclass:: poptics.surface.QuadricSurface
   :members:

SphericalSurface Class
======================

Class to represent a Spherical Surface. This is the main class used is specifying lenses, but is more usually called via the optics.lens
classes.

.. autoclass:: poptics.surface.SphericalSurface
   :members:


ParabolicSurface Class
======================

Class to represent a  Parabolic Surface, similar to Spherical Surface, but with parabolic (aspheric) surface.

.. autoclass:: poptics.surface.ParabolicSurface
   :members:

SurfaceInteraction Class
========================

Class to return the interaction of a ray with a surface. Each surface an this object returns this 
via the method .getSurfaceInteraction(ray). It is then used to act on the ray to update
it.

.. autoclass:: poptics.surface.SurfaceInteraction


 There are no methods associated with this class, it is used to transfer information to
 update the ray and is not normally called by users.
