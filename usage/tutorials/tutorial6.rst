Tutorial 6: Writing new modules
===============================

So far we've used modules from the CosmoSIS standard library to build our pipeline.  This works fine for many projects, where using or modifying the standard library will be enough.  But we can go further by creating entirely new modules to calculate new observables or include new physics effects in them.


Pipelines & Modules
-------------------

CosmoSIS modules are isolated from each other - all the calculations done by a module are stored in a DataBlock, which is passed through the list of modules in the pipeline.  Each module reads what previous modules have done, performs its own calculations, and then adds these to the pipeline.

Typically, a pipeline is run many times on different sets of input parameters, for an example in an MCMC.

Module requirements
-------------------

CosmoSIS modules can be written in C, C++, Fortran, Python, or (experimentally) Julia.

In each of these languages the structure of the file you write is the same: you write functions with specific names.  Two of these are required, and one is optional::

    setup(options)
    # Takes the information from the parameter file as a DataBlock and configures the module.
    # This is called once, when the pipeline is created.

    execute(block, config)
    # Takes a DataBlock (see below) from the values file and any preivous pipeline, and runs the module.
    # This is called for each set of parameters the pipeline is run on.

    cleanup(config)
    # (Optional) frees memory allocated in the setup function
    # This is run once, when the pipeline is deallocated.
    # We will skip it in this tutorial, as it is rarely needed in python.


Writing our new module
----------------------

Let's write our new module in Python, since that's usually much easier.

Make a new file.  You can put it anywhere, but to keep things organized it's usally better to keep your work separate from the existing standard library.

In that file, put these lines, which represent an empty but runnable CosmoSIS module::

    from cosmosis.datablock import names, option_section

    def setup(options):
        return {}

    def execute(block, config):
        return 0

The Setup Function
------------------

The ``setup`` function is run once per chain, at the beginning of the analysis. It reads options from the parameter file, and then performs any setup required.  For example, it might load some data from files, pre-compute some important values, or just keep a list of all the settings for later.

The ``option`` argument is an instance of a CosmoSIS DataBlock, containing everything specified in the parameter file. The setup function typically reads from it like this::

    x = options[option_section, "name_of_option"]
    # or, for value with a fallback option in case it is not set:
    y = options.get_int(option_section, "name_of_int_option", default=4)

For a full list of the ``get`` functions see the :doc:`Block Python API</api/api_python>`.

The constant ``option_section`` just refers to the section of the datablock that generated this module.  Usually you will want to use it.

The ``setup`` function can return any object you like; you can use whatever is the most convenient way to store the configuration for your module.  For example, you could return a dictionary, list, or an instance of a class.  Whatever object you return will be passed back to the ``execute`` function later when it is called.

The Execute Function
--------------------

``execute`` is the main worker function of a module. It is called for each new set of values that the (MCMC) sampler generates.  The execute functions of all the modules in the pipeline are called one by one, in order, with a single datablock passed from one to the next.  Each module reads values from the block (put there either by the sampler or previous modules), does some calculations, and then puts its own values in the block.

The second argument, ``config``, is whatever the ``setup`` function returns.

For example, here is an execute function that calculates ``D_V``, a distance measure used in BAO studies::

    # Some values from previous modules
    z = block["distances", "z"]
    d_a = block["distances", "D_A"]
    H = block["distances", "H"]

    # Some constants
    c = 1.0

    # compute something derived from the inputs
    d_v = ((1.0+z)**2 * c * z * d_a**2 / H )**(1./3.)

    block["distances", "d_v"] = d_v

The full list of methods that a block can run is discussed on the :doc:`Block Python API </api/api_python>` page.

You can explore what the previous pipeline has put in the block either by running the pipeline with the test sampler and exploring the saved directory from the block, by using the ``block.keys()`` method, or by reading the documentation for the module on the :doc:`Standard Library Overview </usage/standard_library_overview>` page.

Execute functions should return ``0`` if the succeeded and any non-zero integer if they failed for any reason.



Likelihood modules
------------------

Likelihoods are implemented in cosmosis just as another kind of module, but they should put the value of a log-likelihood the "likelihoods" section of the block::

    block["likelihoods", "my_like"] = -0.5 * (x - mu)**2 / sigma**2

If your likelihood is a Gaussian you can inherit from ``cosmosis.GaussianLikelihood`` and override some of the methods there.  See  `the Gaussian Likelihood class here <https://github.com/cosmosis-developers/cosmosis/blob/main/cosmosis/gaussian_likelihood.py>`_  for details; you would usually only have to override the methods ``extract_theory_points``, ``build_data`` and ``build_covariance``.



