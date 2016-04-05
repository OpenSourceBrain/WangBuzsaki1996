### NeuroML2/LEMS version of model 

The model defined in the NEURON has been converted to a LEMS ComponentType defintion: [WangBuzsakiCell.xml](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS_ComponentType/WangBuzsakiCell.xml).

A LEMS file ([LEMS_WangBuzsaki.xml](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS_ComponentType/LEMS_WangBuzsaki.xml)) creates a network with 1 instances of the cell:

    <wangBuzsakiBasketCell id="wb1" spikeThresh="0mV" r="2.82095um" C="1uF_per_cm2" v0="-70mV" gL="0.1mS_per_cm2" eL="-65mV" gNa="35mS_per_cm2" eNa="55mV" alpham_rate="1per_ms" alpham_midpoint="-35mV" alpham_scale="10mV"  betam_rate="4per_ms" betam_midpoint="-60mV" betam_scale="-18mV" h_q="5" alphah_rate="0.07per_ms" alphah_midpoint="-58mV" alphah_scale="-20mV" betah_rate="1per_ms" betah_midpoint="-28mV" betah_scale="-10mV"  gK="9mS_per_cm2" eK="-90mV" n_q="5" alphan_rate="1per_ms" alphan_midpoint="-34mV" alphan_scale1="100mV"  alphan_scale2="10mV" betan_rate="0.125per_ms" betan_midpoint="-44mV" betan_scale="-80mV"/>
                            
applies currents (2 uA/cm2) and runs a simulation with the cell:
  
![](https://raw.githubusercontent.com/OpenSourceBrain/WangBuzsaki1996/master/NeuroML2/LEMS_ComponentType/wangbuzsaki.png)
  
This model can be run locally using [jNeuroML](https://github.com/NeuroML/jNeuroML):
  
    git clone https://github.com/OpenSourceBrain/WangBuzsaki1996.git # Clone GitHub repository
    cd WangBuzsaki1996/NeuroML2/LEMS_ComponentType
    jnml LEMS_WangBuzsaki.xml
    
or using [pyNeuroML](https://github.com/NeuroML/pyNeuroML):
  
    git clone https://github.com/OpenSourceBrain/WangBuzsaki1996.git # Clone GitHub repository
    cd WangBuzsaki1996/NeuroML2/LEMS_ComponentType
    pynml LEMS_WangBuzsaki.xml

--------------------------------------------------------------------------------------------------------------

A .py file ([Fig1_A.py](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS_ComponentType/Fig1_A.py)) gernerates the f-I curve as specifiedin the paper (Fig1.A)

![](https://raw.githubusercontent.com/OpenSourceBrain/WangBuzsaki1996/master/NeuroML2/LEMS_ComponentType/f-I_cure.png)

The script can be run locally using python after installing [pyNeuroML](https://github.com/NeuroML/pyNeuroML) and [pyelectro](https://github.com/NeuralEnsemble/pyelectro)
  
--------------------------------------------------------------------------------------------------------------

A LEMS file ([LEMS_Fig1_C.xml](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS_ComponentType/LEMS_Fig1_C.xml)) creates a network with 2 instances of cells:

    <wangBuzsakiBasketCell id="wb2" spikeThresh="0mV" r="2.82095um" C="1uF_per_cm2" v0="-64.0175mV" gL="0.1mS_per_cm2" eL="-65mV" gNa="35mS_per_cm2" eNa="55mV" alpham_rate="1per_ms" alpham_midpoint="-35mV" alpham_scale="10mV"  betam_rate="4per_ms" betam_midpoint="-60mV" betam_scale="-18mV" h_q="5" alphah_rate="0.07per_ms" alphah_midpoint="-58mV" alphah_scale="-20mV" betah_rate="1per_ms" betah_midpoint="-28mV" betah_scale="-10mV"  gK="9mS_per_cm2" eK="-90mV" n_q="5" alphan_rate="1per_ms" alphan_midpoint="-34mV" alphan_scale1="100mV"  alphan_scale2="10mV" betan_rate="0.125per_ms" betan_midpoint="-44mV" betan_scale="-80mV"/>

connects them with a graded synapse (described in [WangBuzsakiSyapse.xml](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS_ComponentType/WangBuzsakiSynapse.xml)):

    <wangBuzsakiSynapse id="wbs1" g_s="0.1nS" e_s="-75mV" Vth="0mV" Vscale="-2mV" alpha="12per_ms" beta="0.1per_ms"/>

applies currents to the presynaptic cell as specified in the paper (Fig1.C) and runs the simulation:

![](https://raw.githubusercontent.com/OpenSourceBrain/WangBuzsaki1996/master/NeuroML2/LEMS_ComponentType/wangbuzsakisynapse.png)

--------------------------------------------------------------------------------------------------------------

A .py file ([Fig3_A.py](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS_ComponentType/Fig3_A.py)) creates a network with 100 instances of cells, connected in all-to-all manner, applies current as specified in the paper and reproduce the same figures as the original NEURON code.
> Note: these figures are not the same as the figures (Fig3.A) in the paper...

![](https://raw.githubusercontent.com/OpenSourceBrain/WangBuzsaki1996/master/NeuroML2/LEMS_ComponentType/wangbuzsakinetwork.png)

An other .py file ([WangBuzsakiNet.py](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS_ComponentType/WangBuzsakiNet.py)) enables one to create any kind of network (from the [cell](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS_ComponentType/WangBuzsakiCell.xml) and [synapse](https://github.com/OpenSourceBrain/WangBuzsaki1996/blob/master/NeuroML2/LEMS_ComponentType/WangBuzsakiSynapse.xml) described in the .xml files) and export it as a LEMS simulation.
> Eg.: connection probability = 0.6, I_mu = 1 uA/cm2, I_sigma = 0.03 as specified in the paper (Fig8C) 

![](https://raw.githubusercontent.com/OpenSourceBrain/WangBuzsaki1996/master/NeuroML2/LEMS_ComponentType/wangbuzsakinetwork2.png)

The scripts can be run locally using python after installing [pyNeuroML](https://github.com/NeuroML/pyNeuroML) and [libNeuroML](https://github.com/NeuralEnsemble/libNeuroML)







