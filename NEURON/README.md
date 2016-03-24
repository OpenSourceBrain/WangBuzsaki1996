### NEURON scripts for model

This folder contains files from the original model scripts [ModelDB-26997](https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=26997) and additional tester scripts (in order to create a .mep file, which against LEMS/NeuroML2 implementation could be tested).

![](https://raw.githubusercontent.com/OpenSourceBrain/WangBuzsaki1996/master/NEURON/wangbuzsaki.png)

To run the scripts, [install NEURON](https://www.neuron.yale.edu/neuron/download) and run:

    git clone https://github.com/OpenSourceBrain/WangBuzsaki1996.git  # clone git repository
    cd WangBuzsaki1996/NEURON
    nrnivmodl  # compile .mod files
    nrngui tester.hoc  # runs a simulation (single cell, current clamp) and saves data into wangbuzsaki.dat
