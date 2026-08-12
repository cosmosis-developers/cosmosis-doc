Block C API
===========

Include the header ``cosmosis/datablock/c_datablock.h`` (relative to the include directory ``${COSMOSIS_SRC_DIR}``) to write cosmosis modules in C.  

The following functions are available to write modules in C.  The return type DATABLOCK_STATUS is an enum; 0 represents success.

C Module Structure
------------------

Here is an example of a module structure in C.

.. code-block:: c

    #include "cosmosis/datablock/c_datablock.h"
    #include "cosmosis/datablock/section_names.h"


    void * setup(c_datablock * options)
    {


        // Read options from the CosmoSIS configuration ini file,
        // passed via the "options" argument
        int status = 0;
        status |= c_datablock_get_double(options, OPTION_SECTION, "mode", &mode);

        if (status){
            fprintf(stderr, "Please specify a mode in the CosmoSIS configuration ini file.\n");
            exit(status);
        }
        // Record any configuration information required
        struct my_config * config = malloc(sizeof(struct my_config));
        config->mode = mode;
        // Pass back any object you like
        return config
    }

    int execute(c_datablock * block, void * config)
    {

        // Config is whatever you returned from setup above
        // Block is the collection of parameters and calculations for
        // this set of cosmological parameters
        int status = 0;
        int mode = config->mode;

        double w,omega_m;
        status |= c_datablock_get_double(block, cosmo, "w", &w);
        status |= c_datablock_get_double(block, cosmo, "omega_m", &omega_m);

        result = my_function(omega_m,w);
        //save to datablock
        status |= c_datablock_put_double(block, like, "MY_FUNCTION_LIKE", result);

        return status;
    }


Getters
-------

.. code-block:: c

    DATABLOCK_STATUS
    c_datablock_get_int(c_datablock* s, const char* section, const char* name, int* val);

    DATABLOCK_STATUS
    c_datablock_get_bool(c_datablock* s, const char* section, const char* name, bool* val);

    DATABLOCK_STATUS
    c_datablock_get_double(c_datablock* s, const char* section, const char* name, double* val);

    DATABLOCK_STATUS
    c_datablock_get_complex(c_datablock* s, const char* section, const char* name, double _Complex* val);

    DATABLOCK_STATUS
    c_datablock_get_string(c_datablock* s, const char* section, const char* name, char** val);


Getters with defaults
---------------------

.. code-block:: c

    DATABLOCK_STATUS
    c_datablock_get_int_default(c_datablock* s, const char* section, const char* name, int def, int* val);

    DATABLOCK_STATUS
    c_datablock_get_bool_default(c_datablock* s, const char* section, const char* name, bool def, bool* val);

    DATABLOCK_STATUS
    c_datablock_get_double_default(c_datablock* s, const char* section, const char* name, double def, double* val);

    DATABLOCK_STATUS
    c_datablock_get_string_default(c_datablock* s, const char* section, const char* name, const char* def, char** val);

    DATABLOCK_STATUS
    c_datablock_get_complex_default(c_datablock* s, const char* section, const char* name, double _Complex def,double _Complex* val);

Array getters
-------------

If you want CosmoSIS to malloc the array for you and also return the size:

.. code-block:: c

    DATABLOCK_STATUS
    c_datablock_get_int_array_1d(c_datablock* s, const char* section, const char* name, int** val, int* size);

    DATABLOCK_STATUS
    c_datablock_get_double_array_1d(c_datablock* s, const char* section, const char* name, double** val, int* size);

    DATABLOCK_STATUS
    c_datablock_get_complex_array_1d(c_datablock* s, const char* section, const char* name, double _Complex** val, int* size);

Or if you already know the size:

.. code-block:: c

    DATABLOCK_STATUS
    c_datablock_get_int_array_1d_preallocated(c_datablock* s, const char* section, const char* name, int* array, int* size, int maxsize);

    DATABLOCK_STATUS
    c_datablock_get_double_array_1d_preallocated(c_datablock* s, const char* section, const char* name, double* array, int* size, int maxsize);

    DATABLOCK_STATUS
    c_datablock_get_complex_array_1d_preallocated(c_datablock* s, const char* section, const char* name, double _Complex* array, int* size, int maxsize);


Setters
--------

In C you don't use setter functions to modify existing values, just to add new ones. See Replacers below for the former.

.. code-block:: c

    DATABLOCK_STATUS
    c_datablock_put_int(c_datablock* s, const char* section, const char* name, int val);

    DATABLOCK_STATUS
    c_datablock_put_bool(c_datablock* s, const char* section, const char* name, bool val);

    DATABLOCK_STATUS
    c_datablock_put_double(c_datablock* s, const char* section, const char* name, double val);

    DATABLOCK_STATUS
    c_datablock_put_complex(c_datablock* s, const char* section, const char* name, double _Complex val);

    DATABLOCK_STATUS
    c_datablock_put_string(c_datablock* s, const char* section, const char* name, const char* val);


Array Setters
--------------


.. code-block:: c

    DATABLOCK_STATUS
    c_datablock_put_int_array_1d(c_datablock* s, const char* section, const char* name, int const*  val, int sz);

    DATABLOCK_STATUS
    c_datablock_put_double_array_1d(c_datablock* s, const char* section, const char* name, double const*  val, int sz);

    DATABLOCK_STATUS
    c_datablock_put_complex_array_1d(c_datablock* s, const char* section, const char* name, double _Complex const*  val, int sz);


Replacers
---------
These replace an existing value. Must be the same type.

.. code-block:: c

    DATABLOCK_STATUS
    c_datablock_replace_int(c_datablock* s, const char* section, const char* name, int val);

    DATABLOCK_STATUS
    c_datablock_replace_bool(c_datablock* s, const char* section, const char* name, bool val);

    DATABLOCK_STATUS
    c_datablock_replace_double(c_datablock* s, const char* section, const char* name, double val);

    DATABLOCK_STATUS
    c_datablock_replace_complex(c_datablock* s, const char* section, const char* name, double _Complex val);

    DATABLOCK_STATUS
    c_datablock_replace_string(c_datablock* s, const char* section, const char* name, const char* val);

Array Replacers
---------------

.. code-block:: c

  DATABLOCK_STATUS
  c_datablock_replace_int_array_1d(c_datablock* s, const char* section, const char* name, int const* val, int sz);

  DATABLOCK_STATUS
  c_datablock_replace_double_array_1d(c_datablock* s, const char* section, const char* name, double const* val, int sz);

  DATABLOCK_STATUS
  c_datablock_replace_complex_array_1d(c_datablock* s, const char* section, const char* name, double _Complex const* val, int sz);