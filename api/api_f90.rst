Block Fortran API
=================

We do not condone the use of Fortran for new projects.

Module Structure
----------------

Fortran setup and execute functions cannot be inside a fortran module.

.. code-block:: fortran

    function setup(options) result(result)
        use cosmosis_modules
        implicit none
        integer(cosmosis_block), value :: options
        integer(cosmosis_status) :: status
        type(my_settings), pointer :: settings
        type(c_ptr) :: result

        !Make space for the configuration
        allocate(settings)

        !example: get an option from the section for this module.
        !we are assuming that the settings type has a my_option field in.
        status = datablock_get_int(options, option_section, "my_option", settings%my_option)

        if (status .ne. 0) then
            write(*,*) "Please set the option called 'my_option' in the ini file for my wonderful module"
            stop
        endif

        !Convert to the form that CosmoSIS needs.
        !c_loc is a built-in fortran function (in the iso_c_binding built-in module)
        !which converts from a Fortran pointer to a C pointer that python can understand.
        result = c_loc(settings)
    end function setup

    function execute(block, config) result(status)
        use cosmosis_modules

        implicit none
        integer(cosmosis_block), value :: block
        integer(cosmosis_status) :: status
        type(c_ptr), value :: config
        type(my_settings), pointer :: settings  

        call c_f_pointer(config, settings)

        return status

    end function execute

Types
-----

The functions below use these types:


.. code-block:: fortran

    integer(cosmosis_status) :: status
    integer(cosmosis_block) :: block
    character(*) :: section
    character(*) :: name

and:

.. code-block:: fortran

    integer :: value  ! For the "int" functions
    logical :: value  ! For the "logical" functions
    real(c_double) :: value  ! For the "double" functions. This is the same as real(8).
    complex(c_double_complex) :: value  ! For the "complex" functions
    character(len=*) :: value ! For the "string" functions


Getters
-------

.. code-block:: fortran

    datablock_get_int(block, section, name, value) result(status)
    datablock_get_double(block, section, name, value) result(status)
    datablock_get_complex(block, section, name, value) result(status)
    datablock_get_string(block, section, name, value) result(status)

    datablock_get_int_default(block, section, name, default, value) result(status)
    datablock_get_double_default(block, section, name, default, value) result(status)
    datablock_get_complex_default(block, section, name, default, value) result(status)
    datablock_get_string_default(block, section, name, default, value) result(status)


Array Getters
-------------

.. code-block:: fortran

    datablock_get_int_array_1d(block, section, name, value, size) result(status)
    datablock_get_double_array_1d(block, section, name, value, size) result(status)


Setters
-------

.. code-block:: fortran

    datablock_put_int(block, section, name, value) result(status)
    datablock_put_double(block, section, name, value) result(status)
    datablock_put_complex(block, section, name, value) result(status)
    datablock_put_string(block, section, name, value) result(status)

Array Setters
-------------

.. code-block:: fortran

    datablock_put_int_array_1d(block, section, name, value) result(status)
    datablock_put_double_array_1d(block, section, name, value) result(status)
    datablock_put_double_array_2d(block, section, name, value) result(status)


Grids
-----

A particularly common pattern in cosmology is a 2D grid where you have a function of two variables, for example P(k,z) where k and z are 1D arrays of size nk and nz, and P is a 2D array of size nk,nz.

There are specialized functions for this scenario:

.. code-block:: fortran

    datablock_put_double_grid(s, section, x_name, x, y_name, y, z_name, z) result(status)
    datablock_get_double_grid(s, section, x_name, x, y_name, y, z_name, z) result(status)
    datablock_put_double_grids(s, section, x_name, x, y_name, y, z1_name, z1, z2_name, z2,  ..., z10_name, z10) result(status)

In the latter case multiple grids on the same axes are saved; all the grids after the first are optional. This code automatically takes care of the grid ordering - z will be allocated with size nx,ny regardless of how it was originally saved.
