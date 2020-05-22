============
Lens Classes
============

The classes to handle lenses and lens systems.


CurrentLens functions
=====================

There are two functions that control the default lens used in the package.
These are mainly to simply the GUI interface.

.. autofunction:: poptics.lens.setCurrentLens

and the getter function

.. autofunction:: poptics.lens.getCurrentLens

If there is no CurrectLens set, it defaults the default SimpleSinglet.

OpticalGroup Class
==================

Basic class for lenes to hold list of OpticalSurfaces, this also has
a series of methods used in tracing of rays and the analyis of optical sytsems.

.. autoclass:: poptics.lens.OpticalGroup
   :members:

This class is not normally called direclty expect for testing, it is normally
used through on of the extending classes.

      
Lens Class
==========

Class extending for a lens with extra methods to make it s easier to call.

.. autoclass:: poptics.lens.Lens
   :members:

Singlet Class
=============

Class for a general singlet lens with extra methods to set the parameters such
as bend. It also has it own draw() which draws a proper lens rather than
just the surfaces

.. autoclass:: poptics.lens.Singlet
   :members:

SimpleSinglet Class
===================

Simpler interface to Singlet to form a thin singlet lens specified
by focal length, bend and radius. This class is here to allow a very easy start to this
package

.. autoclass:: poptics.lens.SimpleSinglet
   :members:


Doublet Class
=============

Class to handle a doublet with all parameters specified in the constructor.

.. autoclass:: poptics.lens.Doublet
   :members:

Prism Class
===========

Class to implement a glass prism with methods to calcualte resolution, minimum deviation.

.. autoclass:: poptics.lens.Prism
   :members:

Eye Class
=========

Class to simulate the human eye with variable crystaline lens

.. autoclass:: poptics.lens.Eye
   :members:
      
DataBaseLens Class
==================

Class to read a lens from an input file, this the main user intreface to
read in pre-defined lenses for the internal lens database

.. autoclass:: poptics.lens.DataBaseLens
   :members:
 
OpticalSystem Class
===================

Class to represent an optical system with is a list which in an extension of the Lens class.
It can hold multiple OpticalGroups  (or Lens) with methods to manipulate the whole system or
individual components. This class will work with any of the analysis tools.

.. autoclass:: poptics.lens.OpticalSystem
   :members:

 
