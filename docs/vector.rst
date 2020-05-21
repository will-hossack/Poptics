==============
Vector Classes
==============

These classes handle two and three dimensional vectors with many supporting
methods to simplfy their use. These classes are used throughout the poptics
package but can also be used as stand alone classes for other applications.

Note these vector classes are all interally hand coded and do not use
Numpy.

Vector2d Class
==============

Class for two dimensional vectors. This class is typically used to describe
point in planes.

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

Extending class to Vector3d to handle unit three dimensional unit vectors, this class is
typically used for ray directions and also contains the code to implment Snell's Law for
reflection and refration at surfaces.

Note the default constructor will form a Unit3d set to "invalid" with all
components set to "nan". 

.. autoclass:: poptics.vector.Unit3d
   :members:

Angle Class
===========

 Class to implement a unit vector using theta/psi angles. It is not used for internal
 calcualtions but is a humanly understandable alternative for secifying and and reading
 ray directions. Note both angle are in radians.

 .. autoclass:: poptics.vector.Angle
    :members:

 

