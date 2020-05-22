===========
Ray Classes
===========

There are the main classes to perform ray tracing either indivudual rays of via higher level classes that form pencil.


Ray Class
=========

The base class in the Ray, which is abstract with the useful extensing
classes being ParaxialRay and Intensity ray.

.. autoclass:: poptics.ray.Ray
   :members:

Not normally called by users.

RayMonitor Class
================

A RayMonitor is an object can be attached to each Ray that is automatically updated every time the ray propated.
The abstarct RayMonitor class is specifed as:

.. autoclass:: poptics.ray.RayMonitor
   :members:

It is actually used via its extending clases, these being:

.. autoclass:: poptics.ray.PrintPath
   :members:

which prints the values of the ray as it is updated which is useful for debugging  and

.. autoclass:: poptics.ray.RayPath
   :members:

which records the ray path in internal lists that can then be plotted via the .draw() method to make diagrams. This
is the most common used class.
      

ParaxialRay Class
=================

This class definbes Paraxial Rays which work with the poptics.matrix classes.

.. autoclass:: poptics.ray.ParaxialRay
   :members:

Paraxial Ray Tracing
====================

.. code-block:: python

   import poptics.matrix as m
   import poptics.ray as r



Intensity Ray
=============

The IntensityRay is the main ray used for full ray tracing though optical system. The ray is specified by a position in global coordinates
by a Vector3d and a direction specified by a Unit3d.

.. autoclass:: poptics.ray.IntensityRay
   :members:

SourcePoint
===========

Class to implement a source of rays, being a vector position with assoiated intensity or spectrum

.. autoclass:: poptics.ray.SourcePoint
   :members:

RayPencil
=========

The most useful and powerful class for handling rays is the RayPencil, beinng a list or rays that can be propagated through surfaces with the
"\*=" operator. There are also a set of powerful method that allow the creation of various types or RayPencils.

.. autoclass:: poptics.ray.RayPencil
   :members:


  
