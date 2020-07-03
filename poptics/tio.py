"""
The tio package gives a set of terminal input methods to read the built in
Python types plus Vector2d, Angle and Vector3d classes and open files.

The packages formats prompts, give defaults, does range and general sanity
checking and will re-prompt on errors. There is also a simple print function
and a simple internal command handler and journal facility which is being
developed.
"""

from os import listdir
import os.path as p
from datetime import datetime
import math
from poptics.vector import Vector2d, Vector3d, Unit3d, Angle
import sys

#                    Setup the logging
import logging
logger = logging.getLogger("Poptics")  # Glogal logger
logger.handlers.clear()             # Clear any stray handlers (IPython issue)
logger.setLevel(logging.INFO)
fmt = logging.Formatter('%(levelname)s: %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(fmt)                   # Set format
ch.setLevel(logging.INFO)              # Set print level to INFO
logger.addHandler(ch)                  # Add the handler


def getLogger():
    """
    Function to get the message logger when used in other parts of package

    :return: the packaage logger
    """
    return logger


#               Internal globals
__journalFile = None
__tiooutput = sys.stdout
__tioerr = sys.stderr
__tioesc = "%"
__tiocomment = "#"


def getString(prompt, default=None):
    """
    Read a string from the terminal with no processing or evaluation.

    :param prompt: The prompt to be displayed.
    :param default: the default string (defaults to None)
    :type prompt: str
    :type default: str
    :return: str with no processing, but leading and trailing white space will be removed.

    Note: will allow a zero length string to be returned.
    """
    while True:
        val = __getInput(prompt, default)
        try:
            s = str(val)          # Force to be a string
            return s.strip()      # Strip off leading and trailing white space
        except:                                  # Catch everything
            logger.error("String conversion failed")


def getFloat(prompt, default=None, min=None, max=None):
    """
    Read a float from the terminal with optional default and range checking.

    :param prompt: the prompt to be displayed.
    :type prompt: str
    :param default: float (defaults to None)
    :type default: float
    :param min: float min value accepted (defaults to None)
    :type min: float
    :param max: float max value accepted (defaults to None)
    :type max: float
    :return: float in specified range.

    Note: if response is a string it will be evaluated.
    """
    if default != None:
        default = float(default)
    if min == None:
        min = float("-Inf")
    if max == None:
        max = float("Inf")
    while True:
        val = __getInput(prompt, default)
        try:                                     # Work out what happened
            if isinstance(val, str):             # If str eval what been given
                val = eval(val)
            fval = float(val)                            # force to float
            if fval >= min and fval <= max:              # test range
                return fval
            else:
                logger.error("Float {0:6.3e} outside range {1:6.3e} to {2:6.3e}"\
                             .format(fval, min, max))
        except (ValueError, NameError, ZeroDivisionError, SyntaxError):
            logger.error("Failed to evaluate float : '{0:s}'".format(str(val)))


def getInt(prompt, default=None, min=None, max=None):
    """
    Read an int from the terminal with optional default and range checking.
    The default is decimal but also binary (prefix 0b) , oct (prefix 0o),
    hex prefix (0x) is also supported.

    :param prompt: the prompt string to be displayed.
    :type prompt: str
    :param default: default value, (defaults to None)
    :type default: int
    :param min: min value accepted (defaults to None)
    :type min: int
    :param max: max value accepted (defaults to None)
    :type max: int
    :return: int in specified range.

    Note: if response is a string it will be evaluated.
    """
    if min == None:
        min = -sys.maxsize - 1
    if max == None:
        max = sys.maxsize
    while True:
        val = __getInput(prompt, default)             # Get input
        try:                                          # Work out what happened
            if isinstance(val, str):              # If str eval what been given
                val = eval(val)
            #if isinstance(val,float):
            #   if round(val) == val:                    # It is a int
            #val = int(round(val))

            if isinstance(val, int):                    # Check we have an int
                if val >= min and val <= max:            # test range
                    return val
                else:
                    logger.error("Int {0:d} outside range {1:d} to {2:d}".\
                                 format(val, min, max))
            else:
                logger.error("Conversion of '{0:s}' to integer failed".format(str(val)))

        except (ValueError, NameError, ZeroDivisionError, SyntaxError):
            logger.error("Conversion of '{0:s}' failed".format(str(val)))


def getBool(prompt, default=None):
    """
    Read a boolean from the terminal with checking.
    It will accept: yes / no , true / false in lower or upper case,
    1 / 0 or any logical expression.

    :param prompt: the prompt to be displayed.
    :type prompt: str
    :param default: default response (default to None)
    :type default: bool
    :return: bool True/False

    Note: if response is a string it will be evaluated.
    """
    while True:
        val = __getInput(prompt, default)
        try:
            if isinstance(val, bool):
                return val
            if isinstance(val, str):                      # if str
                bval = val.lower().strip()
                if bval.startswith("yes") or bval.startswith("true"):
                    return True
                if bval.startswith("no") or bval.startswith("false"):
                    return False

            val = eval(val)                        # do eval to for expression
            bval = bool(val)                       # Try and convert to bool
            return bval
        except:
            logger.error("Conversion of '{0:s}' to boolean failed".format(str(val)))


def getComplex(prompt, default=None, maxabs=None):
    """
    Read a complex from the terminal with optional default and range
    checking of the abs.

    :param prompt: the prompt to be displayed.
    :type prompt: str
    :param default: the default (may be None)
    :type default: complex
    :param maxabs: maximum abs value of complex accepted  (defaults to None)
    :type maxabs: float
    :return: complex in specified range (it will always return complex even if imaginary is zero)

    It will also try and convert from list or tuple, and evaluate strings.
    """
    if maxabs == None:
        maxabs = float("Inf")
    while True:
        val = __getInput(prompt, default)              # Get input
        try:                                          # Work out what happened
            if isinstance(val, str):              # If str eval what been given
                val = eval(val)
            if isinstance(val, list) or isinstance(val, tuple): # Convert from list or tuple if needed
                cval = complex(val[0], val[1])
            else:
                cval = complex(val)              # Convert to complex
            if abs(cval) <= maxabs:              # test range
                return cval
            else:
                logger.error("Abs value of '{0:s}' greater than '{1:6.3e}'".\
                             format(repr(cval), maxabs))

        except (ValueError, NameError, ZeroDivisionError, SyntaxError):
            logger.error("Conversion of '{0:s}' to Complex failed.".format(str(val)))


def getVector3d(prompt, default=None, maxabs=None):
    """
    Read a Vector3d from the terminal with checking.

    Format from terminal may be 'x,y,z'   OR   '[x,y,z]',  also each componet
    will be evaluated.

    :param prompt:  the prompt to be displayed
    :type prompt: str
    :param  default: the default value (may be None)
    :type default: Vector3d
    :param maxabs: abs max value of the Vector3d (defaults to None)
    :type maxabs: float
    :return: the set Vector3d

    Its also Tries to evaluate any sensible string as a Vector3d.
    """
    if maxabs == None:
        maxabs = float("Inf")
    while True:
        val = __getInput(prompt, default)
        try:
            if isinstance(val, str):          # Its a string
                val = eval(val)              # Eval list

            vec = Vector3d(val)

            if abs(vec) <= maxabs:
                return vec                  #  Success
            else:
                logger.error("Abs value of '{0:s}' greater than '{1:6.3e}'".\
                             format(repr(vec), maxabs))
        except (ValueError,NameError,ZeroDivisionError,SyntaxError):
            logger.error("Conversion of '{0:s}' to Vector3d failed.".format(str(val)))


def getUnit3d(prompt, default=None):
    """
    Read a Unit3d for the termial with checking. This will accapt and
    directon in any format accepted by Unit3d().parseAngle()

    Allowed formats

    * x,y,z or [x,y,z]   three floats
    * theta,psi or [theta,psi], in radians (quoted in "" for degrees)
    * theta in radians (or quotes in "" for degrees)

    :param prompt: the promp to be displayed
    :type prompt: str
    :param default: the default Unit3d
    :type: Unit3d
    """

    while True:
        val = __getInput(prompt, default)
        try:
            if isinstance(val, str):          # Its a string
                val = eval(val)              # Eval list
            u = Unit3d().parseAngle(val)
            return u
        except (ValueError, NameError, ZeroDivisionError, SyntaxError):
            logger.error("Conversion of '{0:s}' to Unit3d failed.".format(str(val)))


def getAngle(prompt, default=None):
    """
    Read a Angle in theta/psi fromat  the terminal with checking.

    Format from terminal may be 'theta,psi'   OR   '[theta,psi]',  also each componet will be evaluated.

    :param prompt: the prompt to be displayed
    :type prompt: str
    :param  default: the default value (may be None)
    :type default: Angle
    :return: the Angle (note will always return an Angle)

    Note: input values are in radians.

    """
    while True:
        val = __getInput(prompt, default)
        try:
            if isinstance(val, str):          # Its a string
                val = eval(val)              # Eval list

            return Angle(val)
        except (ValueError, NameError, ZeroDivisionError, SyntaxError):
            logger.error("Conversion of '{0:s}' to Angle failed.".format(str(val)))


def getAngleDegrees(prompt, default=None):
    """
    Read a Angle in theta/psi from the terminal in Degrees with checking.

    Format from terminal may be theta,psi   OR   '[theta,psi]',  also each componet will be evaluated.

    :param prompt: the prompt to be displayed
    :type prompt: str
    :param default: the default value (may be None), this is assumes to be in radians.
    :type default: Angle
    :return: the Angle (note will always return an Angle in radians)

    Note: input values are in degrees but the returned Angle values are in radians.

    """
    if default != None and isinstance(default, Angle):    # Convert to degree for default
        default = default.getDegrees()
    while True:
        val = __getInput(prompt, default)
        try:
            if isinstance(val, str):          # Its a string
                val = eval(val)              # Eval list

            return Angle().setDegrees(val)
        except (ValueError, NameError, ZeroDivisionError, SyntaxError):
            logger.error("Conversion of '{0:s}' to Angle failed.".format(str(val)))




def getVector2d(prompt, default = None, maxabs = None):
    """
    Read a Vector2d from the terminal with default and checking for the abs maximum.

    Format from terminal may be 'x,y'   OR   '[x,y]',  also each componet will be evaluated.

    :param prompt: the prompt to be displayed
    :type prompt: str
    :param default: the default value (may be None)
    :type default: Vector2d
    :param maxabs: maximum absolutle value of the Vector2d, (defaults to None)
    :type maxabs: float
    :return: a Vector2d in specified range.

    Note: strings will be evaluated to try and form a Vector2d.

    """
    #
    if maxabs == None:
        maxabs = float("Inf")
    while True:
        val = __getInput(prompt,default)
        try:
            if isinstance(val,str):          # Its a string
                val = eval(val)              # Eval list

            vec = Vector2d(val)

            if abs(vec) <= maxabs:
                return vec                  #  Success
            else:
                logger.error("Abs value of '{0:s}' greater than '{1:6.3e}'".\
                             format(repr(vec),maxabs))
        except (ValueError,NameError,ZeroDivisionError,SyntaxError):
            logger.error("Conversion of '{0:s}' to Vector2d failed.".format(str(val)))




def getExpandedFilename(name):
    """
    Method to expand filename and process environmental variable
    with $env or ~username prefix to a filename.

    :param name: with original name, assumed to contains NO leading white spaces
    :param type: str
    :return: the expanded filename as a str.

    Note this method does not prompt for input from the terminal.

    Updated to use the os.path.expanduser() and os.path.expandvars()
    so should work on Unix/MacOs and Windows.
    """

    name = p.expanduser(name)
    name = p.expandvars(name)
    return name



def getFilename(prompt, defaulttype = None, defaultname = None):
    """
    Method to get a filename with optional defaults. The name is also processed by getExpandedFilename
    to process environmental variable with $env or ~username prefix to a filename.

    :param prompt:  the prompt to be displayed
    :type prompt: str
    :param defaulttype: the default extension which will be added if not supplied, (default to None)
    :type defailttype: str
    :param defaultname: the default filename, (defaults to None)
    :type defaultname: str
    :return: the filename as a str which has been expanded to deal with logical names and username prefix.

    """
    val = getString(prompt,defaultname)
    filename = getExpandedFilename(val)                       # Expand to process env/user
    if defaulttype != None:
        defaultext = "." + defaulttype
        name,ext = p.splitext(filename)
        if ext != defaultext:
            filename += defaultext
    return filename


def openFile(prompt,key = "r",defaulttype = None, defaultname = None):
    """
    Method to open a text file with sanity checking, optional defaults and reprompt on failure.
    This is the main used callable function to open files.

    :param prompt:  the prompt to be displayed
    :type prompt: str
    :param key: the key passed to open, default is "r" (read)
    :type key: str
    :param defaulttype: the default extension which will be added if not supplied, (default to None)
    :type defailttype: str
    :param defaultname: the defaault filename, (defaults to None)
    :type defaultname: str
    :return: the the opened file descriptor.


    The file names is processded to expand environmental variable and user names\
    so for example $ENV/dir/file.data or ~user/dir/file.data are expanded

    """
    while True:
        filename = getFilename(prompt,defaulttype,defaultname)      # Get the filename
        try:
            filestream = open(filename,str(key))                  # try and open
            return filestream
        except IOError:
            logger.error("Failed to open file '{0:s}' with key '{1:s}'".\
                         format(filename,str(key)))


def tprint(*args):
    """
    Simply alternative to print that will print to the sysout and also to journal if there is a journal file open.
    Output to the journal file be prefixed with a comment character.

    :param args: argumemnt list  each will be conveterd to a str() and concatinated to a single string.

    Also newline will be appended if not present and the print buffer will be flushed.

    Note this should work identially in Pythons 2 and 3 since it uses direct write to output rather than print()

    """

    #               Form output string by appending str() of each argument
    string = ""
    for a in args:
        string += str(a)

    logger.info(string)
    if not string.endswith("\n"):       # Add automatic newline if needed
        string += "\n"

    #__tiooutput.write(string)           # Write string and flush output buffer
    #__tiooutput.flush()

    if __journalFile != None:           # Journal file open, so write string, but with prefix of "# "
        __journalFile.write(__tiocomment + " " + string)


#
#
def getOption(prompt,options,default = None):
    """
    Method to get a choice of options from a supplied list with error checking.

    :param prompt: the prompt to be displayed.
    :type prompt: str
    :param options:  the list of options assumed to be list of str.
    :type options: list
    :param default: the default option (int in range 0 -> < len(options)) (default to None)
    :type default: int
    :return: truple selected option, opt, so (opt,options[opt])

    Each option is tested for existance and uniquness. It will fail an re-prompt as required.
    There is also a simple internal 'help' option that pints the list of options.

    """
    if default == None:
        defaultOption = None
    else:
        if default >= 0 and default < len(options):
            defaultOption = options[default]
        else:
            defaultOption = None
    while True:
        val = getString(prompt,defaultOption)       # Get input
        #
        #                 Search for option (also check for uniquness)
        opt = -1
        i = 0
        for o in options:
            if o == val:                                    # Found unique option
                return i,options[i]
            if o.startswith(val):                            # found option
                if opt == -1:                                # first find
                    opt = i
                else:
                    opt = -2                                 # Not unique
            i += 1

        if opt >= 0:                                         # success, one found return
            return opt,options[opt]

        #
        #                Deal with help.
        if val.startswith("help") or val.startswith("HELP") :
            pl = ""
            for o in options:
                pl += " [{0:s}]".format(o)

            tprint("Options are : {0:s}".format(pl))
        elif opt == -1:                                     # Unknown option
            logger.error("Invalid option '{0:s}' help for list of options".\
                         format(str(val)))

        elif opt == -2:                                     # Non-unique option
            logger.error("Non-unique option '{0:s}' help for list of options".\
                         format(str(val)))


#
#
def __formatPrompt(prompt,default = None):
    """
    Internal method to format the prompt and add a default if included.
    """
    if default != None:                     # Add a default if given
        if isinstance(default,float):       # For float
            prompt += " (default : {0:5.3g}) : ".format(default)
        elif isinstance(default,int):       # for int
            if isinstance(default,bool):    # for bool (subclass of int)
                prompt += " (default : {0} ) : ".format(default)
            else:
                prompt += " (default : {0:d}) : ".format(default)
        elif isinstance(default,complex):   # For complex
            prompt += " (default : {0.real:5.3e} {0.imag:+5.3e}j) : ".\
                      format(default)
        else:                               # assume is string or obeys str
            prompt += " (default : {0:s}) : ".format(str(default))

    #             Add a " : " at end of there is not at least one ":"
    #
    if prompt.find(":") < 0 :
        prompt += " : "

    return prompt

#
#
def __getInput(prompt,default):
    """
    Internal method to get the response from the terminal and apply default if given.
    This method will strip comments denoted by #  but no other processing.

    This used a .readline() from a input stream and not input() or raw_input() so will work with both P2 and P3
    """
    p = __formatPrompt(prompt,default)
    #
    while True:
        try:
            val = input(p)                 # Use the Python 3 "input" method
            i = val.find(__tiocomment)     # is there a comment
            if (i >= 0):                   # comment found
                val = val[0:i]             # Kill comment
            val = val.strip()              # kill white space
            if val.startswith(__tioesc):   # process tio commands
                __tiocommand(val)
            elif len(val) > 0:
                break                      # have something valid
            else:
                if default != None:
                    val = default          # Take default
                    break
        except KeyboardInterrupt:
            logger.info("Exit Requsted.")
            sys.exit(0)

    if __journalFile != None:          # Journal to stream open
        __journalFile.write("{0:s}    # {1:s}\n".format(str(val),p))
    return val


#
#
def setJournal(filename = None):
    """
    Method of open / close a journal file that records prompts and commands typed to a text file.
    param filename string the name of the journal file, if None will close any current open journal file.

    :param filename: the name of the journal file, (defaults to None which switches off journal)
    :type filename: str

    This is elementary fucntion at the moment and may be expanded in scope.

    """
    global __journalFile

    if filename == None:             # No file give.
        if __journalFile != None:    # Close Journal file if open
            __journalFile.write(__tiocomment + "             closed at {0:s}\n".format(str(datetime.now())))
            __journalFile.close()
            __journalFile = None     # Null journal file
            tprint("tio.info: Journal off.")
        return                       # All finished

    #                                File given, so try and open it
    fn = getExpandedFilename(filename)
    if not fn.endswith("tio"):
        fn += ".tio"
    try:
        __journalFile = open(fn,"w")
        __journalFile.write("#             tio Journal file\n")
        __journalFile.write("#             opened at {0:s}\n".format(str(datetime.now())))
        tprint("tio.info: Journal on.")
    except IOError:
        __tioerr.write("setJournal.error: file open of {0:s} failed\n".format(fn))
        if getBool("Manually open journal file",False):
            __journalFile = openFile("Journal File","w","tio")
        else:
            __journalFile = None

#
#
def __tiocommand(cmd):
    """ Internal command handler, limited use at the moment, but will be expanded
    """
    cmd = cmd[1:].strip()                # Remove % and clean up
    if cmd.lower().startswith("beep"):   # Output a beep to the terminal
        __tiooutput.write("\a")
    elif cmd.startswith("exit"):         # Exit quitely
        logger.info("Exit requested.")
        sys.exit(0)
    elif cmd.lower().startswith("journal"):   # Open a journal file
        tokens = cmd.split()
        filename = tokens[1].strip()
        setJournal(filename)
    elif cmd.lower().startswith("nojournal"):  # Close the journal file
        setJournal()
    elif cmd.lower().startswith("dir"):     # Add directory
        tokens = cmd.split()                # Break into tokens
        if len(tokens) < 2:                 # if no directory, then current
            d = ""
            fulldir = "."
        else:
            d = tokens[1].strip()            # Extract directory name
            fulldir = getExpandedFilename(d) # expand name if starts with $ or ~
            if not d.endswith("/"):          # Add "/" to name if needed
                d += "/"
        try:
            for filename in listdir(fulldir):  # get directory list and process
                if not filename.endswith("~"): # Ignore backup files
                    tprint(d,filename)
        except OSError :                      # Catch error of not directory
            tprint("Unknown directory : ",d)

    else:
        __tioerr.write("toi.command error: unknown command {0:s}, ignored.\n".format(cmd))


