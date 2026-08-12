CosmoSIS: The COSMOlogical Survey Inference System
==================================================

CosmoSIS is a **cosmological parameter estimation code**.  It is now at version |version|

It is a framework for structuring cosmological parameter estimation with a focus on flexibility, re-usability, debugging, verifiability, and code sharing in the form of calculation modules.  It consolidates and connects together existing code for predicting cosmic observables, and makes mapping out experimental likelihoods with a range of different techniques much more accessible.

CosmoSIS is described in `Zuntz et al <http://arxiv.org/abs/1409.3409>`_ - if you make use of it in your research, please cite that paper and include the URL of this repository in your acknowledgments. Thanks!

For help with CosmoSIS you can `open an issue <https://github.com/cosmosis-developers/cosmosis>`_


.. toctree::
   :maxdepth: 1
   :caption: Introduction:

   intro/overview
   intro/installation

.. toctree:: 
   :maxdepth: 1
   :caption: Using CosmoSIS:

   usage/tutorials
   usage/samplers
   usage/parameter_files
   usage/standard_library_overview
   usage/upgrading

.. toctree::
   :maxdepth: 1
   :caption: Bonus Features:

   features/sampler_features
   features/pipeline_features
   features/parameter_features
   features/debugging
   features/Interactive Postprocessing
   features/campaign


.. toctree::
   :maxdepth: 1
   :caption: Writing modules:

   api/api_python
   api/api_c
   api/api_cpp
   api/api_f90
   api/python

.. toctree::
   :maxdepth: 1
   :caption: Reference:

   reference/cosmosis_command_line
   reference/cosmosis_campaign
   reference/cosmosis_configure
   reference/cosmosis_extract
   reference/cosmosis_sample_fisher
   reference/postprocess_command_line
   reference/standard_library_complete


.. toctree::
   :maxdepth: 1
   :caption: Misc:

   reference/scripting
   reference/nersc_examples
   help/faq



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

