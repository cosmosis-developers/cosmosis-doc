Managing sets of runs with a Campaign
=====================================

It is common to want to run a suite of related analyses, for
example to explore the effects of different models, priors, or data sets.

CosmoSIS comes with a tool to help you do this, called the
``campaign`` module.  This allows you to specify a set of runs
using a YAML file, and then run them individually and check their status.

The command to run and use campaigns is called ``cosmosis-campaign``.


File Format
-----------

The campaign file is in the YAML format. You can find an
`example campaign file in the CosmoSIS standard library <https://github.com/cosmosis-developers/cosmosis-standard-library/blob/main/examples/desy3/des-campaign.yml>`_.

General settings
****************

The file can have four top-level keys:


- ``runs`` - a list of run definitions, see below.

- ``components`` - an optional dictionary of reusable components, see below.

-  ``output_dir`` which sets where all outputs from chains are saved. If this is not set then the current directory is used.

- ``include`` - either a list or a string, this specifies other YAML campaign files to load before the current one.

- ``output_name`` - a string to use as the format for all output files. This must include the string ``{name}`` which will be replaced by the name of the run. You can put other things before and after ``{name}`` to customize the output chain file names.

Runs
****

The file has a top-level key called ``runs`` which is a list of
runs. Each run has a name, and a dictionary of parameters.

Runs must have:

- a ``name`` key which is used to name output files for the run.

- EITHER ``base``: specifying an ini format parameter file on disk to run

- OR ``parent``: specifying another run to descend from.  The parent run must have been defined earlier in the file.

  * a common pattern is to have a single base run, and then a set of runs that are descended from it, making modifications.

Optionally they may have any of these keys:

- ``params``: a dictionary of parameter updates to use for this run.  These will be replace values in the base or parent run.

- ``values``:  similar updates to the values file of fixed and varied numerical parameters input to the chain.

- ``priors``: similar updates to the priors.

- ``pipeline``:updates to the list of modules that make up the pipeline.

- ``components``: a list of keys to the ``components`` dictionary (see below).

- ``env``:  a dictionary of environment variables to set for this run, both when making the configuration and running the chain.

Updates to runs
***************

Updates to the params, values, or priors modify the settings from the parameter file, and can have either of these forms:

- ``section.option=value`` to set or replace a single parameter

- ``del section.option`` to delete a parameter

- ``del section`` to delete an entire section

For example, the update ``camb.feedback=4`` would change the ``feedback`` option in the ``[camb]`` section of the parameter file to ``4``.

Additionally, the parameter file only can accept an option of the form:

- ``sampler=<name of sampler>`` to select the sampler to be used. This is shortand for ``runtime.sampler=<name>``.

The ``pipeline`` key is a list of changes to the "modules" setting in the parameter file, which
specifies the list of CosmoSIS modules to be run to evaluate a likelihood.  The changes can be:

- ``after <module> <new_module> [<new_module> ...]`` to add one or more modules after an existing one

- ``before <module> <new_module> [<new_module> ...]`` to add one or more modules before an existing one

- ``replace <module> <new_module> [<new_module> ...]`` to replace a module with one or more new ones

- ``del <module> [<module> ...]`` to delete a module

- ``append <new_module> [<new_module> ...]`` to add a new module to the end of the pipeline

- ``prepend <new_module> [<new_module> ...]`` to add a new module to the start of the pipeline



Components
**********

It's common to have a set of updates to a pipeline that are used in many runs. For example,
you might have many runs that add a new parameter to the pipeline, such as varying the equation of state ``w``.

Rather than repeating the same set of updates in many runs, you can define a component and then refer to it in mulltiple runs.

Components are defined in a dictionary called ``components``.  Each component has a name, and a dictionary of updates.
The updates are exact same format as for the runs.

Components are applied before any updates in the runs themselves.


Using the campaign tool from the command line
----------------------------------------------

The ``cosmosis-campaign`` command is always called with the name of the campaign file described above.

Then it has a number of options:

- ``--list`` or ``-l`` lists the names of all the runs in the campaign.

- ``--cat <name>`` or ``-c <name>`` prints the ini files that would be generated for a given run

- ``--run <name>`` or ``-r <name>`` launches a run.

- ``--test <name>`` or ``-t <name>`` runs a pipeline using the test sampler to check it works.

- ``--status`` or ``-s`` shows the status of all runs, or a single run if given a name. It checks whether an output file for the run has been generated and how large and recent it is.  Because this option takes an optional argument it must be given after the name of the campaign file.

If you use the ``--run`` flag to set a run going then you can also give the ``--mpi`` flag to run it under MPI. In that case
you should run the whole ``cosmosis-campaign`` command under MPI, e.g.

``mpirun -n 4 cosmosis-campaign my_campaign.yml --run my_run --mpi``


Using the campaign tool from a Python script or Jupyter notebook
------------------------------------------------------------------

You can import the campaign module into a script or notebook and use the tools in it to
run and monitor campaigns.

You can import the module ``cosmosis.campaign``, and then monitor with the functions:

- ``parse_yaml_run_file(filename)`` - parse a campaign file.

- ``show_run(run_info)`` - print the ini information to the screen for the dict specifying the run

- ``show_run_status(runs_dict, [name_of_run])`` - print a summary of the status of all runs, or a single run if given a name.

- ``launch_run(run, mpi=False)`` - launch a run, optionally under MPI.

You can also explore the commands that modify runs and components by looking at the function docstrings in that module.


