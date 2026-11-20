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
* Multinest & Polychord pointer changes by `@joezuntz <https://github.com/joezuntz>`__ in `#251 <https://github.com/cosmosis-developers/cosmosis/pull/251>`__
* Fix MultiNest shared library executable stack by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#250 <https://github.com/cosmosis-developers/cosmosis/pull/250>`__
* Declare h5py for Nautilus installation by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#245 <https://github.com/cosmosis-developers/cosmosis/pull/245>`__
* Update publish workflow actions to current major versions by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#240 <https://github.com/cosmosis-developers/cosmosis/pull/240>`__
* Handle zero within-chain variance in Gelman-Rubin diagnostic by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#246 <https://github.com/cosmosis-developers/cosmosis/pull/246>`__
* Reject negative tabulated prior densities before integration by `@fujikix1102 <https://github.com/fujikix1102>`__ in `#234 <https://github.com/cosmosis-developers/cosmosis/pull/234>`__

v3.26
~~~~~

*Released 2026-09-03* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.26>`__

* Add methods code to serialize/deserialize a DataBlock quickly to a binary file. by `@joezuntz <https://github.com/joezuntz>`__ in `#219 <https://github.com/cosmosis-developers/cosmosis/pull/219>`__
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

* Fixing issue with python changes affecting Inifile.items by `@joezuntz <https://github.com/joezuntz>`__ in `#212 <https://github.com/cosmosis-developers/cosmosis/pull/212>`__

v3.25
~~~~~

*Released 2025-12-03* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.25>`__

* Switch to just trying hermitian=True in numpy by `@joezuntz <https://github.com/joezuntz>`__ in `#210 <https://github.com/cosmosis-developers/cosmosis/pull/210>`__
* Add configure script flag to create conda activate script by `@joezuntz <https://github.com/joezuntz>`__ in `#211 <https://github.com/cosmosis-developers/cosmosis/pull/211>`__

v3.24
~~~~~

*Released 2025-10-29* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.24>`__

* Integrate Cosmopower training by `@andrejdvornik <https://github.com/andrejdvornik>`__ in `#206 <https://github.com/cosmosis-developers/cosmosis/pull/206>`__
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

* Fix fisher method naming inconsistency by `@ajouellette <https://github.com/ajouellette>`__ in `#196 <https://github.com/joezuntz/cosmosis/pull/196>`__
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

* Fix output name for test sampler and MN / PC by `@joezuntz <https://github.com/joezuntz>`__ in `#188 <https://github.com/joezuntz/cosmosis/pull/188>`__
* Fix final nsample value in polychord boosted files by `@joezuntz <https://github.com/joezuntz>`__ in `#189 <https://github.com/joezuntz/cosmosis/pull/189>`__
* Finding a crash in the CI by `@joezuntz <https://github.com/joezuntz>`__ in `#191 <https://github.com/joezuntz/cosmosis/pull/191>`__

v3.20.2
~~~~~~~

*Released 2025-07-08* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.20.2>`__

This is a bugfix release:

* Fix output name for test sampler and MN / PC by `@joezuntz <https://github.com/joezuntz>`__ in `#188 <https://github.com/joezuntz/cosmosis/pull/188>`__
* Fix final nsample value in polychord boosted files by `@joezuntz <https://github.com/joezuntz>`__ in `#189 <https://github.com/joezuntz/cosmosis/pull/189>`__
* Finding a crash in the CI by `@joezuntz <https://github.com/joezuntz>`__ in `#191 <https://github.com/joezuntz/cosmosis/pull/191>`__

v3.20.1
~~~~~~~

*Released 2025-05-06* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.20.1>`__

* Use a more robust fix for a logging crash by `@joezuntz <https://github.com/joezuntz>`__ in `#184 <https://github.com/joezuntz/cosmosis/pull/184>`__
* Handle errors in pybobyqa gracefully by `@joezuntz <https://github.com/joezuntz>`__ in `#185 <https://github.com/joezuntz/cosmosis/pull/185>`__

v3.20
~~~~~

*Released 2025-05-05* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.20>`__

* Handle yaml merge keys by `@ajouellette <https://github.com/ajouellette>`__ in `#180 <https://github.com/joezuntz/cosmosis/pull/180>`__
* Log string array bug by `@joezuntz <https://github.com/joezuntz>`__ in `#183 <https://github.com/joezuntz/cosmosis/pull/183>`__

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
* Allow failures in attributions without killing runs by `@joezuntz <https://github.com/joezuntz>`__ in `#176 <https://github.com/joezuntz/cosmosis/pull/176>`__
* Fix a bug when running the Minuit sampler

v3.18
~~~~~

*Released 2025-03-14* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.18>`__

* Allow starting a sampler from the best-fit point in a chain file by `@joezuntz <https://github.com/joezuntz>`__ in `#175 <https://github.com/joezuntz/cosmosis/pull/175>`__

v3.17
~~~~~

*Released 2025-02-14* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.17>`__

* Rename output files from repeated samplers by `@joezuntz <https://github.com/joezuntz>`__ in `#172 <https://github.com/joezuntz/cosmosis/pull/172>`__

v3.16.1
~~~~~~~

*Released 2025-02-14* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.16.1>`__

* Fix the likelihoods in the reformatted polychord boosted files by `@joezuntz <https://github.com/joezuntz>`__ in `#169 <https://github.com/joezuntz/cosmosis/pull/169>`__
* SMP call count reduce bug by `@joezuntz <https://github.com/joezuntz>`__ in `#171 <https://github.com/joezuntz/cosmosis/pull/171>`__

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

* Expose bobyqa hessian by `@joezuntz <https://github.com/joezuntz>`__ in `#156 <https://github.com/joezuntz/cosmosis/pull/156>`__

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

* Address issue 142 by `@joezuntz <https://github.com/joezuntz>`__ in `#143 <https://github.com/joezuntz/cosmosis/pull/143>`__

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

* Expose n_steps parameter for pocoMC by `@minaskar <https://github.com/minaskar>`__ in `#133 <https://github.com/joezuntz/cosmosis/pull/133>`__

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
* Check for duplicate YAML keys by `@joezuntz <https://github.com/joezuntz>`__ in `#117 <https://github.com/joezuntz/cosmosis/pull/117>`__
* Fixing actions problem with missing gfortran by `@joezuntz <https://github.com/joezuntz>`__ in `#121 <https://github.com/joezuntz/cosmosis/pull/121>`__
* Fix issues with loading campaigns from multiple files by `@joezuntz <https://github.com/joezuntz>`__ in `#125 <https://github.com/joezuntz/cosmosis/pull/125>`__

v3.5.1
~~~~~~

*Released 2024-01-09* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.5.1>`__

* Let campaign output name be overridden per run by `@joezuntz <https://github.com/joezuntz>`__ in `#112 <https://github.com/joezuntz/cosmosis/pull/112>`__

v3.5
~~~~

*Released 2024-01-04* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.5>`__

* Avoid fail on git error by `@joezuntz <https://github.com/joezuntz>`__ in `#110 <https://github.com/joezuntz/cosmosis/pull/110>`__
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

* Bug fixes to from_likelihood_function by `@joezuntz <https://github.com/joezuntz>`__ in `#99 <https://github.com/joezuntz/cosmosis/pull/99>`__

v3.3
~~~~

*Released 2023-09-01* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.3>`__

* Add a method to make a pipeline directly from a single likelihood fun… by `@joezuntz <https://github.com/joezuntz>`__ in `#98 <https://github.com/joezuntz/cosmosis/pull/98>`__

v3.2
~~~~

*Released 2023-08-17* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.2>`__

* Fix setting values under mpi through campaign by `@joezuntz <https://github.com/joezuntz>`__ in `#95 <https://github.com/joezuntz/cosmosis/pull/95>`__, including a change to the default root directory.

v3.1
~~~~

*Released 2023-08-03* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v3.1>`__

* Add postprocessing and resuming apriori sampler by `@joezuntz <https://github.com/joezuntz>`__ in `#94 <https://github.com/joezuntz/cosmosis/pull/94>`__

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

* Updated nautilus integration by `@johannesulf <https://github.com/johannesulf>`__ in `#90 <https://github.com/joezuntz/cosmosis/pull/90>`__
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

* Allow passing new priors to the run_cosmosis method by `@joezuntz <https://github.com/joezuntz>`__ in `#86 <https://github.com/joezuntz/cosmosis/pull/86>`__
* Corner plots &  KDE edge fix by `@joezuntz <https://github.com/joezuntz>`__ in `#87 <https://github.com/joezuntz/cosmosis/pull/87>`__

v2.5
~~~~

*Released 2023-05-25* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.5>`__

* Allow passing new priors to the run_cosmosis method by `@joezuntz <https://github.com/joezuntz>`__ in `#86 <https://github.com/joezuntz/cosmosis/pull/86>`__
* Corner plots &  KDE edge fix by `@joezuntz <https://github.com/joezuntz>`__ in `#87 <https://github.com/joezuntz/cosmosis/pull/87>`__

v2.4.1
~~~~~~

*Released 2023-04-24* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.4.1>`__

* support for features in nautilus 0.6 by `@johannesulf <https://github.com/johannesulf>`__ in `#83 <https://github.com/joezuntz/cosmosis/pull/83>`__
* Add a test of additional nautilus options by `@joezuntz <https://github.com/joezuntz>`__ in `#84 <https://github.com/joezuntz/cosmosis/pull/84>`__

v2.4
~~~~

*Released 2023-04-24* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.4>`__

* support for features in nautilus 0.6 by `@johannesulf <https://github.com/johannesulf>`__ in `#83 <https://github.com/joezuntz/cosmosis/pull/83>`__
* Add a test of additional nautilus options by `@joezuntz <https://github.com/joezuntz>`__ in `#84 <https://github.com/joezuntz/cosmosis/pull/84>`__

v2.3.2
~~~~~~

*Released 2023-03-27* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.3.2>`__

* Bugfix for list sampler with vector quantities as extra output by `@BStoelzner <https://github.com/BStoelzner>`__ in `#76 <https://github.com/joezuntz/cosmosis/pull/76>`__
* Fix dynesty and nautilus returing posterior instead of likelihood by `@joezuntz <https://github.com/joezuntz>`__ in `#82 <https://github.com/joezuntz/cosmosis/pull/82>`__

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

* Add option to draw starting sample from proposal by `@joezuntz <https://github.com/joezuntz>`__ in `#63 <https://github.com/joezuntz/cosmosis/pull/63>`__
* Better error messages and tests for them by `@joezuntz <https://github.com/joezuntz>`__ in `#66 <https://github.com/joezuntz/cosmosis/pull/66>`__
* Fixes for MN and PC output of vector quantities by `@joezuntz <https://github.com/joezuntz>`__ in `#71 <https://github.com/joezuntz/cosmosis/pull/71>`__

v2.2.4
~~~~~~

*Released 2023-02-20* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.2.4>`__

* Add option to draw starting sample from proposal by `@joezuntz <https://github.com/joezuntz>`__ in `#63 <https://github.com/joezuntz/cosmosis/pull/63>`__
* Better error messages and tests for them by `@joezuntz <https://github.com/joezuntz>`__ in `#66 <https://github.com/joezuntz/cosmosis/pull/66>`__
* Fixes for MN and PC output of vector quantities by `@joezuntz <https://github.com/joezuntz>`__ in `#71 <https://github.com/joezuntz/cosmosis/pull/71>`__

v2.2.3
~~~~~~

*Released 2022-11-08* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.2.3>`__

* Add missing requirements and remove redundancies by `@marcpaterno <https://github.com/marcpaterno>`__ in `#55 <https://github.com/joezuntz/cosmosis/pull/55>`__
* Fix hard crash when using wrong array types with put/get by `@joezuntz <https://github.com/joezuntz>`__ in `#56 <https://github.com/joezuntz/cosmosis/pull/56>`__
* Add 3.11 to CI by `@joezuntz <https://github.com/joezuntz>`__ in `#57 <https://github.com/joezuntz/cosmosis/pull/57>`__
* Add sklearn into dependencies by `@joezuntz <https://github.com/joezuntz>`__ in `#58 <https://github.com/joezuntz/cosmosis/pull/58>`__

v2.2.2
~~~~~~

*Released 2022-10-17* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.2.2>`__

* Enable python 3.10 in the CI by `@joezuntz <https://github.com/joezuntz>`__ in `#49 <https://github.com/joezuntz/cosmosis/pull/49>`__
* Add a way to avoid launching subprocesses by `@joezuntz <https://github.com/joezuntz>`__ in `#50 <https://github.com/joezuntz/cosmosis/pull/50>`__

CosmoSIS previously launched git in a subprocess to try and find out the git revisions of various directories. This causes problems on the NERSC Perlmutter machine because that's technically undefined behaviour under MPI and the Cray MPI implementation actually does do strange things.  CosmoSIS will now try to use the Dulwich library to find the versions without using a subprocess, and in either case the setting the new ``COSMOSIS_NO_SUBPROCESS`` environment variable to ``1`` will stop any subprocesses from being launched.

We also now test CosmoSIS under python 3.10, so that version is now fully supported.

v2.2.1
~~~~~~

*Released 2022-10-17* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.2.1>`__

* Enable python 3.10 in the CI by `@joezuntz <https://github.com/joezuntz>`__ in `#49 <https://github.com/joezuntz/cosmosis/pull/49>`__
* Add a way to avoid launching subprocesses by `@joezuntz <https://github.com/joezuntz>`__ in `#50 <https://github.com/joezuntz/cosmosis/pull/50>`__

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
* Generate trace plots and improve dynesty integration by `@joezuntz <https://github.com/joezuntz>`__ in `#38 <https://github.com/joezuntz/cosmosis/pull/38>`__

