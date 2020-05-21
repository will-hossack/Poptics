=======================
CSV File Read and Write
=======================

There are two simple CSV file functions to read and write simple CSV of float data direct
to and from numpy.ndarray. There are:

.. autofunction:: poptics.csvfile.readCSV

This funtion will also ignore comment lines starting with \# and also blank lines, but there is no
other processing. The actual reads and done with the standard csv.read() function.
		  
.. autofunction:: poptics.csvfile.writeCSV

The written files are simple comma delimited file with floats is 12.5e format. The actual write is done
by default action of csv.write()
		  
Examples
========

If a CSV file contains two columes of floats values with a comma spearator these two columns can be read to
two numpy ndaray by:

.. code-block:: python

     from poptics.csvfile import readCSV
     from poptions.tio import getFilename
     # Get filename
     fn = getFilename("CSV file","csv")
     xData , yData = readCSV(fn)
     		
While is the CSV file has three columns the first and third columum, with the second ignored,
can be read with the following code:

.. code-block:: python

     from poptics.csvfile import readCSV
     from poptions.tio import getFilename
     # Get filename
     fn = getFilename("CSV file","csv")
     xData , yData = readCSV(fn,(True,False,True))


The write a simple CSV file data from two numpy array into a default comma delimted CSV
file with no header can be done with:

.. code-block:: python

    from poptics.csvfile import writeCSV
    from poptions.tio import getFilename
    import numpy as np
    #      Make some data
    xdata = np.linspace(0.0,10.0,100)
    ydata = np.cos(xdata)
    #      Get an output file and output data
    fn = getFilename("CSV file","csv")
    ln = writeCSV(fn,[xdata,ydata])
    print("Number of lines written : " + str(n))


These functions are used in a number of examples to read or write data, but are not used internally
in the poptics package.
