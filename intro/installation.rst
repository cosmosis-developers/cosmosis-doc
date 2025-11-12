Installing CosmoSIS
-------------------

We are deeply indebted to Matt Becker for getting the Conda installation method to work.

Pip (core package only, no cosmology content)
=============================================

If you only need CosmoSIS for its core sampling tools and datablock, and don't need the cosmological likelihoods, then you can install those with pip::

    pip install cosmosis

If you get an error including the phrase ``--single-version-externally-managed not recognized`` then you should first upgrade your setuptools package like this::

    pip install -U setuptools wheel

and then try again.

Conda-Forge (from scratch)
==================================================

This is the easiest way to get the full CosmoSIS package. It downloads everything you need.  If the ``conda`` command works on your computer already, use the instructions for an existing installation (next section) instead. 

Otherwise first run one of these commands to download the installer:

On Linux::

    wget -O Miniforge3.sh  https://github.com/conda-forge/miniforge/releases/download/24.3.0-0/Miniforge3-Linux-x86_64.sh

On Intel Macs::

    wget -O Miniforge3.sh  https://github.com/conda-forge/miniforge/releases/download/24.3.0-0/Miniforge3-MacOSX-x86_64.sh

On Silicon (M1 or M2) Macs::

    wget -O Miniforge3.sh  https://github.com/conda-forge/miniforge/releases/download/24.3.0-0/Miniforge3-MacOSX-arm64.sh

Then, whichever you do, run these commands to install everything and download the standard library (see below for CosmoPower instructions)::

    chmod +x Miniforge3.sh
    ./Miniforge3.sh -b -p ./env
    source ./env/bin/activate
    mamba install -y cosmosis cosmosis-build-standard-library
    source cosmosis-configure
    cosmosis-build-standard-library main

This will make a new directory cosmosis-standard-library with the cosmology packages in. Explore that directory to start using CosmoSIS.

If you want to use `CosmoPower <https://github.com/alessiospuriomancini/cosmopower>`_ then change the fourth line above to::

    mamba install -y cosmosis cosmosis-build-standard-library cosmopower

Whenever you start a fresh terminal shell you need to run these commands to get set up again::

    source ./env/bin/activate
    source cosmosis-configure



Conda-Forge (existing installation)
===================================

If you already have conda installed on your computer, then you can create a new environment and install cosmosis tools in it with::

    conda create -p ./env -c conda-forge cosmosis cosmosis-build-standard-library
    conda activate ./env
    source cosmosis-configure
    cosmosis-build-standard-library

This will make a new directory cosmosis-standard-library with the cosmology packages in.

If you find this takes a very long time, you can try instead (mamba is a faster version of conda)::

    conda create -p ./env -c conda-forge mamba
    conda activate ./env
    mamba install -y cosmosis cosmosis-build-standard-library
    source cosmosis-configure
    cosmosis-build-standard-library main



Whenever you start a fresh terminal shell you need to run these commands to get set up again::

    conda activate ./env
    source cosmosis-configure

NERSC
=====

There is a globally-accessible CosmoSIS installation for the NERSC machine Perlmutter.  You can access it by running::

    source /dvs_ro/cfs/projectdirs/des/zuntz/cosmosis-global/setup-cosmosis3

This will set all the necessary environment variables; you can then clone the cosmosis-standard-library and the make command should work::

    git clone https://github.com/cosmosis-developers/cosmosis-standard-library
    cd cosmosis-standard-library
    make

You need source the setup script each time you want to use the system, including in batch scripts and interactive jobs.

If you need your own python environment to install new dependencies, you can do that with::

    conda create -p ./env --clone $CFS/des/zuntz/cosmosis-global/env-latest-${NERSC_HOST}

That will make a new environment in the ./env directory, which you can start using by doing::

    source /dvs_ro/cfs/projectdirs/des/zuntz/cosmosis-global/setup-cosmosis3 ./env

You can then pip or conda install things in your new environment.

If your dependency may be generally useful please open an issue and we can install it centrally also: https://github.com/cosmosis-developers/cosmosis/issues/

Jupyter at NERSC
================

After setting up the conda environment as described above, you can create a Jupyter "kernel" which lets you run notebooks in that environment with::

    python -m ipykernel install --user --name cosmosis-$(cosmosis --version)

Then you can select the kernel in the Jupyter notebook interface at jupyter.nersc.gov.


Installing manually on clusters and supercomputers
==================================================

The conda-forge version above often works on larger machines, though not always. Give it a go first (and test to see if multi-node jobs work).

If not, you will need these dependencies, which many systems will have already:

* `gcc/g++/gfortran 6 <https://gcc.gnu.org/>`_ or above
* MPI compilers
* `gsl 1.16 <http://ftpmirror.gnu.org/gsl/>`_ or above
* `cfitsio 3.30 <http://heasarc.gsfc.nasa.gov/fitsio/fitsio.html>`_ or above
* `FFTW 3 <http://www.fftw.org/download.html>`_ 
* `lapack <http://www.netlib.org/lapack/>`_ (except on MacOS)
* `git <https://git-scm.com/downloads>`_ 
* `python 3.6 or above <https://www.python.org/downloads/>`_

First, export these environment variables:

* ``GSL_INC`` the path to GSL header files
* ``GSL_LIB`` the path to GSL library files
* ``CFITSIO_INC`` the path to CFTSIO header files
* ``CFITSIO_LIB`` the path to CFTSIO library files
* ``FFTW_LIBRARY`` the path to FFTW header files
* ``FFTW_INCLUDE_DIR`` the path to FFTW library files
* ``LAPACK_LINK`` whatever command line you need to link to LAPACK
* ``CXX`` Command for your C++ compiler
* ``CC`` Command for your C compiler
* ``FC`` Command for your Fortran compiler
* ``MPIFC`` Command for your MPI Fortran compiler
* ``COSMOSIS_ALT_COMPILERS=1``

and run::

    python -m venv ./env
    source env/bin/activate
    pip install cosmosis camb astropy fitsio cython scikit-learn fast-pt

Then clone and build the standard library repository::

    source cosmosis-configure
    git clone https://github.com/cosmosis-developers/cosmosis-standard-library
    cd cosmosis-standard-library
    make

Please `open an issue <https://github.com/cosmosis-developers/cosmosis/issues/new>`_ if you have installation problems.

The ``cosmosis-configure`` command can also set you up to use HomeBrew to install things: ``source cosmosis-configure --brew``