v2.1.2
~~~~~~

*Released 2022-07-22* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.1.2>`__

FIxes tests in v2.1.1

v2.1.1
~~~~~~

*Released 2022-07-22* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.1.1>`__

* Expose new PocoMC sampler by `@joezuntz <https://github.com/joezuntz>`__ in `#37 <https://github.com/joezuntz/cosmosis/pull/37>`__
* Generate trace plots and improve dynesty integration by `@joezuntz <https://github.com/joezuntz>`__ in `#38 <https://github.com/joezuntz/cosmosis/pull/38>`__

v2.1.1 fixes the version number being wrong in 2.1.0. I should automate this.

v2.0.11
~~~~~~~

*Released 2022-07-13* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.11>`__

* Enable zeus patience for small nsteps by `@SebastianBocquet <https://github.com/SebastianBocquet>`__ in `#35 <https://github.com/joezuntz/cosmosis/pull/35>`__
* Add macports flags by `@joezuntz <https://github.com/joezuntz>`__ in `#36 <https://github.com/joezuntz/cosmosis/pull/36>`__

**New Contributors**


* `@SebastianBocquet <https://github.com/SebastianBocquet>`__ made their first contribution in `#35 <https://github.com/joezuntz/cosmosis/pull/35>`__

v2.0.10
~~~~~~~

*Released 2022-06-30* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.10>`__

* Fix no_2d in interactive mode and make imports nicer by `@joezuntz <https://github.com/joezuntz>`__ in `#32 <https://github.com/joezuntz/cosmosis/pull/32>`__
* Fix vector extra outputs by `@joezuntz <https://github.com/joezuntz>`__ in `#33 <https://github.com/joezuntz/cosmosis/pull/33>`__

v2.0.9
~~~~~~

*Released 2022-06-30* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.9>`__

* Fix no_2d in interactive mode and make imports nicer by `@joezuntz <https://github.com/joezuntz>`__ in `#32 <https://github.com/joezuntz/cosmosis/pull/32>`__
* Fix vector extra outputs by `@joezuntz <https://github.com/joezuntz>`__ in `#33 <https://github.com/joezuntz/cosmosis/pull/33>`__

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

* Enable developer installs by `@joezuntz <https://github.com/joezuntz>`__ in `#13 <https://github.com/joezuntz/cosmosis/pull/13>`__
* Fix CosmoMC output format by `@joezuntz <https://github.com/joezuntz>`__ in `#17 <https://github.com/joezuntz/cosmosis/pull/17>`__

v2.0.3
~~~~~~

*Released 2022-04-29* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.3>`__

* Fix bug to let single gaussian likelihoods work in Fisher matrices  in `#12 <https://github.com/joezuntz/cosmosis/pull/12>`__

v2.0.2
~~~~~~

*Released 2022-04-27* — `release page <https://github.com/cosmosis-developers/cosmosis/releases/tag/v2.0.2>`__

* Fixed bug in sampler chaining and added associated test in `#11 <https://github.com/joezuntz/cosmosis/pull/11>`__

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
* DES Y6 Data Release (`#248 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/248>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-11-20)
* fix {a-b} per-bin filtering for cross-tracer spectra in project\_2d (`#252 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/252>`__, `@BStoelzner <https://github.com/BStoelzner>`__, 2026-11-13)
* Camb 2.0.5 (`#251 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/251>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-11-10)
* Testing CI Fixes (`#250 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/250>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-11-06)
* fix: remove m64 for aarch64 without effecting other flags (`#244 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/244>`__, `@beckermr <https://github.com/beckermr>`__, 2026-11-02)

October 2026
~~~~~~~~~~~~

* Correct matter power output documentation (`#236 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/236>`__, `@fujikix1102 <https://github.com/fujikix1102>`__, 2026-10-29)

September 2026
~~~~~~~~~~~~~~

* Feature: Add DES Y5 Dovekie Supernova Likelihood and formatted dataset (`#234 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/234>`__, `@CosmicShreya <https://github.com/CosmicShreya>`__, 2026-09-03)

August 2026
~~~~~~~~~~~

* Updates for CAMB version 2 (`#231 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/231>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-08-25)
* Add SP(k) baryon-suppression model (Salcido et al. 2023) (`#225 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/225>`__, `@jemme07 <https://github.com/jemme07>`__, 2026-08-06)

June 2026
~~~~~~~~~

* Updated the DES no-DESI BAO likelihood (`#227 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/227>`__, `@juanejo95 <https://github.com/juanejo95>`__, 2026-06-12)
* Sr desy6 likelihood (`#160 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/160>`__, `@GisCris <https://github.com/GisCris>`__, 2026-06-08)

May 2026
~~~~~~~~

* Cope with there being zero overlap in the kernels in the non-limber 2pt (`#224 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/224>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-05-12)
* Added onepower interface to CSL (`#223 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/223>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2026-05-05)

March 2026
~~~~~~~~~~

* Fix macOS shared-library build issues (`#222 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/222>`__, `@marcpaterno <https://github.com/marcpaterno>`__, 2026-03-31)
* Fix sigma\_8 calculation in camb when zmin is non-zero. (`#219 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/219>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-03-09)
* Add category labels for modules (`#218 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/218>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-03-04)

February 2026
~~~~~~~~~~~~~

* Add version of DES Y6 BAO without DESI tiles (`#216 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/216>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-02-17)
* Implemented bin average for 1 point statistics (`#207 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/207>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2026-02-17)
* fix reference to the sacc 2-pt module (twopoint not 2pt) (`#215 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/215>`__, `@ajouellette <https://github.com/ajouellette>`__, 2026-02-02)

January 2026
~~~~~~~~~~~~

* Including TDCOSMO2025 results (`#213 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/213>`__, `@martin-millon <https://github.com/martin-millon>`__, 2026-01-28)
* Checking for problems with pandas deprecating a parameter name (`#214 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/214>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-01-27)
* Add ingredients for candl to do fisher (`#212 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/212>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-01-14)
* Change np.trapz to np.trapezoid everywhere (`#211 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/211>`__, `@joezuntz <https://github.com/joezuntz>`__, 2026-01-13)

December 2025
~~~~~~~~~~~~~

* Add KiDS-Legacy cosmic shear analysis pipeline (`#210 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/210>`__, `@BStoelzner <https://github.com/BStoelzner>`__, 2025-12-16)
* fix consistency relation with cosmomc\_theta as input in non-Lambda DE models (`#209 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/209>`__, `@SebastianBocquet <https://github.com/SebastianBocquet>`__, 2025-12-10)
* lollipop takes unscaled Cls (`#208 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/208>`__, `@SebastianBocquet <https://github.com/SebastianBocquet>`__, 2025-12-09)

October 2025
~~~~~~~~~~~~

* PR to add 1pt (SMF and LF) functionality to CSL (`#202 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/202>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2025-10-29)
* Interface to use CosmoPower as replacement for CAMB (`#199 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/199>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2025-10-20)
* Faster limber (`#201 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/201>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-10-13)
* Remove duplicated RPATH\_FLAGS in planck makefile (`#200 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/200>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-10-09)

September 2025
~~~~~~~~~~~~~~

* Sacc smf (`#195 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/195>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2025-09-26)
* Update class interface (`#170 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/170>`__, `@arthurmloureiro <https://github.com/arthurmloureiro>`__, 2025-09-25)
* Remove enforcement of unit sum weights in sacc\_like (`#194 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/194>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-09-05)
* Remove an embarassing repeated call to load\_kernels (`#191 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/191>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-09-04)
* Some fixes for old IA modules (`#190 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/190>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-09-04)
* Add decam test (`#189 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/189>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-09-02)
* Add DECam13k likelihood (`#188 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/188>`__, `@DhayaaAnbajagane <https://github.com/DhayaaAnbajagane>`__, 2025-09-02)

August 2025
~~~~~~~~~~~

* Add missing parameters, inputs, and outputs to module.yaml files (`#186 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/186>`__, `@Copilot <https://github.com/Copilot>`__, 2025-08-28)
* Add Hillipop and Lollipop likelihoods (`#187 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/187>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-08-25)
* Add complete module.yaml documentation for all CosmoSIS interface modules (`#184 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/184>`__, `@Copilot <https://github.com/Copilot>`__, 2025-08-22)
* Add ell cuts for planck python interface (`#182 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/182>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-08-21)
* Correct z=0 index in transfer function (`#185 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/185>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2025-08-21)
* fixed bug in perbin param name (`#166 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/166>`__, `@rchgomes <https://github.com/rchgomes>`__, 2025-08-21)
* ACT dr6 fixes (`#181 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/181>`__, `@itrharrison <https://github.com/itrharrison>`__, 2025-08-21)
* Rename 6x2pt (`#177 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/177>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-08-20)

July 2025
~~~~~~~~~

* add act dr6 lite likehood and example (`#180 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/180>`__, `@itrharrison <https://github.com/itrharrison>`__, 2025-07-31)
* Update imports to allow fastpy v4 (`#178 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/178>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-07-15)
* Enable saving dataset name in 2pt\_like (`#162 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/162>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-07-03)
* DES Y6 bao (`#174 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/174>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-07-03)
* Add to second wf group (`#176 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/176>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-07-03)
* Add pythons 12 and 13 to CI (`#175 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/175>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-07-02)

June 2025
~~~~~~~~~

* Update for candl 2.0 (`#173 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/173>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-06-27)
* Candl issue (`#171 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/171>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-06-05)
* fixed missing import numpy in bbn likelihood (`#168 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/168>`__, `@arthurmloureiro <https://github.com/arthurmloureiro>`__, 2025-06-03)

May 2025
~~~~~~~~

* Fix bug when use\_optical\_depth=False in camb interface (`#165 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/165>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-05-28)
* pass extra reionization params to simple tau model (`#164 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/164>`__, `@ajouellette <https://github.com/ajouellette>`__, 2025-05-28)

April 2025
~~~~~~~~~~

* Random fail module (`#158 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/158>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-04-22)
* Add DES-Y5 Supernovae and ACT DR6, and show combined example with DESI (`#157 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/157>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-04-15)

March 2025
~~~~~~~~~~

* Allow setting the mean of a correlated prior (`#156 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/156>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-03-25)
* Allow saving CMB Kappa 2pt data (`#152 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/152>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-03-24)
* Have the planck-lite code save the effective ell values for plotting (`#153 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/153>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-03-24)
* Add DESI DR2 (`#155 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/155>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-03-24)

January 2025
~~~~~~~~~~~~

* change nersc test some more (`#151 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/151>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-01-10)
* NERSC updates (`#150 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/150>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-01-10)
* fix makefile (`#149 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/149>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-01-10)
* DES + planck and related update (`#148 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/148>`__, `@joezuntz <https://github.com/joezuntz>`__, 2025-01-06)

December 2024
~~~~~~~~~~~~~

* Remove mambaforge spec (`#147 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/147>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-12-17)

November 2024
~~~~~~~~~~~~~

* Numpy v2 (`#146 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/146>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-11-29)
* CI scipy update (`#145 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/145>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-11-22)
* Add more data types and features to sacc (`#141 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/141>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-11-21)
* Alias for trapz (`#138 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/138>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-11-11)
* Get f(z) used for RSD calcs from datablock instead of a spline fit (`#143 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/143>`__, `@jessmuir <https://github.com/jessmuir>`__, 2024-11-11)

October 2024
~~~~~~~~~~~~

* A\_mod suppression of non-linear power (`#142 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/142>`__, `@ajouellette <https://github.com/ajouellette>`__, 2024-10-31)

September 2024
~~~~~~~~~~~~~~

* Implement interface with Candl (`#137 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/137>`__, `@yomori <https://github.com/yomori>`__, 2024-09-12)

August 2024
~~~~~~~~~~~

* Add distance modulus to class (`#135 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/135>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-08-14)
* Fix bug in sacc likelihood (`#136 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/136>`__, `@ajouellette <https://github.com/ajouellette>`__, 2024-08-14)

July 2024
~~~~~~~~~

* Add Planck NPIPE (`#111 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/111>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-07-15)
* DESI likelihoods and examples (`#132 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/132>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-07-15)
* Scipy 2.0 updates (`#133 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/133>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-07-13)
* Add CMB shift parameter calculation to camb (`#134 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/134>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-07-12)

May 2024
~~~~~~~~

* Update classy.pyx for cython v3.0.0+ (`#125 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/125>`__, `@AngusWright <https://github.com/AngusWright>`__, 2024-05-24)
* Update module.yaml for the added transfer function output in the camb interface (`#126 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/126>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2024-05-22)

April 2024
~~~~~~~~~~

* Do not run baccoemu on python 3.12 or newer (`#129 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/129>`__, `@marcpaterno <https://github.com/marcpaterno>`__, 2024-04-23)

February 2024
~~~~~~~~~~~~~

* Add support for Python 3.12 (`#124 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/124>`__, `@marcpaterno <https://github.com/marcpaterno>`__, 2024-02-06)

January 2024
~~~~~~~~~~~~

* Fix multiple memory leaks in EuclidEmulator2 and make it 3x faster (`#122 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/122>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-01-31)
* HSC Cosmic shear likelihood (`#105 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/105>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-01-29)
* Remove import of scipy zeros (`#121 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/121>`__, `@joezuntz <https://github.com/joezuntz>`__, 2024-01-26)
* Transfer function to data block (`#118 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/118>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2024-01-26)
* Documenting TDCosmo new likelihood (`#119 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/119>`__, `@jpratmarti <https://github.com/jpratmarti>`__, 2024-01-26)
* add TDCOSMO likelihood (`#102 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/102>`__, `@martin-millon <https://github.com/martin-millon>`__, 2024-01-09)

November 2023
~~~~~~~~~~~~~

* Fix low-k extrapolation issue, consistent sampling in z (`#113 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/113>`__, `@tilmantroester <https://github.com/tilmantroester>`__, 2023-11-07)

October 2023
~~~~~~~~~~~~

* Add error on zmax too low for cmb lensing (`#112 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/112>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-10-30)
* Replace nonstandard #elseif with standard #elif (`#110 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/110>`__, `@marcpaterno <https://github.com/marcpaterno>`__, 2023-10-10)
* Use plik-lite in examples to reduce parameter space. (`#108 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/108>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-10-10)
* Add Bacco emulator (`#106 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/106>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-10-03)

September 2023
~~~~~~~~~~~~~~

* Fix deprecated cosebis header usage and skip act test if lib not found (`#107 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/107>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-09-29)
* act\_dr6\_lenslike code from PyPI (`#104 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/104>`__, `@itrharrison <https://github.com/itrharrison>`__, 2023-09-25)

August 2023
~~~~~~~~~~~

* Checks on theta for w models (`#103 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/103>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-31)
* Put planck priors back in (`#101 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/101>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-25)
* Add kids-only cosebis likelihood (`#99 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/99>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-23)
* Change the consistency cosmomc\_theta->H0 to use camb (`#94 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/94>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-22)
* DES-Y3+KiDS-1000 (`#98 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/98>`__, `@cheymans <https://github.com/cheymans>`__, 2023-08-22)
* Cache wmap and planck files properly to avoid multiple downloads (`#97 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/97>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-22)
* Add metadata keys to backup gg-only shear section (`#96 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/96>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-18)
* Imrprove consistency relations docs, allow adding extras (`#92 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/92>`__, `@itrharrison <https://github.com/itrharrison>`__, 2023-08-11)
* Allow sampling in S\_8 (`#91 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/91>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-08-11)

July 2023
~~~~~~~~~

* CosmoSIS 3 changes (`#88 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/88>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-07-28)
* Act DR6 lensing likelihood (`#87 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/87>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-07-17)
* Changes to project\_2d.py to allow for different source bins (`#81 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/81>`__, `@andrejdvornik <https://github.com/andrejdvornik>`__, 2023-07-17)
* Better sampling of sigma\_8 (`#86 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/86>`__, `@tilmantroester <https://github.com/tilmantroester>`__, 2023-07-17)
* Fixes to the various module.yaml files (`#85 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/85>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-07-11)
* Allow output of mean of biased n(z) (`#84 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/84>`__, `@tilmantroester <https://github.com/tilmantroester>`__, 2023-07-11)
* Testing new class installation (`#82 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/82>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-07-07)

June 2023
~~~~~~~~~

* Restore ability to read generic P\_gal(k, z) in project\_2d (`#78 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/78>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-06-29)
* Make comment in save\_2pt.py less slanderous (`#76 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/76>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-06-22)

May 2023
~~~~~~~~

* Cherry-pick changes from des-science to fix fast-pt (`#75 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/75>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-05-11)

April 2023
~~~~~~~~~~

* Add des y3 bao (`#73 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/73>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-04-21)
* Add python 3.11 to the test matrix (`#72 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/72>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-04-18)
* Remove generated source file from version control (`#71 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/71>`__, `@marcpaterno <https://github.com/marcpaterno>`__, 2023-04-18)
* Add BAO to CI and fix some of them (`#69 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/69>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-04-14)
* fixing magnification (`#67 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/67>`__, `@ebaxter <https://github.com/ebaxter>`__, 2023-04-10)
* Add 6x2pt to github actions (`#66 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/66>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-04-06)
* fixing scale cuts (`#65 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/65>`__, `@ebaxter <https://github.com/ebaxter>`__, 2023-04-06)
* Code for running DES+SPT Year 3 6x2pt analysis (`#59 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/59>`__, `@ebaxter <https://github.com/ebaxter>`__, 2023-04-04)

March 2023
~~~~~~~~~~

* Generalize shear ratio DES code (`#52 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/52>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-03-21)
* Adding manual bin division options for smail (`#61 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/61>`__, `@jessmuir <https://github.com/jessmuir>`__, 2023-03-21)
* Change host for planck data (`#63 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/63>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-03-21)
* Fix theta\_H0\_range usage by adding a key to dict (`#48 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/48>`__, `@msyriac <https://github.com/msyriac>`__, 2023-03-13)
* Add Pantheon+/SHOES and example (`#60 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/60>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-03-03)
* Faster and better-named distance calculations in camb and astropy modules (`#58 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/58>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-03-03)
* Faster version of pantheon (`#57 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/57>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-03-02)

February 2023
~~~~~~~~~~~~~

* Fix calculation of D(z) (`#56 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/56>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-02-28)
* Stop a NameError in camb when reporting another error (`#53 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/53>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-02-03)

January 2023
~~~~~~~~~~~~

* Add planck lite example (`#51 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/51>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-01-29)
* Class version of DES Y3 (`#50 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/50>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-01-26)
* Add shear-only des y3 example (`#46 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/46>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-01-03)
* Change CI to use mamba for speed (`#47 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/47>`__, `@joezuntz <https://github.com/joezuntz>`__, 2023-01-02)

December 2022
~~~~~~~~~~~~~

* Fix camb f(z) calculation (`#45 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/45>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-12-15)
* Fix output of fsigma8 in class (`#42 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/42>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-12-15)
* Sample sigma 8 in camb (`#44 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/44>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-12-07)

November 2022
~~~~~~~~~~~~~

* Catch the camb error "dark energy model has w + wa > 0, giving w>0 at high redshift" (`#40 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/40>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-11-10)

October 2022
~~~~~~~~~~~~

* Enable python 3.10 in the CI (`#39 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/39>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-10-14)

September 2022
~~~~~~~~~~~~~~

* Faster 2pt like for binned theory (`#38 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/38>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-09-28)
* Add option to not do BAO and speed up camb (`#37 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/37>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-09-28)
* Fixes for MacOS OpenMP (v2) (`#36 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/36>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-09-01)

August 2022
~~~~~~~~~~~

* Update cl\_to\_corr (`#35 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/35>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-31)
* save CDM+baryon linear power spectrum (`#33 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/33>`__, `@SebastianBocquet <https://github.com/SebastianBocquet>`__, 2022-08-26)
* Fix header in file logPkRatio\_TNG100.dat (`#34 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/34>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-24)
* Restore the option to save the kernels used in the Limber integral to the block (`#32 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/32>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-24)
* Stop class assuming that CC=gcc (`#29 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/29>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-17)
* Add Mira Titan 2022 (`#28 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/28>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-17)
* Fix name of parameter accurate\_massive\_neutrino\_transfers (`#27 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/27>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-15)
* Fix setting parameters for mead2020 and mead2020\_feedback (`#26 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/26>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-15)
* Euclid Emulator 2 (`#19 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/19>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-10)
* P(k, chi) interpolate cache (`#25 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/25>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-08-10)

July 2022
~~~~~~~~~

* Fixes from removal of py2 compatibility (`#22 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/22>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-07-26)
* Logarithmic w(z) model example (`#21 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/21>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-07-21)
* Catch camb errors and print traceback for first few errors (`#20 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/20>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-07-21)
* WMAP9 downloader and Makefile fixes (`#18 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/18>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-07-04)
* fix crash in one boss mode (`#17 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/17>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-07-04)

June 2022
~~~~~~~~~

* Fix gunzip command for older systems (`#16 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/16>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-06-20)
* Fix one path in consistency and speed up (`#15 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/15>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-06-15)
* Fix cblas gsl import on NERSC (`#14 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/14>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-06-06)

May 2022
~~~~~~~~

* Fixes for Apple Silicon (`#12 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/12>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-05-25)
* Add MacOS to conda test (`#13 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/13>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-05-25)
* Expose options to do or skip CMB, MPK in class (`#11 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/11>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-05-23)
* Fixed typo for delta\_tot\_de and section headings (`#10 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/10>`__, `@annis <https://github.com/annis>`__, 2022-05-16)
* Update to class v3.2.0 (`#9 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/9>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-05-11)
* Fix the demos and their ingredients (`#6 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/6>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-05-02)

April 2022
~~~~~~~~~~

* Improve error message in conda when user forgets cosmosis-configure (`#5 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/5>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-04-08)

March 2022
~~~~~~~~~~

* Residual Y3 changes (`#4 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/4>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-03-25)
* Planck downloader (`#3 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/3>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-03-25)
* DES Y3 Changes (`#2 <https://github.com/cosmosis-developers/cosmosis-standard-library/pull/2>`__, `@joezuntz <https://github.com/joezuntz>`__, 2022-03-23)
