Block C++ API
=============

C++ Module Structure
--------------------

The setup and execute functions in C++ modules should be enclosed in ``extern "C" { ... }`` to enable cosmosis to fund them.

Here's an example module:

.. code-block:: c++


    #include "cosmosis/datablock/datablock.hh"
    #include "cosmosis/datablock/section_names.h"
    

    extern "C" {
    void * setup(DataBlock * options)
    {
        // Read options from the CosmoSIS configuration ini file,
        // passed via the "options" argument

        // Record any configuration information required

        // Pass back any object you like
    }

    DATABLOCK_STATUS execute(DataBlock * block, void * config)
    {
        // Config is whatever you returned from setup above
        // Block is the collection of parameters and calculations for
        // this set of cosmological parameters

        DATABLOCK_STATUS status = 0;

        return status;
    }
    }



Getters
-------

The DataBlock class that you get passed in the setup and execute functions has methods for loading and saving data.

``get_val`` is a template method that gets (i.e. reads/loads) any kind of object from the data block, depending on the type of value. You can optionally also supply a default value:

.. code-block:: c++

    // get functions return the status, and set the value of their
    // output argument only upon success.

    template <class T>
    DATABLOCK_STATUS 
    DataBlock::get_val(std::string section,
                       std::string name,
                       T& val);

    template <class T>
    DATABLOCK_STATUS 
    DataBlock::get_val(std::string section,
                       std::string name,
                       T const& def,
                       T& val);

Setters
-------

``put_val`` is a template method that puts (i.e. writes/saves) any kind of object into the data block, depending on the type of value:

.. code-block:: c++

    template <class T>
    DATABLOCK_STATUS 
    DataBlock::put_val(std::string section,
                       std::string name,
                       T const& val);

Replacers
---------

replace_val replaces (overwrites) an existing object in the data block:

.. code-block:: c++

    template <class T>
    DATABLOCK_STATUS 
    DataBlock::replace_val(std::string section,
                           std::string name,
                           T const& val);

Data Types
----------

The data types T for any of these methods can be any of::


    int
    double
    std::string
    std::complex<double>
    std::vector<int>
    std::vector<double>
    std::vector<std::string>
    std::vector<std::complex<double>>
    cosmosis::ndarray<int>
    cosmosis::ndarray<double>
    cosmosis::ndarray<std::complex>

Array data types are done using the std::vector types above. There are C++ standard library types for arrays.

Multidimensional arrays are done using the cosmosis::ndarray.


Introspection
-------------

These methods check what is in the data block

.. code-block:: c++

    // Return true if the datablock has a value in the given
    // section with the given name, and false otherwise.
    bool has_val(std::string section,
                 std::string name) const;

    // Return -1 if no parameter of the given name in the given section
    // is found, or if the parameter is not an array. Return -2 if the
    // length of the array is larger than MAXINT. Otherwise, return the
    // length of the array.
    int get_size(std::string section,
                 std::string name) const;


    // Return true if the DataBlock has a section with the given name.
    bool has_section(std::string name) const;

    // Return the extents of the array of the given name in the given
    // section. If the found item is actually an array carrying the
    // right fundamental data type, return DBS_SUCCESS and fill in
    // extents. If no object is found, or if the object is not an array,
    // return an error status, and do no modify extents.
    template <class T>
    DATABLOCK_STATUS get_array_shape(std::string section,
                                     std::string name,
                                     std::vector<std::size_t>& extents);

    // Get the type, if any, of the named object. The types are
    // identified by the enumeration type datablock_type_t. Returns
    // DBS_SUCCESS if found.
    DATABLOCK_STATUS get_type(std::string section,
                              std::string name,
                              datablock_type_t& t) const;
