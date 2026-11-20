Tutorial 1: Computing a single cosmology likelihood
---------------------------------------------------

This tutorial uses the CosmoSIS standard library, and an example in it, to show
you how to compute a likelihood using CosmoSIS.


Installation
============

Before you start, :doc:`follow the instructions to install cosmosis </intro/installation>`.  Once you are complete, you should be able to run::

    cosmosis --help

and see a usage message.

These tutorials are in the CosmoSIS standard library, and should be run from that directory.

Parameter files
============================

Have a look at the file :code:`examples/planck/planck.ini`.  CosmoSIS is always run on a single parameter file like this.  It specifies how to construct a pipeline that generates a likelihood, and what to do with that likelihood once it is calculated.  

CosmoSIS parameter files use the :code:`ini` format, which has section names with square brackets around them and parameters specified with an equals sign.  This example says there is a section called :code:`runtime` with a parameter named :code:`sampler` with the values "test"::


    [runtime]
    sampler = test

Each CosmoSIS run uses at least two ini files, this one, called a parameter file, and a second *values* file, specifying the cosmological and other varied parameters used in the pipeline.  In this case the values file is :code:`examples/planck/planck_values.ini`.

Running CosmoSIS on a parameter file
=====================================


Run CosmoSIS on this parameter file with this command::

    cosmosis examples/planck/planck.ini

You will see a lot of output showing:

* What parameters are used in this pipeline, e.g. ::

    Parameter Priors
    ----------------
    planck--a_planck                      ~ delta(1.0)
    cosmological_parameters--h0           ~ delta(0.6726)
    cosmological_parameters--omega_m      ~ delta(0.3141)
    ...


* The set-up phase for each step (module) in the calculation, e.g.::

        -- Setting up module camb --
    Looking for clik Planck likelihood file 1: likelihood/planck2018/baseline/plc_3.0/hi_l/plik/plik_rd12_HM_v22b_TTTEEE.clik

     ...


* The sampler that is being run::

    ****************************
    * Running sampler 1/1: test
    ****************************

* The output of each module, e.g.::

    Running camb ...
    Reion redshift       =  11.751
    Integrated opt depth =  0.0800
    Om_b h^2             =  0.018096
    Om_c h^2             =  0.123356
    Om_nu h^2            =  0.000644
    ...

Outputs
=======

At the end of the pipeline the code will print out the likelihood of the Planck 2018 data given the chosen parameters.

It will also save a directory ``output/planck`` full of all the quantities it calculated throughout the pipeline.  You can explore that to learn more about the specific calculations done in the pipeline.


Defining a sampler
===================

The first lines in the parameter file :code:`examples/planck/planck.ini` are::

    [runtime]
    sampler = test
    root = .

    [test]
    save_dir=output/planck
    fatal_errors=T

The first option, :code:`sampler`, tells CosmoSIS what it should do with the likelihood that we will construct - how the parameter space should be explored.

CosmoSIS has lots of different samplers in it, designed to move around parameter spaces in different ways.  The :code:`test` sampler is the simplest possible one: it doesn't move around the parameter space at all - it just computes a likelihood (runs the pipeline) for a single set of values.  These tutorials will discuss several samplers; the full list is described in :doc:`the samplers page </usage/samplers>`.

Once you have chosen a sampler you configure that sampler with the second section shown in above, which has the name of the sampler, in this case :code:`test`.

Defining a pipeline
===================

Cosmological analyses use a *Likelihood Function* - the probability of the observed data given some cosmological model and parameters.  In realistic cosmological problems these are usually long calculations with many parts.

In CosmoSIS you build a likelihood function from a sequence of *modules*.  Each module does a different piece of the calculation, often modelling different pieces of physics and different observed data sets.  You need to understand the calculation you are trying to do to build a CosmoSIS pipelines, and then put together the ingredients that it needs.

The pipeline is defined in the parameter file like this::

    [pipeline]
    ; these names refer to sections later in the file:
    modules = consistency camb planck


This tells CosmoSIS to run three modules; as the comment says, each module listed is defined later in the file.  For example, the :code:`planck` module is specified futher down like this::

    [planck]
    file = likelihood/planck2018/planck_interface.so
    data_1 = %(planck_path)s/hi_l/plik/plik_rd12_HM_v22b_TTTEEE.clik
    ...

The :code:`file` option, which all modules must have, tells CosmoSIS where to find the file containing the code of this module. The other two options, :code:`data_1` and :code:`data_2` are passed to the module during setup, which in this cases uses them to select data files.

The modules in this example are all part of the CosmoSIS Standard Library.  For your own analyses you could mix standard library modules with your own steps.  We have a list of all the standard library modules and their options, inputs, and outputs in the standard library reference.

Defining input values
======================

The pipeline we have built is a machine for turning a collection of numerical parameters into a single total likelihood.  We need some initial input values for the first module to take in::


    [pipeline]
    ...
    values = examples/planck/planck_values.ini

This option points to the values file, the second cosmosis ini file.  The values file contains all the inputs that are passed to the pipeline.  For example::

    [cosmological_parameters]
    h0 = 0.6726       ;H0 (km/s/Mpc)/100.0km/s/Mpc 
    omega_m = 0.3141  ;density fraction for matter today
    omega_b = 0.04    ;density fraction for baryons today
    omega_k = 0.0     ;spatial curvature

This creates a category of parameters called :code:`cosmological_parameters` and within that a collection of named values.  The semi-colons begin comments.

Parameters can either have a fixed value, like the ones above, or they can have a range, like this::

    [cosmological_parameters]
    h0 = 0.6   0.6726   0.8

This doesn't make any difference for the test sampler, because it just uses the one central value.  But if you are sampling, as in the next tutorial, then that is the range that the parameters can take.

