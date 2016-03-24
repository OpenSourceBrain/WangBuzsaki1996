### Original NEURON scripts for model

These files are the original model scripts for use with the [NEURON simulator](https://www.neuron.yale.edu/neuron/) as [submitted to ModelDB](https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=26997).

To run the scripts, [install NEURON](https://www.neuron.yale.edu/neuron/download) and run:

    git clone https://github.com/OpenSourceBrain/WangBuzsaki1996.git  # clone git repository
    cd WangBuzsaki1996/ModelDB_NEURON
    nrnivmodl  # compile .mod files
    nrngui mosinit.hoc  # runs the example simulation
    press Fig 1A

![](https://raw.githubusercontent.com/OpenSourceBrain/WangBuzsaki1996/master/ModelDB_NEURON/Fig1A.png)

    press Fig 3A
    press Run or Init & Run
    when the simulation stops press Spike plot

![](https://raw.githubusercontent.com/OpenSourceBrain/WangBuzsaki1996/master/ModelDB_NEURON/Fig3A_Spike_plot.png)

    or when the simulation stops press Plot cells A&B
    
![](https://raw.githubusercontent.com/OpenSourceBrain/WangBuzsaki1996/master/ModelDB_NEURON/Fig3A_Plot_cells_AB.png)

Technical notes from the authors:

> In the [original paper](http://www.jneurosci.org/content/16/20/6402.full), current injection is given in unit of uA/cm2. Here we have choosen a cell size of 100 um/cm2 so that nA is equivalent to uA/cm2.

> In the [original paper](http://www.jneurosci.org/content/16/20/6402.full), phi directly alters the time constant as a factor in differential equation. In this implementation phi (phi0) alters celsius appropriately.
