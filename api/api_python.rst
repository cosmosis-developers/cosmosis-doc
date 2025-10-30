Block Python API
****************

This page describes how to use CosmoSIS DataBlocks in Python modules.

Overview
--------
**class cosmosis.datablock.DataBlock**

  A map of (section,name)->value of parameters.

  At the heart of Cosmosis is a data-containing object which is passed
  down a pipeline of processing stages, which shape and massage those
  data as they go through.

  The DataBlock methods are described below.

Getting Values
--------------

The main way to get values in python is to use the usual python lookup syntax::

    value = block[section, name]

This will give you an object whatever type was in the datablock.  The usual reason
for using the alternative methods below is to be extra certain about the type of
data, and to raise an error if the wrong type is provided.

These methods raise ``BlockError`` if no value or the wrong type is found.

When a ``default`` parameter is supplied, that value will also be put in the
datablock.


**get(section, name)**

    Get the value of parameter with *name* in *section*.


**get_int(section, name, default=None)**

    Retrieve an integer value from the parameter set.


**get_double(section, name, default=None)**

    Retrieve a floating-point value from the parameter set.


**get_bool(section, name, default=None)**

    Retrieve a boolean value from the parameter set.


**get_string(section, name, default=None)**

    Retrieve a string value from the parameter set.


**get_complex(section, name, default=None)**

    Retrieve a complex value from the parameter set.


**get_double_array_1d(section, name)**

    Retrieve a floating-point array from the parameter set.


**get_double_array_nd(section, name)**

    Get a floating-point array of *a priori* unspecified shape.


**get_int_array_1d(section, name)**

    Retrieve an integer array from the parameter set.


**get_int_array_nd(section, name)**

    Get an integer-valued array of *a priori* unspecified shape.

**get_string_array_1d(section, name)**

    Retrieve an array of strings from the datablock.




Setting Values
--------------

The usual way to set a value in the block is simply::

    block[section, name] = x

The methods below give more fine-grained type control.  The square
brackets method above will also replace existing values, but the replacement must
be of the same type as the existing.  The methods below do not allow replacement.


**put(section, name, value)**

    Add a parameter with *value* at (*section*, *name*) in the map.


**put_bool(section, name, value)**

    Add a boolean parameter to the map.


**put_complex(section, name, value)**

    Add a complex parameter to the map.


**put_double(section, name, value)**

    Add a floating-point parameter to the map.


**put_double_array_1d(section, name, value)**

    Add a one-dimensional floating-point array to the map.


**put_double_array_nd(section, name, value)**

    Add a floating-point array parameter to the data set.


**put_int(section, name, value)**

    Add an integer parameter to the map.


**put_int_array_1d(section, name, value)**

    Add a one-dimensional integer array to the map.


**put_int_array_nd(section, name, value)**

    Add any integer array parameter to the data set.


**put_string(section, name, value)**

    Add a string parameter to the map.


**put_string_array_1d(section, name, value)**

Add a one-dimensional string array to the map.



Replacing Values
-----------------

As noted above, the usual way to replace block values is the square bracket approach, e.g.::

    block[section, name] = 2 * block[section, name]

The methods below allow more fine-grained control.  A BlockError is raised if types change.

**replace(section, name, value)**

    Replace the value of a parameter at (*section*, *name*) in the map with *value*.


**replace_bool(section, name, value)**

    Change the value of a boolean parameter in the map.


**replace_complex(section, name, value)**

    Change the value of a complex parameter in the map.


**replace_double(section, name, value)**

    Change the value of a floating-point parameter in the map.


**replace_double_array_1d(section, name, value)**

    Replace the value of a parameter with a simple floating-point array.


**replace_double_array_nd(section, name, value)**

    Replace a floating-point array parameter in the data set.


**replace_int(section, name, value)**

    Change the value of an integer parameter in the map.


**replace_int_array_1d(section, name, value)**

    Replace the value of a parameter with a simple integer array.


**replace_int_array_nd(section, name, value)**

    Replace an integer array parameter in the data set.


**replace_string(section, name, value)**

    Change the value of a string parameter in the map.


