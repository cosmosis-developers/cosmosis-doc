NERSC Submission Examples
=========================


Pantheon Example
-------------------


This bash script will run the Pantheon example in the CosmoSIS Standard Library. Put this in a text file, e.g. `pantheon.sub`, and then submit with `srun pantheon.sub`. This particular example is quick and small enough for the debug queue::

    #!/bin/bash
    # The line above must be the first of the script

    # You can use debug for jobs of less than 30 minutes.
    #SBATCH --qos=debug

    # Wall-clock time limit
    #SBATCH --time=00:10:00

    # See https://docs.nersc.gov/jobs/policy/ for info on numbers
    # of nodes you can have in different queues. One node would be
    # fine for this particular task as it's really fast.
    #SBATCH --nodes=2

    # Run on Haswell CPUs. I haven't tried KNL, it might work.
    #SBATCH --constraint=haswell

    # This assumes you want the LSST NERSC account
    #SBATCH --account=m1727

    # This can be anything you like.
    #SBATCH --job-name=pantheon-cosmosis

    # Job output will be sent to pantheon-cosmosis.log
    #SBATCH --output=%x.log

    # You will get an email when the job completes or times out
    #SBATCH --mail-type=END

    # Now the actual work ....


    # Let's run with 4 threads per process. Each node has 32 cores,
    # so if we use 2 nodes that's 64 cores total, so we want 64/4 = 16 processes.
    # There's also the "hyperthread" thing which could let us have twice as many,
    # but the instructions about that are mixed - somewhere it says not to use it.
    # We export OMP_NUM_THREADS so that it is used internally in camb and elsewhere.
    # NUM_PROCESSES we just use below to tell srun how many tasks to launch
    # It is worth exploring the best numbers to use for your specific chains.

    NUM_PROCESSES=16
    export OMP_NUM_THREADS=4

    # Run the setup script
    source $CFS/des/zuntz/cosmosis-global/setup-cosmosis-nersc

    # Launch the program. Don't forget the --mpi flag!
    srun -u -n ${NUM_PROCESSES} --cpus-per-task ${OMP_NUM_THREADS} cosmosis examples/sn/pantheon.ini --mpi
