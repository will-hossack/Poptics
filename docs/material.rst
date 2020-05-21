================
Material Classes
================

Classes to handle of materail database, mainly glasses, but
also gases and liquids where are held in the asci databases using the same 
conventions as in RefractiveIndex.org. 
These class just handes the data bases of the materials, the refractive 
index is handeled by MaterialIndex() and InfoIndex() in the wavelangth module.

The default database is a text file "materails.data" located in the resource
lovcation "poptics" being the package module root. This default data base
can be replaced by a suitable creation of a new MaterialData object.

MaterialData Class
==================

Class to handle the materail database, if called with no paramters
it will assume the default data base which is loaded once into global
variable DataBase.

.. autoclass:: poptics.material.MaterialData
   :members:


Material Class
==============



.. autoclass:: poptics.material.Material
   :members:
