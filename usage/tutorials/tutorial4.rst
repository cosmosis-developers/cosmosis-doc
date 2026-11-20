Tutorial 4: Building new pipelines
----------------------------------

In CosmoSIS a *pipeline* is a sequence of *modules* that computes one or more *likelihoods*.

You can build a new pipeline or modify an existing one by choosing which modules to include in the pipeline, and by selecting their configuration.

Extending a calculation by adding modules
=========================================

To know which module to add you have to understand the calculation you want to perform, and make sure that all the necessary calculations for it are done at some point in the pipeline.
You can add modules into the middle of an existing pipeline, or at the end.

Adding the new module
=====================

In the :code:`[pipeline]` section of :code:`examples/planck/planck.ini` you will find::

    [pipeline]
    modules = consistency camb planck


Let's modify this pipeline, by adding the BOSS DR12 Baryon Acoustic Oscillation measurement.  We can consult the
:doc:`standard library overview page <../standard_library_overview>` for likelihoods we can include, and the :doc:`BOSS DR12 page <../../reference/standard_library/boss_dr12>` for more details.

The latter page lists the file we should use for this module::

    File: likelihood/boss_dr12/boss_dr12.py

This means that we make a new section in the parameter file that we are using, with this information in.  We can add new text to the bottom of :code:`examples/planck/planck.ini`::

    [boss]
    file = likelihood/boss_dr12/boss_dr12.py

Configuring the module
======================

The wiki page also tells us what parameters we can use to configure the pipeline, and what inputs the likelihood will need.  The parameters all have default choices, so nothing is mandatory, but we can make some choices.  The main one is to choose which kind of likelihood to use:

    mode    0 for BAO only, 1 for BAO+FS measurements

Let's use both the BAO and full-shape information, and so set the parameter :code:`mode` 1.  So our new parameter file section becomes::

    [boss]
    file = cosmosis-standard-library/likelihood/boss_dr12/boss_dr12.py
    mode = 1

Running the module
==================


Right now, nothing will change if we run this pipeline, because we have not told CosmoSIS to use this new module.  We can do so by changing the modules option from above to this::

    [pipeline]
    modules = consistency camb planck boss

This tells CosmoSIS to look for a section called "boss" in the parameter file and configure a module based on it.

It's fine to include unused modules in the parameter file - it can be useful later when you run different variations of a similar pipeline.

Once we have this, we can run the module with::

    cosmosis examples/planck/planck.ini

and it will now print out both likelihoods, and their total::

    Found likelihood named planck2018
        Likelihood boss_dr12 = -5.542050189759326
        Likelihood planck2018 = -6288.687206797975
    Likelihood total = -6294.2292569877345


More complicated pipelines
===========================

This was a case where only a simple addition to the pipeline was needed. In more complicated cases we often need more complicated pipelines, and to add more calculation steps along the way.

