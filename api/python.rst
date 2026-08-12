Calling CosmoSIS from Python
===============================

You can run CosmoSIS on the command line, but you can also call it from
Python code. This is useful if you want to run multiple CosmoSIS
instances in a loop, or if you want to integrate CosmoSIS into a larger
Python application.

This page lists the main functions and classes you can use from scripts.

Top-Level Usage with ``run_cosmosis``
--------------------------------------

The simplest way to run CosmoSIS from Python is to use the
``run_cosmosis`` function. 


.. code-block:: python

    from cosmosis import run_cosmosis
    # This is equivalent to running `cosmosis params.ini` on the command line:
    run_cosmosis("params.ini")

The most useful additional arguments to ``run_cosmosis`` are ``override``, which
lets you replace parameters in the ini file, ``variables``, which lets you
replace contents of the values file. 

You can also specify ``output="astropy"`` to get the results back as an
Astropy Table.

.. documentation of the run cosmosis function:

.. autofunction:: cosmosis.run_cosmosis


Classes for custom usage
----------------------------

Other classes that may be particularly useful 
- ``LikelihoodPipeline`` - for building and running custom pipelines
- ``DataBlock`` - for storing and playing with theory predictions from pipelines

.. autoclass:: cosmosis.LikelihoodPipeline
   :members:

.. autoclass:: cosmosis.datablock.DataBlock
    :members:


