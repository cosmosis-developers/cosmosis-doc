Changelog
=========

This page lists changes to the two CosmoSIS repositories: the core `cosmosis <https://github.com/cosmosis-developers/cosmosis>`_ package and the `cosmosis-standard-library <https://github.com/cosmosis-developers/cosmosis-standard-library>`_.

It is generated from GitHub by ``generate_changelog.py`` and was last updated on 2026-11-20.

.. contents::
   :local:
   :depth: 1

CosmoSIS
--------

Changes to the core ``cosmosis`` package, taken from the `release notes <https://github.com/cosmosis-developers/cosmosis/releases>`_.

v3.27.1
~~~~~~~

*Released 2026-11-06* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.27.1>`__

* Validate truncated prior boundaries by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#233 <https://github.com/cosmosis-developers/cosmosis/pull/233>`__
* Use Cholesky solves in PMC covariance evaluation by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#222 <https://github.com/cosmosis-developers/cosmosis/pull/222>`__
* Use stable logsumexp in grid plots by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#223 <https://github.com/cosmosis-developers/cosmosis/pull/223>`__
* Change ``multinest`` and ``polychord`` Fortran wrappers and build flags so the libraries do not need an executable stack on Linux by `@joezuntz <https://github.com/joezuntz>`__ in `#251 <https://github.com/cosmosis-developers/cosmosis/pull/251>`__
* Fix MultiNest shared library executable stack by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#250 <https://github.com/cosmosis-developers/cosmosis/pull/250>`__
* Declare h5py for Nautilus installation by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#245 <https://github.com/cosmosis-developers/cosmosis/pull/245>`__
* Update publish workflow actions to current major versions by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#240 <https://github.com/cosmosis-developers/cosmosis/pull/240>`__
* Handle zero within-chain variance in Gelman-Rubin diagnostic by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#246 <https://github.com/cosmosis-developers/cosmosis/pull/246>`__
* Reject negative tabulated prior densities before integration by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#234 <https://github.com/cosmosis-developers/cosmosis/pull/234>`__

v3.26
~~~~~

*Released 2026-09-03* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.26>`__

* Add methods to quickly serialize and deserialize a ``DataBlock`` to a binary file by `@joezuntz <https://github.com/joezuntz>`__ in `#219 <https://github.com/cosmosis-developers/cosmosis/pull/219>`__
* Avoid explicit inverse in GaussianLikelihood chi-square evaluation by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#220 <https://github.com/cosmosis-developers/cosmosis/pull/220>`__

**New Contributors**


* `@fujikix1102 <https://github.com/fujikix1102>`__ made their first contribution in `#220 <https://github.com/cosmosis-developers/cosmosis/pull/220>`__

v3.25.2
~~~~~~~

*Released 2026-03-09* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.25.2>`__

* Fix config object items method when there are defaults and defaults=False by `@joezuntz <https://github.com/joezuntz>`__ in `#214 <https://github.com/cosmosis-developers/cosmosis/pull/214>`__

v3.25.1
~~~~~~~

*Released 2026-03-05* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.25.1>`__

* Fix ``Inifile.items`` interpolation with newer Python versions by `@joezuntz <https://github.com/joezuntz>`__ in `#212 <https://github.com/cosmosis-developers/cosmosis/pull/212>`__

v3.25
~~~~~

*Released 2025-12-03* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.25>`__

* Simplify use of ``hermitian=True`` when inverting covariance matrices in ``GaussianLikelihood``, falling back for older numpy by `@joezuntz <https://github.com/joezuntz>`__ in `#210 <https://github.com/cosmosis-developers/cosmosis/pull/210>`__
* Add configure script flag to create conda activate script by `@joezuntz <https://github.com/joezuntz>`__ in `#211 <https://github.com/cosmosis-developers/cosmosis/pull/211>`__

v3.24
~~~~~

*Released 2025-10-29* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.24>`__

* Add a ``cosmopower_train`` sampler for training CosmoPower emulators, and a ``latin_hypercube`` sampler by `@andrejdvornik <https://github.com/andrejdvornik>`__ in `#206 <https://github.com/cosmosis-developers/cosmosis/pull/206>`__
* Add function to read files into getdist by `@joezuntz <https://github.com/joezuntz>`__ in `#208 <https://github.com/cosmosis-developers/cosmosis/pull/208>`__
* Allow setting of env var to enable importing cosmosis without building by `@joezuntz <https://github.com/joezuntz>`__ in `#209 <https://github.com/cosmosis-developers/cosmosis/pull/209>`__

**New Contributors**


* `@andrejdvornik <https://github.com/andrejdvornik>`__ made their first contribution in `#206 <https://github.com/cosmosis-developers/cosmosis/pull/206>`__

v3.23
~~~~~

*Released 2025-09-08* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.23>`__

* Add a cosmosis format to astropy by `@joezuntz <https://github.com/joezuntz>`__ in `#205 <https://github.com/joezuntz/cosmosis/pull/205>`__

v3.22.1
~~~~~~~

*Released 2025-09-03* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.22.1>`__

* Fix zeus yaml to expected format to fix documentation by `@joezuntz <https://github.com/joezuntz>`__ in `#204 <https://github.com/joezuntz/cosmosis/pull/204>`__

v3.22
~~~~~

*Released 2025-09-01* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.22>`__

* Allow the documented ``smooth`` method to be used when running the ``fisher`` sampler by `@ajouellette <https://github.com/ajouellette>`__ in `#196 <https://github.com/joezuntz/cosmosis/pull/196>`__
* Audit and complete sampler.yaml parameter documentation across all samplers by `@Copilot <https://github.com/Copilot>`__ in `#198 <https://github.com/joezuntz/cosmosis/pull/198>`__
* Add comprehensive GitHub Copilot instructions for CosmoSIS development by `@Copilot <https://github.com/Copilot>`__ in `#200 <https://github.com/joezuntz/cosmosis/pull/200>`__
* Remove Python 2 compatibility code by `@Copilot <https://github.com/Copilot>`__ in `#201 <https://github.com/joezuntz/cosmosis/pull/201>`__
* Avoid serializing the current sample data block in metropolis checkpoints by `@joezuntz <https://github.com/joezuntz>`__ in `#203 <https://github.com/joezuntz/cosmosis/pull/203>`__

**New Contributors**


* `@Copilot <https://github.com/Copilot>`__ made their first contribution in `#198 <https://github.com/joezuntz/cosmosis/pull/198>`__

v3.21.1
~~~~~~~

*Released 2025-07-09* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.21.1>`__

This is actually the same as v3.20.2 but I forgot to update the version number.

* Make ``cosmosis-campaign`` use the ``output_name`` setting for ``test``, ``multinest`` and ``polychord`` output files by `@joezuntz <https://github.com/joezuntz>`__ in `#188 <https://github.com/joezuntz/cosmosis/pull/188>`__
* Fix final nsample value in polychord boosted files by `@joezuntz <https://github.com/joezuntz>`__ in `#189 <https://github.com/joezuntz/cosmosis/pull/189>`__
* Fix malformed Fortran format strings in ``polychord`` progress and stats output that caused crashes by `@joezuntz <https://github.com/joezuntz>`__ in `#191 <https://github.com/joezuntz/cosmosis/pull/191>`__

v3.20.2
~~~~~~~

*Released 2025-07-08* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.20.2>`__

This is a bugfix release:

* Make ``cosmosis-campaign`` use the ``output_name`` setting for ``test``, ``multinest`` and ``polychord`` output files by `@joezuntz <https://github.com/joezuntz>`__ in `#188 <https://github.com/joezuntz/cosmosis/pull/188>`__
* Fix final nsample value in polychord boosted files by `@joezuntz <https://github.com/joezuntz>`__ in `#189 <https://github.com/joezuntz/cosmosis/pull/189>`__
* Fix malformed Fortran format strings in ``polychord`` progress and stats output that caused crashes by `@joezuntz <https://github.com/joezuntz>`__ in `#191 <https://github.com/joezuntz/cosmosis/pull/191>`__

v3.20.1
~~~~~~~

*Released 2025-05-06* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.20.1>`__

* Use a more robust fix for the ``DataBlock`` logging crash with long type names by `@joezuntz <https://github.com/joezuntz>`__ in `#184 <https://github.com/joezuntz/cosmosis/pull/184>`__
* Handle errors in pybobyqa gracefully by `@joezuntz <https://github.com/joezuntz>`__ in `#185 <https://github.com/joezuntz/cosmosis/pull/185>`__

v3.20
~~~~~

*Released 2025-05-05* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.20>`__

* Handle yaml merge keys by `@ajouellette <https://github.com/ajouellette>`__ in `#180 <https://github.com/joezuntz/cosmosis/pull/180>`__
* Fix a ``DataBlock`` logging bug when storing string arrays by `@joezuntz <https://github.com/joezuntz>`__ in `#183 <https://github.com/joezuntz/cosmosis/pull/183>`__

v3.19
~~~~~

*Released 2025-03-26* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.19>`__

* Add a ``reiterations`` parameter to the maxlike sampler to re-run optimization starting at the previous point

v3.18.2
~~~~~~~

*Released 2025-03-24* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.18.2>`__

* Speed up nautilus test and print test timing by `@joezuntz <https://github.com/joezuntz>`__ in `#178 <https://github.com/joezuntz/cosmosis/pull/178>`__
* Allow postprocessing multiple metropolis files by `@joezuntz <https://github.com/joezuntz>`__ in `#179 <https://github.com/joezuntz/cosmosis/pull/179>`__

v3.18.1
~~~~~~~

*Released 2025-03-21* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.18.1>`__

* Allow running testing campaign runs under PDB by `@joezuntz <https://github.com/joezuntz>`__ in `#177 <https://github.com/joezuntz/cosmosis/pull/177>`__
* Stop errors reading module attribution (``module.yaml``) files from crashing runs by `@joezuntz <https://github.com/joezuntz>`__ in `#176 <https://github.com/joezuntz/cosmosis/pull/176>`__
* Fix a bug when running the Minuit sampler

v3.18
~~~~~

*Released 2025-03-14* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.18>`__

* Allow starting a sampler from the best-fit point in a chain file by `@joezuntz <https://github.com/joezuntz>`__ in `#175 <https://github.com/joezuntz/cosmosis/pull/175>`__

v3.17
~~~~~

*Released 2025-02-14* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.17>`__

* Add a numeric index to output file names when the same sampler appears more than once in a chained ``sampler`` list by `@joezuntz <https://github.com/joezuntz>`__ in `#172 <https://github.com/joezuntz/cosmosis/pull/172>`__

v3.16.1
~~~~~~~

*Released 2025-02-14* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.16.1>`__

* Fix the likelihoods in the reformatted polychord boosted files by `@joezuntz <https://github.com/joezuntz>`__ in `#169 <https://github.com/joezuntz/cosmosis/pull/169>`__
* Fix a crash when totalling pipeline call counts at the end of runs using the SMP process pool by `@joezuntz <https://github.com/joezuntz>`__ in `#171 <https://github.com/joezuntz/cosmosis/pull/171>`__

v3.16
~~~~~

*Released 2025-01-13* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.16>`__

* Save covariance matrix hints as well as max-post hints where possible by `@joezuntz <https://github.com/joezuntz>`__ in `#160 <https://github.com/joezuntz/cosmosis/pull/160>`__
* Fix error in NautilusSampler when saving outputs by `@ajshajib <https://github.com/ajshajib>`__ in `#163 <https://github.com/joezuntz/cosmosis/pull/163>`__
* Add output_block option to maxlike sampler by `@joezuntz <https://github.com/joezuntz>`__ in `#164 <https://github.com/joezuntz/cosmosis/pull/164>`__

**New Contributors**


* `@ajshajib <https://github.com/ajshajib>`__ made their first contribution in `#163 <https://github.com/joezuntz/cosmosis/pull/163>`__

v3.15
~~~~~

*Released 2024-12-10* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.15>`__

* Add new mode to fisher matrix sampler with smoothed derivatives by `@joezuntz <https://github.com/joezuntz>`__ in `#157 <https://github.com/joezuntz/cosmosis/pull/157>`__

V3.14.1
~~~~~~~

*Released 2024-12-09* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/V3.14.1>`__

* Pass the Hessian from the ``bobyqa`` method to the ``maxlike`` sampler so it can save covariance outputs by `@joezuntz <https://github.com/joezuntz>`__ in `#156 <https://github.com/joezuntz/cosmosis/pull/156>`__

v3.14
~~~~~

*Released 2024-12-05* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.14>`__

* Include truth values on Fisher matrix plots if requested by `@ajouellette <https://github.com/ajouellette>`__ in `#149 <https://github.com/joezuntz/cosmosis/pull/149>`__
* Add repeats option to maxlike sampler to make it run from multiple starting points, and parallelize  by `@joezuntz <https://github.com/joezuntz>`__ in `#155 <https://github.com/joezuntz/cosmosis/pull/155>`__

**New Contributors**


* `@ajouellette <https://github.com/ajouellette>`__ made their first contribution in `#149 <https://github.com/joezuntz/cosmosis/pull/149>`__

v3.13.2
~~~~~~~

*Released 2024-11-29* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.13.2>`__

* Fix renaming old log_weight col correctly in importance sampler by `@joezuntz <https://github.com/joezuntz>`__ in `#150 <https://github.com/joezuntz/cosmosis/pull/150>`__
* Allow numpy version 2 by `@joezuntz <https://github.com/joezuntz>`__ in `#154 <https://github.com/joezuntz/cosmosis/pull/154>`__

v3.13.1
~~~~~~~

*Released 2024-11-29* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.13.1>`__

* Fix renaming old log_weight col correctly in importance sampler by `@joezuntz <https://github.com/joezuntz>`__ in `#150 <https://github.com/joezuntz/cosmosis/pull/150>`__
* Allow numpy version 2 by `@joezuntz <https://github.com/joezuntz>`__ in `#154 <https://github.com/joezuntz/cosmosis/pull/154>`__

v3.13
~~~~~

*Released 2024-11-20* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.13>`__

* Add bobyqa minimizer by `@joezuntz <https://github.com/joezuntz>`__ in `#147 <https://github.com/joezuntz/cosmosis/pull/147>`__
* Add a version of the boosted polychord file with a full header. by `@joezuntz <https://github.com/joezuntz>`__ in `#148 <https://github.com/joezuntz/cosmosis/pull/148>`__
* Add a helper method to re-create a pipeline object from a chain output file. by `@joezuntz <https://github.com/joezuntz>`__ in `#151 <https://github.com/joezuntz/cosmosis/pull/151>`__
* Add utility function datablock_to_astropy by `@joezuntz <https://github.com/joezuntz>`__ in `#152 <https://github.com/joezuntz/cosmosis/pull/152>`__
* Add python 3.12 to CI by `@joezuntz <https://github.com/joezuntz>`__ in `#144 <https://github.com/joezuntz/cosmosis/pull/144>`__

v3.12.1
~~~~~~~

*Released 2024-09-17* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.12.1>`__

* Fix the getdist branch of postprocessing statistics to also report the automatically found max-like and max-post samples by `@joezuntz <https://github.com/joezuntz>`__ in `#143 <https://github.com/joezuntz/cosmosis/pull/143>`__

v3.12
~~~~~

*Released 2024-09-08* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.12>`__

* All samplers now save their MAP estimate for the next to use, allowing you to follow a nested or MCMC chain with an optimizer `@joezuntz <https://github.com/joezuntz>`__ in `#141 <https://github.com/joezuntz/cosmosis/pull/141>`__

v3.11.2
~~~~~~~

*Released 2024-08-13* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.11.2>`__

Adds ability to resume importance sampler.

v3.11.1
~~~~~~~

*Released 2024-07-26* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.11.1>`__

* Fix crash in PocoMC checkpointing when using class by `@joezuntz <https://github.com/joezuntz>`__ in `#137 <https://github.com/joezuntz/cosmosis/pull/137>`__

v3.11
~~~~~

*Released 2024-07-25* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.11>`__

* Add an option to log all failed parameter sets to a file by `@joezuntz <https://github.com/joezuntz>`__ in `#135 <https://github.com/joezuntz/cosmosis/pull/135>`__

v3.10
~~~~~

*Released 2024-07-16* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.10>`__

* Expose the ``n_steps`` parameter for the ``pocomc`` sampler by `@minaskar <https://github.com/minaskar>`__ in `#133 <https://github.com/joezuntz/cosmosis/pull/133>`__

v3.9.2
~~~~~~

*Released 2024-06-28* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.9.2>`__

Fix a bug when trying to use PocoMC in parallel

v3.9.1
~~~~~~

*Released 2024-06-28* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.9.1>`__

Fix a bug when trying to use PocoMC in parallel

v3.9
~~~~

*Released 2024-06-21* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.9>`__

* Added support for pocoMC 1.2.2 by `@minaskar <https://github.com/minaskar>`__ in `#131 <https://github.com/joezuntz/cosmosis/pull/131>`__

**New Contributors**


* `@minaskar <https://github.com/minaskar>`__ made their first contribution in `#131 <https://github.com/joezuntz/cosmosis/pull/131>`__

v3.8
~~~~

*Released 2024-06-12* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.8>`__

* Add preliminary classes for version 2 of the postprocessing system by `@joezuntz <https://github.com/joezuntz>`__ in `#128 <https://github.com/joezuntz/cosmosis/pull/128>`__
* Propagate command line changes to the values file into output headers by `@joezuntz <https://github.com/joezuntz>`__ in `#129 <https://github.com/joezuntz/cosmosis/pull/129>`__

v3.7
~~~~

*Released 2024-05-29* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.7>`__

* Update nautilus integration to 1.0 by `@johannesulf <https://github.com/johannesulf>`__ in `#119 <https://github.com/joezuntz/cosmosis/pull/119>`__
* Fix thinning and burning in list sampler by `@joezuntz <https://github.com/joezuntz>`__ in `#127 <https://github.com/joezuntz/cosmosis/pull/127>`__

v3.6
~~~~

*Released 2024-05-27* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.6>`__

* Improve error messaging in fast/slow split `@joezuntz <https://github.com/joezuntz>`__ in `#106 <https://github.com/joezuntz/cosmosis/pull/106>`__
* Add an option to submit jobs with the campaign system by `@joezuntz <https://github.com/joezuntz>`__ in `#105 <https://github.com/joezuntz/cosmosis/pull/105>`__
* Defer expanding environment variables in parent campaign runs so children can override by `@joezuntz <https://github.com/joezuntz>`__ in `#116 <https://github.com/joezuntz/cosmosis/pull/116>`__
* Check for duplicate keys in ``cosmosis-campaign`` YAML files by `@joezuntz <https://github.com/joezuntz>`__ in `#117 <https://github.com/joezuntz/cosmosis/pull/117>`__
* Fix CI workflow failure caused by missing ``gfortran`` by `@joezuntz <https://github.com/joezuntz>`__ in `#121 <https://github.com/joezuntz/cosmosis/pull/121>`__
* Fix inheritance of components and environment variables from parent files and runs in ``cosmosis-campaign`` by `@joezuntz <https://github.com/joezuntz>`__ in `#125 <https://github.com/joezuntz/cosmosis/pull/125>`__

v3.5.1
~~~~~~

*Released 2024-01-09* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.5.1>`__

* Let campaign output name be overridden per run by `@joezuntz <https://github.com/joezuntz>`__ in `#112 <https://github.com/joezuntz/cosmosis/pull/112>`__

v3.5
~~~~

*Released 2024-01-04* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.5>`__

* Avoid crashing when git revision metadata for output headers cannot be read by `@joezuntz <https://github.com/joezuntz>`__ in `#110 <https://github.com/joezuntz/cosmosis/pull/110>`__
* Allow user to set name of campaign output by `@joezuntz <https://github.com/joezuntz>`__ in `#111 <https://github.com/joezuntz/cosmosis/pull/111>`__
* Fix the cosmosis-extract tool which was lower-casing file names.

v3.4.4
~~~~~~

*Released 2023-11-09* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.4.4>`__

* Make list sampler operate on chunks of data by `@joezuntz <https://github.com/joezuntz>`__ in `#108 <https://github.com/joezuntz/cosmosis/pull/108>`__

v3.4.3
~~~~~~

*Released 2023-11-09* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.4.3>`__

* Make list sampler operate on chunks of data by `@joezuntz <https://github.com/joezuntz>`__ in `#108 <https://github.com/joezuntz/cosmosis/pull/108>`__

v3.4.2
~~~~~~

*Released 2023-11-09* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.4.2>`__

* Make list sampler operate on chunks of data by `@joezuntz <https://github.com/joezuntz>`__ in `#108 <https://github.com/joezuntz/cosmosis/pull/108>`__

v3.4.1
~~~~~~

*Released 2023-11-09* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.4.1>`__

* Make list sampler operate on chunks of data by `@joezuntz <https://github.com/joezuntz>`__ in `#108 <https://github.com/joezuntz/cosmosis/pull/108>`__

v3.4
~~~~

*Released 2023-09-20* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.4>`__

* Postprocess updates to generate maxlike and maxpost outputs, and fix bugs in grid plotting by `@joezuntz <https://github.com/joezuntz>`__ in `#103 <https://github.com/joezuntz/cosmosis/pull/103>`__
* Update dynesty to save blobs and prior by `@joezuntz <https://github.com/joezuntz>`__ in `#102 <https://github.com/joezuntz/cosmosis/pull/102>`__

v3.3.1
~~~~~~

*Released 2023-09-01* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.3.1>`__

* Fix bugs in the pipeline ``from_likelihood_function`` method by `@joezuntz <https://github.com/joezuntz>`__ in `#99 <https://github.com/joezuntz/cosmosis/pull/99>`__

v3.3
~~~~

*Released 2023-09-01* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.3>`__

* Add a ``from_likelihood_function`` method to build a pipeline directly from a single likelihood function by `@joezuntz <https://github.com/joezuntz>`__ in `#98 <https://github.com/joezuntz/cosmosis/pull/98>`__

v3.2
~~~~

*Released 2023-08-17* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.2>`__

* Fix values passed to ``run_cosmosis`` (e.g. by the campaign tool) being ignored when running under MPI by `@joezuntz <https://github.com/joezuntz>`__ in `#95 <https://github.com/joezuntz/cosmosis/pull/95>`__, including a change to the default root directory.

v3.1
~~~~

*Released 2023-08-03* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.1>`__

* Add postprocessing plots for the ``apriori`` sampler and allow it to resume by `@joezuntz <https://github.com/joezuntz>`__ in `#94 <https://github.com/joezuntz/cosmosis/pull/94>`__

v3.0.3
~~~~~~

*Released 2023-07-28* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.0.3>`__

* Reduce parallel output with more careful logging by `@joezuntz <https://github.com/joezuntz>`__ in `#93 <https://github.com/joezuntz/cosmosis/pull/93>`__

v3.0.2
~~~~~~

*Released 2023-07-28* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.0.2>`__

* Reduce parallel output with more careful logging by `@joezuntz <https://github.com/joezuntz>`__ in `#93 <https://github.com/joezuntz/cosmosis/pull/93>`__

v3.0.1
~~~~~~

*Released 2023-07-28* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.0.1>`__

* A handful of fixes based on quick tests with version 3.0.  See that version for a more interesting changelog versus 2.*

  * Fix a crash when postprocessing fails
  * Fix postprocessing grid-type samples
  * Work around an MPICH bug in multinest
  * Add a build action in setup.py to help with editable installs

v3.0
~~~~

*Released 2023-07-27* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.0>`__

* Update the ``nautilus`` sampler interface: remove ``n_jobs``, share one parallel pool, and raise default live points to 2000 by `@johannesulf <https://github.com/johannesulf>`__ in `#90 <https://github.com/joezuntz/cosmosis/pull/90>`__
* Expose emcee "a" parameter by `@joezuntz <https://github.com/joezuntz>`__ in `#67 <https://github.com/joezuntz/cosmosis/pull/67>`__
* Allow more configuration of the ``run_cosmosis`` and ``run_postprocess`` functions, for use from Jupyter or other interactive notebooks.
* Add the ``cosmosis-campaign`` tool to manage suites of related runs.
* Allow output in ``astropy`` table format in interactive mode.
* Extensive changes to logging - we now exclusively use cosmosis.logs for anything that is printed during main sampling

  * The ``quiet`` option is deprecated in favour of more fine-grained logging control.

* Tidy up the output in general
* Update the setup script to avoid the deprecated distutils.
* Deal with various deprecation warnings
* Modify the format of the tables output by the "statistics" postprocessor so they can be read in astropy.
* Fix corner plots so you can put multiple chains on the same axes.
* Allow using MPI pools with general communicator objects - should make it possible to run under MPI in jupyter eventually.

v2.5.1
~~~~~~

*Released 2023-05-25* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.5.1>`__

* Allow passing new priors to the ``run_cosmosis`` function by `@joezuntz <https://github.com/joezuntz>`__ in `#86 <https://github.com/joezuntz/cosmosis/pull/86>`__
* Add corner plots to ``cosmosis-postprocess`` and switch to a faster, more accurate KDE method by default by `@joezuntz <https://github.com/joezuntz>`__ in `#87 <https://github.com/joezuntz/cosmosis/pull/87>`__

v2.5
~~~~

*Released 2023-05-25* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.5>`__

* Allow passing new priors to the ``run_cosmosis`` function by `@joezuntz <https://github.com/joezuntz>`__ in `#86 <https://github.com/joezuntz/cosmosis/pull/86>`__
* Add corner plots to ``cosmosis-postprocess`` and switch to a faster, more accurate KDE method by default by `@joezuntz <https://github.com/joezuntz>`__ in `#87 <https://github.com/joezuntz/cosmosis/pull/87>`__

v2.4.1
~~~~~~

*Released 2023-04-24* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.4.1>`__

* Expose new run options from ``nautilus`` 0.6 in the ``nautilus`` sampler by `@johannesulf <https://github.com/johannesulf>`__ in `#83 <https://github.com/joezuntz/cosmosis/pull/83>`__
* Add a test of additional nautilus options by `@joezuntz <https://github.com/joezuntz>`__ in `#84 <https://github.com/joezuntz/cosmosis/pull/84>`__

v2.4
~~~~

*Released 2023-04-24* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.4>`__

* Expose new run options from ``nautilus`` 0.6 in the ``nautilus`` sampler by `@johannesulf <https://github.com/johannesulf>`__ in `#83 <https://github.com/joezuntz/cosmosis/pull/83>`__
* Add a test of additional nautilus options by `@joezuntz <https://github.com/joezuntz>`__ in `#84 <https://github.com/joezuntz/cosmosis/pull/84>`__

v2.3.2
~~~~~~

*Released 2023-03-27* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.3.2>`__

* Bugfix for list sampler with vector quantities as extra output by `@BStoelzner <https://github.com/BStoelzner>`__ in `#76 <https://github.com/joezuntz/cosmosis/pull/76>`__
* Fix ``dynesty`` and ``nautilus`` samplers using the posterior instead of the likelihood by `@joezuntz <https://github.com/joezuntz>`__ in `#82 <https://github.com/joezuntz/cosmosis/pull/82>`__

**New Contributors**


* `@BStoelzner <https://github.com/BStoelzner>`__ made their first contribution in `#76 <https://github.com/joezuntz/cosmosis/pull/76>`__

v2.3.1
~~~~~~

*Released 2023-03-15* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.3.1>`__

* Fix using output from Nautilus when no extra parameters requested by `@joezuntz <https://github.com/joezuntz>`__ in `#74 <https://github.com/joezuntz/cosmosis/pull/74>`__

v2.3
~~~~

*Released 2023-03-03* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.3>`__

* Implement nautilus sampler interface by `@johannesulf <https://github.com/johannesulf>`__ in `#70 <https://github.com/joezuntz/cosmosis/pull/70>`__

**New Contributors**


* `@johannesulf <https://github.com/johannesulf>`__ made their first contribution in `#70 <https://github.com/joezuntz/cosmosis/pull/70>`__

v2.2.5
~~~~~~

*Released 2023-02-20* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.2.5>`__

* Add ``covmat_sample_start`` option to the ``metropolis`` sampler to draw the starting point from the covariance matrix by `@joezuntz <https://github.com/joezuntz>`__ in `#63 <https://github.com/joezuntz/cosmosis/pull/63>`__
* Improve error messages when a pipeline module file is missing or has an unrecognised suffix, and add tests by `@joezuntz <https://github.com/joezuntz>`__ in `#66 <https://github.com/joezuntz/cosmosis/pull/66>`__
* Fix ``multinest`` and ``polychord`` output of vector-valued extra quantities by `@joezuntz <https://github.com/joezuntz>`__ in `#71 <https://github.com/joezuntz/cosmosis/pull/71>`__

v2.2.4
~~~~~~

*Released 2023-02-20* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.2.4>`__

* Add ``covmat_sample_start`` option to the ``metropolis`` sampler to draw the starting point from the covariance matrix by `@joezuntz <https://github.com/joezuntz>`__ in `#63 <https://github.com/joezuntz/cosmosis/pull/63>`__
* Improve error messages when a pipeline module file is missing or has an unrecognised suffix, and add tests by `@joezuntz <https://github.com/joezuntz>`__ in `#66 <https://github.com/joezuntz/cosmosis/pull/66>`__
* Fix ``multinest`` and ``polychord`` output of vector-valued extra quantities by `@joezuntz <https://github.com/joezuntz>`__ in `#71 <https://github.com/joezuntz/cosmosis/pull/71>`__

v2.2.3
~~~~~~

*Released 2022-11-08* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.2.3>`__

* Add missing requirements and remove redundancies by `@marcpaterno <https://github.com/marcpaterno>`__ in `#55 <https://github.com/joezuntz/cosmosis/pull/55>`__
* Raise a Python exception instead of crashing when ``DataBlock`` put/get is used with the wrong array type by `@joezuntz <https://github.com/joezuntz>`__ in `#56 <https://github.com/joezuntz/cosmosis/pull/56>`__
* Add 3.11 to CI by `@joezuntz <https://github.com/joezuntz>`__ in `#57 <https://github.com/joezuntz/cosmosis/pull/57>`__
* Add sklearn into dependencies by `@joezuntz <https://github.com/joezuntz>`__ in `#58 <https://github.com/joezuntz/cosmosis/pull/58>`__

v2.2.2
~~~~~~

*Released 2022-10-17* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.2.2>`__

* Enable python 3.10 in the CI by `@joezuntz <https://github.com/joezuntz>`__ in `#49 <https://github.com/joezuntz/cosmosis/pull/49>`__
* Add ``COSMOSIS_NO_SUBPROCESS`` environment variable to skip pre/post-run scripts and other subprocess launches by `@joezuntz <https://github.com/joezuntz>`__ in `#50 <https://github.com/joezuntz/cosmosis/pull/50>`__

CosmoSIS previously launched git in a subprocess to try and find out the git revisions of various directories. This causes problems on the NERSC Perlmutter machine because that's technically undefined behaviour under MPI and the Cray MPI implementation actually does do strange things.  CosmoSIS will now try to use the Dulwich library to find the versions without using a subprocess, and in either case the setting the new ``COSMOSIS_NO_SUBPROCESS`` environment variable to ``1`` will stop any subprocesses from being launched.

We also now test CosmoSIS under python 3.10, so that version is now fully supported.

v2.2.1
~~~~~~

*Released 2022-10-17* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.2.1>`__

* Enable python 3.10 in the CI by `@joezuntz <https://github.com/joezuntz>`__ in `#49 <https://github.com/joezuntz/cosmosis/pull/49>`__
* Add ``COSMOSIS_NO_SUBPROCESS`` environment variable to skip pre/post-run scripts and other subprocess launches by `@joezuntz <https://github.com/joezuntz>`__ in `#50 <https://github.com/joezuntz/cosmosis/pull/50>`__

CosmoSIS previously launched git in a subprocess to try and find out the git revisions of various directories. This causes problems on the NERSC Perlmutter machine because that's technically undefined behaviour under MPI and the Cray MPI implementation actually does do strange things.  CosmoSIS will now try to use the Dulwich library to find the versions without using a subprocess, and in either case the setting the new ``COSMOSIS_NO_SUBPROCESS`` environment variable to ``1`` will stop any subprocesses from being launched.

We also now test CosmoSIS under python 3.10, so that version is now fully supported.

v2.2
~~~~

*Released 2022-09-21* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.2>`__

* Added a flag --profile FILENAME to cosmosis to use the python cProfile tool to see where time is spent in the code
* Added the flag --truth FILENAME to cosmosis-postprocess which adds a truth marker when given an values file
* Fixed a problem with contour legends in postprocessing in newer matplotlib versions

v2.1.5
~~~~~~

*Released 2022-09-01* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.1.5>`__

* Fix OpenMP flags in compilers.mk by `@joezuntz <https://github.com/joezuntz>`__ in `#44 <https://github.com/joezuntz/cosmosis/pull/44>`__

v2.1.4
~~~~~~

*Released 2022-08-16* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.1.4>`__

* Allow new parameters to be added using the -v flag by `@joezuntz <https://github.com/joezuntz>`__ in `#41 <https://github.com/joezuntz/cosmosis/pull/41>`__

v2.1.3
~~~~~~

*Released 2022-07-23* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.1.3>`__

This version contains the same contents as 2.1.0:

* Expose new PocoMC sampler by `@joezuntz <https://github.com/joezuntz>`__ in `#37 <https://github.com/joezuntz/cosmosis/pull/37>`__
* Add trace plots for MCMC samplers to ``cosmosis-postprocess``, add ``dynesty`` postprocessing, and allow ``sample=auto`` in ``dynesty`` by `@joezuntz <https://github.com/joezuntz>`__ in `#38 <https://github.com/joezuntz/cosmosis/pull/38>`__

v2.1.2
~~~~~~

*Released 2022-07-22* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.1.2>`__

FIxes tests in v2.1.1

v2.1.1
~~~~~~

*Released 2022-07-22* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.1.1>`__

* Expose new PocoMC sampler by `@joezuntz <https://github.com/joezuntz>`__ in `#37 <https://github.com/joezuntz/cosmosis/pull/37>`__
* Add trace plots for MCMC samplers to ``cosmosis-postprocess``, add ``dynesty`` postprocessing, and allow ``sample=auto`` in ``dynesty`` by `@joezuntz <https://github.com/joezuntz>`__ in `#38 <https://github.com/joezuntz/cosmosis/pull/38>`__

v2.1.1 fixes the version number being wrong in 2.1.0. I should automate this.

v2.0.11
~~~~~~~

*Released 2022-07-13* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.11>`__

* Fix ``zeus`` sampler tuning never ending when ``patience`` is larger than ``nsteps`` by `@SebastianBocquet <https://github.com/SebastianBocquet>`__ in `#35 <https://github.com/joezuntz/cosmosis/pull/35>`__
* Add ``--ports`` option to ``cosmosis-configure`` to print environment settings for MacPorts by `@joezuntz <https://github.com/joezuntz>`__ in `#36 <https://github.com/joezuntz/cosmosis/pull/36>`__

**New Contributors**


* `@SebastianBocquet <https://github.com/SebastianBocquet>`__ made their first contribution in `#35 <https://github.com/joezuntz/cosmosis/pull/35>`__

v2.0.10
~~~~~~~

*Released 2022-06-30* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.10>`__

* Fix the default of the ``no_2d`` postprocessing option in interactive mode and simplify imports from ``cosmosis.postprocessing`` by `@joezuntz <https://github.com/joezuntz>`__ in `#32 <https://github.com/joezuntz/cosmosis/pull/32>`__
* Fix saving vector-valued extra output quantities as multiple columns in the output file by `@joezuntz <https://github.com/joezuntz>`__ in `#33 <https://github.com/joezuntz/cosmosis/pull/33>`__

v2.0.9
~~~~~~

*Released 2022-06-30* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.9>`__

* Fix the default of the ``no_2d`` postprocessing option in interactive mode and simplify imports from ``cosmosis.postprocessing`` by `@joezuntz <https://github.com/joezuntz>`__ in `#32 <https://github.com/joezuntz/cosmosis/pull/32>`__
* Fix saving vector-valued extra output quantities as multiple columns in the output file by `@joezuntz <https://github.com/joezuntz>`__ in `#33 <https://github.com/joezuntz/cosmosis/pull/33>`__

v2.0.8
~~~~~~

*Released 2022-06-01* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.8>`__

* Remove dependency on future module by `@joezuntz <https://github.com/joezuntz>`__ in `#26 <https://github.com/joezuntz/cosmosis/pull/26>`__

v2.0.7
~~~~~~

*Released 2022-05-25* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.7>`__

* Installation and setup fixes for some MacOS systems

v2.0.6
~~~~~~

*Released 2022-05-13* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.6>`__

Adding section names for CAMB power spectra and ensuring new section names are built into the code `@annis <https://github.com/annis>`__ in `#21 <https://github.com/joezuntz/cosmosis/pull/21>`__

This is the same as version v2.0.5 but I forgot to bump the version.

v2.0.4
~~~~~~

*Released 2022-05-10* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.4>`__

* Build the CosmoSIS core library when installing in developer mode with ``pip install -e`` by `@joezuntz <https://github.com/joezuntz>`__ in `#13 <https://github.com/joezuntz/cosmosis/pull/13>`__
* Fix ``cosmomc`` output format to put the posterior in the second column instead of the last by `@joezuntz <https://github.com/joezuntz>`__ in `#17 <https://github.com/joezuntz/cosmosis/pull/17>`__

v2.0.3
~~~~~~

*Released 2022-04-29* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.3>`__

* Fix bug to let single gaussian likelihoods work in Fisher matrices  in `#12 <https://github.com/joezuntz/cosmosis/pull/12>`__

v2.0.2
~~~~~~

*Released 2022-04-27* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.2>`__

* Fix sampler chaining failing when an output file is used, and add a test for it in `#11 <https://github.com/joezuntz/cosmosis/pull/11>`__

v2.0
~~~~

*Released 2022-03-23* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0>`__

This new version is now ready for use.

CosmoSIS Standard Library
-------------------------

The standard library is released less often, so changes are listed by the month in which they were merged, taken from the `merged pull requests <https://github.com/cosmosis-developers/cosmosis-standard-library/pulls?q=is%3Apr+is%3Amerged>`_.

November 2026
~~~~~~~~~~~~~

