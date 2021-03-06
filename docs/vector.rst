==============
Vector Classes
==============

These classes handle two and three dimensional vectors with many supporting
methods to simplfy their use. These classes are used throughout the Poptics
package but can also be used as stand alone classes for other applications.

These vector classes are all interally hand coded and do not use
Numpy which significantly imporve efficiency.


Vector2d Class
==============

Class for two dimensional vectors. This class is typically used to describe
points in planes.

.. autoclass:: poptics.vector.Vector2d
   :members:


Vector3d Class
==============

Class for three dimensional vectors. This is main class used in specifiy
rays and component positions in the poptics package.  

.. autoclass:: poptics.vector.Vector3d
   :members:

Unit3d Class
============

Extending class to Vector3d to handle unit three dimensional unit vectors,
this class is typically used for ray directions and surface normnals. It also contains the code to
implment Snell's Law for reflection and refration at surfaces.

Note the default constructor will form a Unit3d set to "invalid" with all
components set to "nan". 

.. autoclass:: poptics.vector.Unit3d
   :members:

Angle Class
===========

 Class to implement a unit vector using theta/psi angles. It is not used for any internal
 calcualtions but is a humanly understandable alternative for secifyinfg
 ray directions and surface normals. Note both angle are in radians.

 .. autoclass:: poptics.vector.Angle
    :members:

 

Examples
========

Some simple code examples so show some of the main operations.

.. code-block:: python

    from poptics.vector import Vector3d
    a = Vector3d(1,2,3)
    b = Vector3d(4,5,6)
    c = a + b       # Add two vectors
    c += 10.0       # Add 10.0 to all compoents
    dot = a.dot(b)  # Dot product
    cross = a.cross(b) # Cross product

Example showing how to get and set in polars.

.. code-block:: python

    from poptics.vector import Vector3d
    a = Vector3d()       # Default vector set to (0,0,0)
    a.set(1.0, 2.0, 3.0) # Set compoents
    r, theta, psi = a.polar()  # Get polars as list
    b = Vector().setPolar(r, theta, psi) # New vector set by polars
    c = Vector().setPolarDegrees(10.0, 37.0, 127.0) # set polars in degrees

One of the most useful method to specify a Unit3d is via its .parseAngle() method, which
will accept parameters in also any format including abgle in degrees. Some examples
are shown below:

.. code-block:: python

    from poptics.vector import Unit3d
    a = Unit3d().parseAngle(0.2)       # theta = 0.2 radians, psi = 0
    b = Unit3d().parseAngle("30","87")  # theta = 30 deg, psi = 87 deg
    c = Unit3d().parseAngle(3.5,7.2,9.1) # Unit vector in specficied direction

More


    
    

		


    
