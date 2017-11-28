### NeuroML2/LEMS version of model 

The model defined in the NEURON has been converted to a LEMS using built in NeuroML2 CoreTypes for ion channels and cellular properties: [WangBuzsaki.cell.nml](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS/WangBuzsaki.cell.nml).

A LEMS file ([LEMS_WangBuzsaki.xml](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS/LEMS_WangBuzsaki.xml)) creates a network with 1 instances of the cell, applies currents as specified in the paper (Fig3.A) and runs a simulation with the cell:
  
![](https://raw.githubusercontent.com/OpenSourceBrain/WangBuzsaki1996/master/NeuroML2/LEMS/wangbuzsaki.png)
  
This model can be run locally using [jNeuroML](https://github.com/NeuroML/jNeuroML):
  
    git clone https://github.com/OpenSourceBrain/WangBuzsaki1996.git # Clone GitHub repository
    cd WangBuzsaki1996/NeuroML2/LEMS
    jnml LEMS_WangBuzsaki.xml
    
or using [pyNeuroML](https://github.com/NeuroML/pyNeuroML):
  
    git clone https://github.com/OpenSourceBrain/WangBuzsaki1996.git # Clone GitHub repository
    cd WangBuzsaki1996/NeuroML2/LEMS
    pynml LEMS_WangBuzsaki.xml
  