**replace_string_array_1d(section, name, value)**

    Replacing string arrays is not yet implemented



Grids
-----

Here, *grids* are sets of three values, two 1D arrays *x* and *y*, and a 2D array *z*,
of shape *(nx, ny)*.  Usually grids are used where *z* is a function of *x* and *y*
sampled on a rectangular grid.


**put_grid(section, name_x, x, name_y, y, name_z, z)**

    Put a grid into the map.  This checks the sizes of the given arrays.


**get_grid(section, name_x, name_y, name_z)**

    Return a triple of arrays x, y, z.  If the grid was originally added
    in the other order (with x and y swapped) then this will transpose
    the returned *z* to make things correct.


**replace_grid(section, name_x, x, name_y, y, name_z, z)**

    Replace a grid in the map.


Querying
--------

These methods can be used to query what is in a datablock, for instance
to perform different calculations depending on what variables are available,
or to perform optional calculations.


**has_section(section)**

    Indicate whether or not there is a given *section* in the data set.

**has_value(section, name)**

    Indicate whether or not a parameter is in the map.

**keys(section=None)**

    Return all keys in the block, or, if *section* is specified, all keys under that section.

    In all cases a list of pairs of strings will be returned, the
    elements of each being the *section* and name of each parameter.

**sections()**

    Return a list of strings with the names of all sections in the data set.


Logging
-------

The DataBlock keeps a log of all operations performed on it, to help debugging.
These methods can be used to view that log.

**get_log_count()**

    Return the number of entries in the log.

**get_log_entry(i)**

    Get the iʼth log entry as a tuple of four strings indicating the verb (i.e.,
    logged action), section and name of the parameter, and the data
    type held by the parameter.


**get_first_parameter_use(params_of_interest)**

    Analyze the log and figure out when each parameter supplied is first used
    by a module.

**log_access(log_type, section, name)**

    Add an entry to the end of this ``DataBlock`` access log.

    The *log_type* describes the action performed on the parameter at
    (*section*, *name*).  It should be one of the strings displayed in
    *datablock_logging.cc*, viz: “READ-OK”, “WRITE-OK”, “READ-FAIL”,
    “WRITE-FAIL”, “READ-DEFAULT”, “REPLACE-OK”, “REPLACE-FAIL”,
    “CLEAR”, “DELETE”, or “MODULE-START”.

**print_log()**

    Dump a human-readable list of log entries to standard output.

    If you are running a jupyter notebook this may end up on the
    command line of the notebook code instead of the screen.

**report_failures()**

    Dump a human-readable list of failed-action log entries to the standard error channel.

    If you are running a jupyter notebook this may end up on the
    command line of the notebook code instead of the screen.


Metadata
--------

*DEPRECATED*

**get_metadata(section, name, key)**

    Get the metadata called *key* attached to parameter *name* under *section*.

**put_metadata(section, name, key, value)**

    Associate *value* with the meta-*key* attached to parameter *name* under *section*.


**replace_metadata(section, name, key, value)**

    Associate *value* with the meta-*key* attached to parameter *name* under *section*.


Life Cycle and I/O
-------------------

In normal operation CosmoSIS handles block life cycle for you; when you are writing modules
you don't need to know anything about this.  But it can be useful for debugging or when
using CosmoSIS as a library.

**clone()**

    Make a brand-new, completely independent object, a deep copy of the existing one.


**save_to_directory(dirname, clobber=False)**

    Save the entire contents of this parameter map in the filesystem under *dirname*.

    The data are all written out long-hand in ASCII.  Each unique
    section will go to its own sub-directory, in which all the
    scalar parameters in that section go into a single file
    (‘values.txt’), and array data each go into their
    own file, named after the parameter key.

    The path, including *dirname*, will be created if necessary.

**save_to_file(dirname, clobber=False)**

    Effectively ``save_to_directory()`` with the result tarʼd and compressed to a single file.

    The *dirname* argument here is actually a file name without an
    extension; the path to the file will be created in the file system
    if necessary (``ValueError`` will be raised if this cannot be
    accomplished), and “.tgz” will be appended to the file name.
