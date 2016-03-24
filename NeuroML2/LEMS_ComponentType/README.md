### NeuroML2/LEMS version of model 

The model defined in the NEURON has been converted to a LEMS ComponentType defintion: [WangBuzsaki.xml](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS_ComponentType/WangBuzsaki.xml).

A LEMS file ([LEMS_WangBuzsaki.xml](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS_ComponentType/LEMS_WangBuzsaki.xml)) creates a network with 1 instances of the cells:

    <wangBuzsakiBasketCell id="wb1" spikeThresh="0mV" r="2.82095um" C="1uF_per_cm2" v0="-70mV" gL="0.1mS_per_cm2" eL="-65mV" gNa="35mS_per_cm2" eNa="55mV" alpham_rate="1per_ms" alpham_midpoint="-35mV" alpham_scale="10mV"  betam_rate="4per_ms" betam_midpoint="-60mV" betam_scale="-18mV" h_q="5" alphah_rate="0.07per_ms" alphah_midpoint="-58mV" alphah_scale="-20mV" betah_rate="1per_ms" betah_midpoint="-28mV" betah_scale="-10mV"  gK="9mS_per_cm2" eK="-90mV" n_q="5" alphan_rate="1per_ms" alphan_midpoint="-34mV" alphan_scale1="100mV"  alphan_scale2="10mV" betan_rate="0.125per_ms" betan_midpoint="-44mV" betan_scale="-80mV"/>
                            
applies currents as specified in the paper (Fig3.A) and runs a simulation with the cell:
  
![](https://raw.githubusercontent.com/OpenSourceBrain/WangBuzsaki1996/master/NeuroML2/LEMS_ComponentType/wangbuzsaki.png)
  
This model can be run locally using [jNeuroML](https://github.com/NeuroML/jNeuroML):
  
    git clone https://github.com/OpenSourceBrain/WangBuzsaki1996.git # Clone GitHub repository
    cd WangBuzsaki1996/NeuroML2/LEMS_ComponentType
    jnml LEMS_WangBuzsaki.xml
    
or using [pyNeuroML](https://github.com/NeuroML/pyNeuroML):
  
    git clone https://github.com/OpenSourceBrain/WangBuzsaki1996.git # Clone GitHub repository
    cd WangBuzsaki1996/NeuroML2/LEMS_ComponentType
    pynml LEMS_WangBuzsaki.xml
  
