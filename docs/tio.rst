=============================
Terminal Input / Output (tio)
=============================

The Terminal input/output module that provides a set of simple to call command line
functions that read / write to \ from the terminal with defaults, range checking
and error correction. There is also a simply option selector and
escape commands that allows simple interactive applications to be written
with the miminium of effort. This modulue is used for all terminal inout in
the examples and test code and is also called for error recovery when
wrong lens files or materials are specified.

This module has been written and mainly tested on Linix and MacOs bit should work
under Windows, but this has not been tested.

Reading Basic Types
===================

The simplest five function read the basic Python variable types; each prompt
the used with an optional default, reads from the terminal and returns the specified type after optional
sanity checking. These functions are:

.. autofunction:: poptics.tio.getString

.. autofunction:: poptics.tio.getFloat

.. autofunction:: poptics.tio.getInt

.. autofunction:: poptics.tio.getBool

.. autofunction:: poptics.tio.getComplex


Reading Vectors and Angles
==========================

The following three function real in the specific vector and angle
classes used in the poptics package, again with prompt, defaults and error checking.

.. autofunction:: poptics.tio.getVector2d

.. autofunction:: poptics.tio.getVector3d

.. autofunction:: poptics.tio.getAngle

.. autofunction:: poptics.tio.getAngleDegrees

File and Filenames
==================

The simplest and most commonly used  file function prompts and a file, open it and returns
a file descriptor, this being

.. autofunction:: poptics.tio.openFile


Finer control can be optained from

.. autofunction:: poptics.tio.getFilename

Which will prompt for the filename and return the string, but not open the file.

There is also an useful utility function that takes a string comtaining logical variables or
user directives and expand to a full file name.

.. autofunction:: poptics.tio.getExpandedFilename

Option and Menu
===============

There is simple options / menu function that prompts for a option,
and return the option number and name as a truple.
This allows simple commnad line interactive programs to be easily built.

.. autofunction:: poptics.tio.getOption

Print Function
==============

There is a simple print function that replaces to standard print(), this is independant of
Python 2/3 problems and also journal to a file if this option is set.

.. autofunction:: poptics.tio.tprint

Journal Function
================

There is a simple journal function that records all inputs  and outputs, inclduing what is printed by tprint()
to a journal file. This is under development and at the moment only output, it is planned to allows
this journal file to be reused as input.

.. autofunction:: poptics.tio.setJournal

Escape Commands
===============
There is a small set of commands that work with all imput called.
There are all refixed by %-sign. The command will be
executed and then the it will re-prompt. The current set are, (more will added in future releases).

+------------+---------------------------+
| Command    |  Action                   |
+------------+---------------------------+
|  %beep     | Rings the terminal bell   |
+------------+---------------------------+
|  %exit     | Exits the program         |
+------------+---------------------------+
| %journal fn| Open journal file  fn     |
+------------+---------------------------+
| %nojournal |  Switch off journal       |
+------------+---------------------------+
| %dir root  | director or root          |
+------------+---------------------------+


Examples
========

Simple example to read string, float and int and output the values via tprint()


   .. code-block:: python

    import poptics.tio as tio

    s = tio.getString("Type a string")
    x = tio.getFloat("And an float",3.5,1.0,10.0)
    i = tio.getInt("Then an int",0,-10,10)
    tio.tprint("Values typed are ",s,x,i)


 Read a complex , with default and max absolute, and a logical with a if:else structure.

   .. code-block:: python

    import poptics.tio as tio

    z = tio.getComplex("Complex number",complex(2,3),50.)
    if tio.getBool("Boolean",True):
      tio.tprint("Typed True")
    else:
      tio.tprint("Typed False")

Open a file for write access with a defaut type and default with logical default file name,
this will expand the logical name $Home and also
set a default extension of data which will be appended if not given.

  .. code-block:: python

     import poptics.tio as tio
     file = tio.openFile("File","w","data","$Home/output")
     file.write("Hello World\n")

Simple use of the options so select one of 4 options number 1 ("go") as the default.

   .. code-block:: python

      import poptics.tio as tio

      options = ["stop","go","reset","reformat"]
      i,opt = tio.getOption("Which option",options,1)
      tio.tprint("Option chosen was : ",i," being ",opt)
