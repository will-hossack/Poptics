================
Zernike analysis
================

Radial and Zernike Polynomials
==============================

Function to calcualte the Radial polynomial R(n,m,r) and the complex
zernike V(n,l,x,y) as defined in Born and Wolf page 770. Up to 8th order
is hard coded, but above that the factorial summation is used which will
be computationally slowed

.. autofunction:: poptics.zernike.radial

The complex Zernike polynomial V(n,l,x,y) is calculated by
		  
.. autofunction:: poptics.zernike.zernike

Optical Zernike Coefficients
============================

Function to calculate the optical zerkine components is 

.. autofunction:: poptics.zernike.opticalZernike

The number and index of the optical Zernike coefficeints
are given in the table below.

+---------+------------------------+----------+
|Order    |  Number of Cooeficient |  Index   |
+---------+------------------------+----------+
| 2       |    4                   |  0 - 3   |
+---------+------------------------+----------+
| 4       |    9                   |  4 - 8   |
+---------+------------------------+----------+
| 6       |    16                  |  9 - 15  |
+---------+------------------------+----------+
| 8       |    25                  |  16 - 24 |
+---------+------------------------+----------+
| 10      |    36                  |  25 - 35 |
+---------+------------------------+----------+
| 12      |    49                  |  36 - 48 |
+---------+------------------------+----------+


Function to return the name of the optical zernike component is:

.. autofunction:: poptics.zernike.opticalZernikeName

This gives names up to 10th order (index 35), and beyond that gives
the index number. Also of the first parameter is a list it is then assume
to be a list of coefficient in order and all an resturned in a fomatted string
with end of line characters.

		  
