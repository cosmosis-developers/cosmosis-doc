CosmoPower training and usage within CosmoSIS
=============================================

CosmoSIS also has a capability to use CosmoPower to train emulators for any module in the pipeline, and then use those emulators in place of the original module. 




Training an CosmoPower emulator
-------------------------------

Running a CosmoPower training is done by adding a few parameters to the :code:`[pipeline]` section of your ini file.  For example, to train an emulator for the :code:`camb` module, you would add:

.. code-block:: ini
    [training]
    train_on_module = camb
    zmin = 0.0
    zmax = 3.0
    nsample = 200
    ntest = 10
    save_dir = %(OUTPUT_FOLDER)s

and run the CosmoSIS with your ini file with and additional command line argument: 

.. code-block:: bash
    cosmosis yourfile.ini --train_cosmopower

If you want to re-train an emulator or overwrite and existing one, you can run the CosmosSIS with and additional command line argument:

.. code-block:: bash
    cosmosis yourfile.ini --train_cosmopower --overwrite_cosmopower

The parameters in this section need a bit of explanation:
- :code:`train_on_module` is the name of the module you want to train an emulator for.  This module must be in the pipeline, if it is not present the CosmoSIS will stop and return and error. Currently only :code:`camb` is supported, as using the trained emulators requires a drop-in replacement interface module to be written, that reads the trained emulator files. Feel free to contribute such interface modules for other modules!
- :code:`zmin` and :code:`zmax` are the minimum and maximum redshifts you want the emulator to cover.  These must be within the range of redshifts that the original module can handle. They exists as in order to create the training samples we need to include the redshift as a parameter, pretending to be a parameter that it is sampled over.
- :code:`nsample` is the number of training samples to use.  More samples will give a more accurate emulator, but will take longer to train.
- :code:`ntest` is the number of test samples to use.  These are used to check the accuracy of the trained emulator, and should be as large as possible without making the training take too long.
- :code:`save_dir` is the directory where the trained emulator files will be saved. This directory will be used also by the interface module to read the trained emulator files, so it should be a permanent location.

When you run CosmoSIS with these parameters, it will run the pipeline :code:`nsample + ntest` times, varying the cosmological parameters each time. The parameters are picked from a Latin Hypercube grid, within the ranges of the free parameters of the module it is training on. The code will only take the free parameters of the module it is training on into account, so if you want to train on a module that has fixed parameters you will need to make those parameters free in order for them to be varied during the training, and will also disregard any parameters that are not used by the module it is training on.

By default the code will train on any outputs the module produces, for :code:`camb` this means the matter power spectrum and the CMB power spectra. 

The resulting emulator witll be saved in :code:`save_dir` directory, and will also print out some information about the training process, including the accuracy of the trained emulator on the test samples. The emulator files include the training and test samples that include the full datablock outputs at each parameter combination, the Latin Hypercube parameter combinations, test figures, and the trained emulator files themselves. Additionaly it saves the information on free and fixed parameters so that the interface module can read them and use them correctly.

Using a trained CosmoPower emulator
-----------------------------------

To use a trained CosmoPower emulator, you need to add a few parameters to the drop-in replacement interface module for the module you trained on. For :code:`camb` this is the :code:`cosmopower_interface` module. You need to add the following parameters to the :code:`[cosmopower_interface]` section of your ini file (the other parameters should be the same as for the original module):

.. code-block:: ini
    [cosmopower_interface]
    use_cosmopower_kvec = F
    cosmopower_folder = %(OUTPUT_FOLDER)s

The parameter :code:`use_cosmopower_kvec` can be set to :code:`T` or :code:`F`. If it is set to :code:`T` then the interface module will use a fixed k-vector for the matter power spectrum, that is saved in the trained emulator files. This is useful if you want to use the matter power spectrum in a subsequent module, as it avoids interpolation errors. If you set it to :code:`F` then the interface module will use the k-vector that is specified by the :code:`camb` module, which can be useful if you want to use a different k-vector than the one used during training.

The parameter :code:`cosmopower_folder` is the directory where the trained emulator files are saved. This should be the same directory that you used when training the emulator.

Inner workings of the training process
--------------------------------------

The training process works by running the CosmoSIS in a special mode, where it replaces the sampler specified in the ini file with a fixed set of two special samplers: a Latin Hypercube sampler that generates the training and test samples. The next step is to run the so-called "CosmoPower" sampler, which is a special sampler that does not actually sample, but instead trains the emulator on the training samples, and tests it on the test samples, by running the CosmoPower emulator code on each output of the desired module. The pipeline will be stopped after the module that the training is done on.

The Latin Hypercube sampler can be used outside of this process as well, for example if you want to generate a set of samples for some other purpose. To use it, you need to add the following parameters to the :code:`[latinhypercube]` section of your ini file (see also the :code:`grid` sampler documentation for more details - Latin Hypercube is a special case of grid sampling):

.. code-block:: ini
    [latinhypercube]
    nsample_dimension = 200