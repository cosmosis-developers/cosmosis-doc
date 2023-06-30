The Gridmax sampler
--------------------------------------------------------------------

Naive grid maximum-posterior

+-------------+-----------------------------------------+
| Name        | gridmax                                 |
+-------------+-----------------------------------------+
| Version     | 1.0                                     |
+-------------+-----------------------------------------+
| Author(s)   | CosmoSIS Team                           |
+-------------+-----------------------------------------+
| URL         | https://bitbucket.org/joezuntz/cosmosis |
+-------------+-----------------------------------------+
| Citation(s) |                                         |
+-------------+-----------------------------------------+
| Parallelism | parallel                                |
+-------------+-----------------------------------------+

This sampler is a naive and experimental attempt to try a parallel ML/MAP sampler.

It samples through the dimensions of the space one-by-one, and draws a line of evenly space samples through that dimension, and finds the best fit along that line.

It then changes that parameter value to the best fit, leaving all the others fixed. The idea is that at moves in on a "square spiral" towards the best fit.

The sampling is parallel along the line.

This sampler is experimental and should probably only be used for testing purposes.




Installation
============

No special installation required; everything is packaged with CosmoSIS




Parameters
============

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+----------------+---------+-----------------------------------------------------------------------------+-----------+
| Name           | Type    | Description                                                                 | Default   |
+================+=========+=============================================================================+===========+
| nsteps         | integer | The number of sample points along each line through the space               |           |
+----------------+---------+-----------------------------------------------------------------------------+-----------+
| tolerance      | real    | tolerance for Delta Log Like along one complete loop through the dimensions | 0.1       |
+----------------+---------+-----------------------------------------------------------------------------+-----------+
| output_ini     | string  | if present, save the resulting parameters to a new ini file with this name  | (empty)   |
+----------------+---------+-----------------------------------------------------------------------------+-----------+
| max_iterations | int     | Max number of slices                                                        | 10000     |
+----------------+---------+-----------------------------------------------------------------------------+-----------+