* Reorganize examples directory (`#249 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/249>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-11-20)
* Fix double scaling of auto-bin GI spectra in mass\_dependent\_ia (`#254 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/254>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-11-20)
* Add the DES Y6 3x2pt likelihood, data and examples, plus new modules from the DES internal fork such as ``photoz_uz``, ``ia_marg`` and ``hmcode2020emu`` (`#248 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/248>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-11-20)
* fix {a-b} per-bin filtering for cross-tracer spectra in project\_2d (`#252 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/252>`__, `@BStoelzner <https://github.com/BStoelzner>`__, 2026-11-13)
* Update the ``camb`` module for CAMB 2.0.5 by setting non-linear lensing explicitly, and test against it in CI (`#251 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/251>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-11-10)
* Fix the continuous-integration workflow with conda package caching, a pinned CosmoSIS 3.27.1 and a reduced macOS test matrix (`#250 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/250>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-11-06)
* Remove the ``-m64`` compiler flag on aarch64 in the ``planck2018`` likelihood build (`#244 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/244>`__, `@beckermr <https://github.com/beckermr>`__, 2026-11-02)

October 2026
~~~~~~~~~~~~

* Correct matter power units and output documentation in the ``camb`` and ``class`` module metadata (`#236 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/236>`__, `@fujikix1102 <https://github.com/fujikix1102>`__, 2026-10-29)

September 2026
~~~~~~~~~~~~~~

* Feature: Add DES Y5 Dovekie Supernova Likelihood and formatted dataset (`#234 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/234>`__, `@CosmicShreya <https://github.com/CosmicShreya>`__, 2026-09-03)

August 2026
~~~~~~~~~~~

* Update the ``camb`` module for CAMB v2 (e.g. ``lens_output_margin``), with related fixes to ``candl``, ``cluster_evs`` and ``spk`` (`#231 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/231>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-08-25)
* Add SP(k) baryon-suppression model (Salcido et al. 2023) (`#225 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/225>`__, `@jemme07 <https://github.com/jemme07>`__, 2026-08-06)

June 2026
~~~~~~~~~

* Updated the DES no-DESI BAO likelihood (`#227 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/227>`__, `@juanejo95 <https://github.com/juanejo95>`__, 2026-06-12)
* Add a DES Y6 shear ratio likelihood that uses only the two geometric ratios (`#160 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/160>`__, `@GisCris <https://github.com/GisCris>`__, 2026-06-08)

May 2026
~~~~~~~~

* Fix the non-Limber calculation in ``project_2d`` when kernels have zero overlap (`#224 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/224>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-05-12)
* Add a ``onepower`` interface module and support for it in ``project_1d`` (`#223 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/223>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2026-05-05)

March 2026
~~~~~~~~~~

* Fix macOS shared-library build issues (`#222 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/222>`__, `@marcpaterno <https://github.com/marcpaterno>`__, 2026-03-31)
* Fix sigma\_8 calculation in camb when zmin is non-zero. (`#219 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/219>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-03-09)
* Add category labels for modules (`#218 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/218>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-03-04)

February 2026
~~~~~~~~~~~~~

* Add version of DES Y6 BAO without DESI tiles (`#216 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/216>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-02-17)
* Implement bin averaging with SACC weights for one-point statistics in the ``sacc`` likelihood (`#207 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/207>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2026-02-17)
* fix reference to the sacc 2-pt module (twopoint not 2pt) (`#215 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/215>`__, `@ajouellette <https://github.com/ajouellette>`__, 2026-02-02)

January 2026
~~~~~~~~~~~~

* Add the TDCOSMO 2025 lensing time-delay likelihood and example pipelines (`#213 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/213>`__, `@martin-millon <https://github.com/martin-millon>`__, 2026-01-28)
* Replace the deprecated pandas ``delim_whitespace`` argument in the ``pantheon_plus_shoes`` likelihood (`#214 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/214>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-01-27)
* Save the data covariance and inverse covariance in the ``candl`` likelihood so it can be used with the Fisher sampler (`#212 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/212>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-01-14)
* Change np.trapz to np.trapezoid everywhere (`#211 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/211>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-01-13)

December 2025
~~~~~~~~~~~~~

* Add KiDS-Legacy cosmic shear analysis pipeline (`#210 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/210>`__, `@BStoelzner <https://github.com/BStoelzner>`__, 2025-12-16)
* Fix the ``consistency`` module when ``cosmomc_theta`` is used as input in non-Lambda dark energy models (`#209 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/209>`__, `@SebastianBocquet <https://github.com/SebastianBocquet>`__, 2025-12-10)
* Fix the ``lollipop`` likelihood interface to use unscaled C_ell values, which biased tau (`#208 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/208>`__, `@SebastianBocquet <https://github.com/SebastianBocquet>`__, 2025-12-09)

October 2025
~~~~~~~~~~~~

* Add the ``project_1d`` module for one-point statistics (stellar mass and luminosity functions) (`#202 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/202>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2025-10-29)
* Interface to use CosmoPower as replacement for CAMB (`#199 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/199>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2025-10-20)
* Speed up the Limber integration in ``project_2d`` when there are many tomographic bins (`#201 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/201>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-10-13)
* Remove duplicated RPATH\_FLAGS in planck makefile (`#200 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/200>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-10-09)

September 2025
~~~~~~~~~~~~~~

* Generalise the HSC, one-point and real-space two-point parts of the ``sacc`` likelihood and add a ``delta_window`` n(z) module (`#195 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/195>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2025-09-26)
* Add a background-only mode and improved parameter handling to the ``class`` module, with a new ``desi_dr2_class.ini`` example (`#170 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/170>`__, `@arthurmloureiro <https://github.com/arthurmloureiro>`__, 2025-09-25)
* Remove enforcement of unit sum weights in sacc\_like (`#194 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/194>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-09-05)
* Remove a repeated call to ``load_kernels`` in ``project_2d`` (`#191 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/191>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-09-04)
* Fix bugs in the ``add_colours``, ``flexible_grid`` and ``la_model_higher_order`` intrinsic alignment modules (`#190 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/190>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-09-04)
* Add a DECam13k likelihood example pipeline and test (`#189 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/189>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-09-02)
* Add DECam13k likelihood (`#188 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/188>`__, `@DhayaaAnbajagane <https://github.com/DhayaaAnbajagane>`__, 2025-09-02)

August 2025
~~~~~~~~~~~

* Add missing parameters, inputs, and outputs to module.yaml files (`#186 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/186>`__, `@Copilot <https://github.com/Copilot>`__, 2025-08-28)
* Add Hillipop and Lollipop likelihoods (`#187 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/187>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-08-25)
* Add complete module.yaml documentation for all CosmoSIS interface modules (`#184 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/184>`__, `@Copilot <https://github.com/Copilot>`__, 2025-08-22)
* Add ell cuts for planck python interface (`#182 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/182>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-08-21)
* Fix the z=0 index of the transfer function output by the ``camb`` module (`#185 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/185>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2025-08-21)
* Fix per-bin IA amplitude parameter names in ``add_intrinsic`` so ``a1_1`` is not confused with the power-law ``a1`` parameter (`#166 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/166>`__, `@rchgomes <https://github.com/rchgomes>`__, 2025-08-21)
* Fix a two-multipole offset in the ACT DR6 and ACT DR6 lite likelihood interfaces and expand their documentation (`#181 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/181>`__, `@itrharrison <https://github.com/itrharrison>`__, 2025-08-21)
* Rename the misnamed DES Y3 ``6x2pt`` example to ``5x2pt`` and add a genuine DES Y3 6x2pt example pipeline (`#177 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/177>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-08-20)

July 2025
~~~~~~~~~

* add act dr6 lite likehood and example (`#180 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/180>`__, `@itrharrison <https://github.com/itrharrison>`__, 2025-07-31)
* Update imports in ``fast_pt`` and the ``project_2d`` FAST-PT tools to support FAST-PT v4 (`#178 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/178>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-07-15)
* Enable saving dataset name in 2pt\_like (`#162 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/162>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-07-03)
* Add DES Y6 BAO likelihood modules, including a 5-bin version, and update the BAO example (`#174 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/174>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-07-03)
* Update the second CI workflow job to test Python 3.10 to 3.13, dropping 3.9 (`#176 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/176>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-07-03)
* Add Python 3.12 and 3.13 to the continuous-integration tests (`#175 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/175>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-07-02)

June 2025
~~~~~~~~~

* Update the ``candl`` likelihood interface for candl 2.0 (`#173 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/173>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-06-27)
* Pin the ``candl`` likelihood to candl 1.x and add DES Y3 Euclid-emulator and DES Y5 supernova example files (`#171 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/171>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-06-05)
* fixed missing import numpy in bbn likelihood (`#168 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/168>`__, `@arthurmloureiro <https://github.com/arthurmloureiro>`__, 2025-06-03)

May 2025
~~~~~~~~

* Fix bug when use\_optical\_depth=False in camb interface (`#165 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/165>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-05-28)
* Pass extra reionization parameters to the tanh reionization model in the ``camb`` module (`#164 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/164>`__, `@ajouellette <https://github.com/ajouellette>`__, 2025-05-28)

April 2025
~~~~~~~~~~

* Add a ``random_fail`` utility module for testing failure handling, and update CI runners (`#158 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/158>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-04-22)
* Add DES-Y5 Supernovae and ACT DR6, and show combined example with DESI (`#157 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/157>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-04-15)

March 2025
~~~~~~~~~~

* Allow setting the mean of a correlated prior in the ``correlated_priors`` module (`#156 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/156>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-03-25)
* Allow saving CMB kappa Fourier-space spectra in the ``2pt`` likelihood files (`#152 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/152>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-03-24)
* Save effective ell values for plotting in the ``planck_py`` (Planck-lite) likelihood (`#153 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/153>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-03-24)
* Add the DESI DR2 BAO likelihood and example pipelines (`#155 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/155>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-03-24)

January 2025
~~~~~~~~~~~~

* Update the NERSC test script (`#151 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/151>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-01-10)
* Fix ``astropy_background`` for newer astropy and the Planck 2018 likelihood build at NERSC (`#150 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/150>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-01-10)
* Fix the Makefile for CLASS 3.2.5 in the ``class`` module (`#149 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/149>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-01-10)
* Add a DES Y3 + Planck example pipeline and update the DES Y3 shear ratio likelihood for newer NumPy (`#148 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/148>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-01-06)

December 2024
~~~~~~~~~~~~~

* Fix the ``class`` module build to use the configured Python and update CI setup (`#147 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/147>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-12-17)

November 2024
~~~~~~~~~~~~~

* Support NumPy 2: update the ``class`` module to CLASS 3.2.5, remove ``interp2d`` usage, drop Python 3.7 and 3.8 (`#146 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/146>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-11-29)
* Update CI tests to use CosmoSIS 3.13 and the latest SciPy (`#145 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/145>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-11-22)
* Add galaxy density and galaxy-shear Cl data types and a ``flip`` option to the ``sacc`` likelihood (`#141 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/141>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-11-21)
* Alias ``scipy.integrate.trapz`` to ``trapezoid`` in the ``fast_pt`` modules for newer SciPy (`#138 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/138>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-11-11)
* Take the growth rate f(z) for RSD in ``project_2d`` from the data block instead of a spline fit (`#143 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/143>`__, `@jessmuir <https://github.com/jessmuir>`__, 2024-11-11)

October 2024
~~~~~~~~~~~~

* Add the ``amod`` module for the ``A_mod`` suppression of non-linear power (Amon & Efstathiou 2022) (`#142 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/142>`__, `@ajouellette <https://github.com/ajouellette>`__, 2024-10-31)

September 2024
~~~~~~~~~~~~~~

* Add a ``candl`` likelihood interface for ACT and SPT CMB likelihoods (`#137 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/137>`__, `@yomori <https://github.com/yomori>`__, 2024-09-12)

August 2024
~~~~~~~~~~~

* Add distance modulus to class (`#135 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/135>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-08-14)
* Fix a bug reading section options in the ``sacc`` likelihood (`#136 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/136>`__, `@ajouellette <https://github.com/ajouellette>`__, 2024-08-14)

July 2024
~~~~~~~~~

* Add the Planck NPIPE likelihood and example pipeline (`#111 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/111>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-07-15)
* Add the DESI DR1 BAO likelihood and DESI example pipelines (`#132 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/132>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-07-15)
* Update ``class``, ``gaussian_window``, ``nz_multirank``, ``add_gammat_point_mass`` and ``baccoemu`` for newer SciPy (`#133 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/133>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-07-13)
* Add CMB shift parameter calculation to camb (`#134 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/134>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-07-12)

May 2024
~~~~~~~~

* Update classy.pyx for cython v3.0.0+ (`#125 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/125>`__, `@AngusWright <https://github.com/AngusWright>`__, 2024-05-24)
* Update module.yaml for the added transfer function output in the camb interface (`#126 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/126>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2024-05-22)

April 2024
~~~~~~~~~~

* Skip the ``baccoemu`` tests on Python 3.12 or newer (`#129 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/129>`__, `@marcpaterno <https://github.com/marcpaterno>`__, 2024-04-23)

February 2024
~~~~~~~~~~~~~

* Add Python 3.12 to the CI tests (`#124 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/124>`__, `@marcpaterno <https://github.com/marcpaterno>`__, 2024-02-06)

January 2024
~~~~~~~~~~~~

* Fix multiple memory leaks in EuclidEmulator2 and make it 3x faster (`#122 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/122>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-01-31)
* Add the HSC Y3 cosmic shear likelihood and example pipelines, with related ``sacc`` likelihood updates (`#105 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/105>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-01-29)
* Remove an import of the removed ``scipy.zeros`` from the eBOSS DR16 ELG likelihood (`#121 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/121>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-01-26)
* Save the transfer function to the data block in the ``camb`` module (`#118 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/118>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2024-01-26)
* Document the TDCOSMO likelihood and rename its example files (`#119 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/119>`__, `@jpratmarti <https://github.com/jpratmarti>`__, 2024-01-26)
* add TDCOSMO likelihood (`#102 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/102>`__, `@martin-millon <https://github.com/martin-millon>`__, 2024-01-09)

November 2023
~~~~~~~~~~~~~

* Fix low-k extrapolation with the ``kmin`` option in the ``camb`` module and respect ``zmid`` in redshift sampling (`#113 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/113>`__, `@tilmantroester <https://github.com/tilmantroester>`__, 2023-11-07)

October 2023
~~~~~~~~~~~~

* Raise an error in ``project_2d`` when ``zmax`` is too low for CMB lensing (`#112 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/112>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-10-30)
* Replace nonstandard ``#elseif`` with ``#elif`` in the Planck 2018 likelihood C code (`#110 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/110>`__, `@marcpaterno <https://github.com/marcpaterno>`__, 2023-10-10)
* Use plik-lite in the Planck example pipelines to reduce the parameter space (`#108 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/108>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-10-10)
* Add Bacco emulator (`#106 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/106>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-10-03)

September 2023
~~~~~~~~~~~~~~

* Fix deprecated cosebis header usage and skip act test if lib not found (`#107 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/107>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-09-29)
* Require the ``act_dr6_lenslike`` package from PyPI in the ACT DR6 lensing likelihood instead of bundling it (`#104 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/104>`__, `@itrharrison <https://github.com/itrharrison>`__, 2023-09-25)

August 2023
~~~~~~~~~~~

* Raise an error in ``camb`` if the ``consistency`` module's ``cosmomc_theta`` conversion is used with a tabulated w(a) (`#103 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/103>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-31)
* Restore Gaussian priors on Planck nuisance parameters in the Planck example pipelines (`#101 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/101>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-25)
* Add a KiDS-1000 COSEBIs-only example pipeline (`#99 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/99>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-23)
* Change the consistency cosmomc\_theta->H0 to use camb (`#94 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/94>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-22)
* Add the DES Y3 + KiDS-1000 hybrid analysis: example pipeline, data file, ``correlated_priors`` module and ``cosebis`` module (`#98 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/98>`__, `@cheymans <https://github.com/cheymans>`__, 2023-08-22)
* Cache Planck and WMAP data in the CI tests to avoid repeated downloads (`#97 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/97>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-22)
* Add metadata keys to the backup GG-only shear section created by ``add_intrinsic`` (`#96 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/96>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-18)
* Improve the ``consistency`` module documentation on relations files and add an ``extra_relations`` option (`#92 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/92>`__, `@itrharrison <https://github.com/itrharrison>`__, 2023-08-11)
* Allow sampling in ``S_8`` in the ``consistency`` module (`#91 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/91>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-11)

July 2023
~~~~~~~~~

* Update demos and example pipelines for CosmoSIS 3 (``verbosity`` replaces ``quiet``) and patch ``fast_pt`` for newer NumPy (`#88 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/88>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-07-28)
* Add the ACT DR6 CMB lensing likelihood and example pipeline (`#87 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/87>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-07-17)
* Allow ``project_2d`` to pair a tracer-matter cross spectrum with different source tomographic bins (`#81 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/81>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2023-07-17)
* Speed up sampling of ``sigma_8`` in the ``camb`` module by computing the transfer function only once (`#86 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/86>`__, `@tilmantroester <https://github.com/tilmantroester>`__, 2023-07-17)
* Fixes to the various module.yaml files (`#85 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/85>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-07-11)
* Add the mean of the shifted n(z) as an output of the ``photoz_bias`` module (`#84 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/84>`__, `@tilmantroester <https://github.com/tilmantroester>`__, 2023-07-11)
* Fix the build of the ``class`` and ``EuclidEmulator2`` modules by installing their Python packages with pip (`#82 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/82>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-07-07)

June 2023
~~~~~~~~~

* Restore ability to read generic P\_gal(k, z) in project\_2d (`#78 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/78>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-06-29)
* Remove a claim in a ``save_2pt.py`` comment that its real-space covariance is not accurate enough for inference (`#76 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/76>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-06-22)

May 2023
~~~~~~~~

* Fix the FAST-PT bias calculation in ``project_2d`` (``fastpt_tools.py``), including swapped ``sig3nl`` and ``sig4`` terms (`#75 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/75>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-05-11)

April 2023
~~~~~~~~~~

* Add the DES Y3 BAO likelihood (``des-y3-bao``) (`#73 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/73>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-04-21)
* Add python 3.11 to the test matrix (`#72 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/72>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-04-18)
* Remove a generated source file from the ``EuclidEmulator2`` module from version control (`#71 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/71>`__, `@marcpaterno <https://github.com/marcpaterno>`__, 2023-04-18)
* Add a BAO example pipeline and CI test, and fix the eBOSS DR16 BAO likelihoods (`#69 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/69>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-04-14)
* Fix magnification in the DES Y3 6x2pt example and a message condition in ``add_magnification`` (`#67 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/67>`__, `@ebaxter <https://github.com/ebaxter>`__, 2023-04-10)
* Add the DES Y3 6x2pt example to the CI tests (`#66 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/66>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-04-06)
* Add the missing scale-cuts file for the DES Y3 6x2pt example (`#65 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/65>`__, `@ebaxter <https://github.com/ebaxter>`__, 2023-04-06)
* Add the DES+SPT/Planck Y3 6x2pt example pipeline, with CMB lensing updates to ``project_2d``, ``2pt_like`` and related modules (`#59 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/59>`__, `@ebaxter <https://github.com/ebaxter>`__, 2023-04-04)

March 2023
~~~~~~~~~~

* Generalize the DES Y3 ``shear_ratio`` likelihood to read the number of ratios per lens bin from its data files (`#52 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/52>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-03-21)
* Adding manual bin division options for smail (`#61 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/61>`__, `@jessmuir <https://github.com/jessmuir>`__, 2023-03-21)
* Change the download URL for Planck likelihood data in ``get-planck-data.sh`` (`#63 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/63>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-03-21)
* Fix the ``theta_H0_range`` option in the ``camb`` module (`#48 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/48>`__, `@msyriac <https://github.com/msyriac>`__, 2023-03-13)
* Add Pantheon+/SHOES and example (`#60 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/60>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-03-03)
* Faster and better-named distance calculations in camb and astropy modules (`#58 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/58>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-03-03)
* Speed up the Pantheon example by using ``astropy_background`` instead of ``camb`` (`#57 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/57>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-03-02)

February 2023
~~~~~~~~~~~~~

* Fix the D(z) growth calculation in the ``camb`` module, which may have affected BAO (`#56 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/56>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-02-28)
* Stop a NameError in camb when reporting another error (`#53 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/53>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-02-03)

January 2023
~~~~~~~~~~~~

* Add planck lite example (`#51 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/51>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-01-29)
* Add a DES Y3 example using ``class``, fixing ``class`` P(k) ordering, distances and massive neutrinos, and ``fast_pt`` grid handling (`#50 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/50>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-01-26)
* Add shear-only des y3 example (`#46 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/46>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-01-03)
* Change CI to use mamba for speed (`#47 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/47>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-01-02)

December 2022
~~~~~~~~~~~~~

* Fix camb f(z) calculation (`#45 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/45>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-12-15)
* Fix output of fsigma8 in class (`#42 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/42>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-12-15)
* Add the option to sample ``sigma_8_input`` instead of ``A_s`` in the ``camb`` module (`#44 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/44>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-12-07)

November 2022
~~~~~~~~~~~~~

* Catch the camb error "dark energy model has w + wa > 0, giving w>0 at high redshift" (`#40 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/40>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-11-10)

October 2022
~~~~~~~~~~~~

* Enable python 3.10 in the CI (`#39 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/39>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-10-14)

September 2022
~~~~~~~~~~~~~~

* Faster 2pt like for binned theory (`#38 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/38>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-09-28)
* Add a ``do_bao`` option to the ``camb`` module to skip BAO quantities for speed, and use it in demos (`#37 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/37>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-09-28)
* Fix OpenMP compiler flags in the ``planck2018`` likelihood Makefile on MacOS (`#36 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/36>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-09-01)

August 2022
~~~~~~~~~~~

* Replace ``cl_to_corr`` with a new version that works with modern scipy and with ``2pt_like`` (`#35 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/35>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-31)
* Save the linear CDM+baryon power spectrum (``cdm_baryon_power_lin``) in the ``class`` module (`#33 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/33>`__, `@SebastianBocquet <https://github.com/SebastianBocquet>`__, 2022-08-26)
* Fix the header of the ``logPkRatio_TNG100.dat`` data file in the ``baryon_power_scaling`` module (`#34 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/34>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-24)
* Restore the ``save_kernels`` option in ``project_2d`` to save the Limber integral kernels to the block (`#32 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/32>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-24)
* Stop class assuming that CC=gcc (`#29 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/29>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-17)
* Add the ``cosmic_emu_2022`` module for the 2022 Mira-Titan emulator, with a DES Y3 example pipeline (`#28 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/28>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-17)
* Fix the name of the ``accurate_massive_neutrino_transfers`` parameter in the ``camb`` module (`#27 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/27>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-15)
* Fix setting HMCode parameters for ``mead2020`` and ``mead2020_feedback`` in the ``camb`` module (`#26 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/26>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-15)
* Add the ``EuclidEmulator2`` non-linear matter power spectrum emulator module and an example pipeline (`#19 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/19>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-10)
* Add a cache for P(k, chi) interpolation in ``project_2d`` to speed up C_ell calculations (`#25 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/25>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-10)

July 2022
~~~~~~~~~

* Remove remaining Python 2 compatibility code from ``2pt`` and ``cl_to_xi_fullsky``, and an unused ``extrapolate`` step from the DES Y3 example (`#22 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/22>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-07-26)
* Add a ``log_w_model`` module for a logarithmic w(z) dark energy model, with an example pipeline (`#21 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/21>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-07-21)
* Catch camb errors and print traceback for first few errors (`#20 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/20>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-07-21)
* Add a WMAP9 data download script, fix the RPATH in the ``wmap9`` likelihood Makefile, and add a CI test (`#18 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/18>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-07-04)
* Fix a crash in one mode of the ``boss_dr12`` likelihood (`#17 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/17>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-07-04)

June 2022
~~~~~~~~~

* Fix the ``gunzip`` command in the ``class`` module Makefile for older systems (`#16 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/16>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-06-20)
* Fix the theta-to-H0 conversion in the ``consistency`` module for curved models (``omega_k``) and speed it up (`#15 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/15>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-06-15)
* Fix loading the GSL cblas library in ``project_2d`` on NERSC (`#14 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/14>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-06-06)

May 2022
~~~~~~~~

* Fix building the ``planck2018`` likelihood on Apple Silicon by removing some compiler flags (`#12 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/12>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-05-25)
* Add MacOS to the conda CI tests and fix the ``class`` build on MacOS (`#13 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/13>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-05-25)
* Expose options to do or skip CMB, MPK in class (`#11 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/11>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-05-23)
* Fix the ``delta_tot_de`` power spectrum name in the ``camb`` module and a section name in ``mf_tinker`` (`#10 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/10>`__, `@annis <https://github.com/annis>`__, 2022-05-16)
* Update the ``class`` module to use CLASS v3.2.0, and use the same neutrino and ``TCMB`` parameter names as ``camb`` (`#9 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/9>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-05-11)
* Fix all demos for CosmoSIS 2.0.3+, including fixes to ``isitgr``, ``extrapolate_power``, ``camb`` D(z) and f(z) outputs, and PPF shear in ``project_2d`` (`#6 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/6>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-05-02)

April 2022
~~~~~~~~~~

* Improve error message in conda when user forgets cosmosis-configure (`#5 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/5>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-04-08)

March 2022
~~~~~~~~~~

* Update the ``project_2d`` documentation and remove unused parameters (`#4 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/4>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-03-25)
* Add ``get-planck-data.sh`` to download the Planck 2018 likelihood data, and a CI test of the ``planck2018`` likelihood (`#3 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/3>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-03-25)
* Add DES Y3 example pipelines and data, the ``tatt`` intrinsic alignment and Y3 shear-ratio modules, and eBOSS likelihoods; update ``2pt_like`` and ``save_2pt`` (`#2 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/2>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-03-23)
