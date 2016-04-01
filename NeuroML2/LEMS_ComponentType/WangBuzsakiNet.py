# -*- coding: utf-8 -*-

import neuroml
from neuroml import __version__

from pyneuroml import pynml
from pyneuroml.lems.LEMSSimulation import LEMSSimulation

import random
random.seed(43297)

ref = 'WangBuzsaki'
nml_doc = neuroml.NeuroMLDocument(id=ref)

# Defie Wang - Buzsáki 1996 PV+ basket cell
def wangBuzsaiBasketCell(id, r, C, v0, gL, eL, spikeThresh,
                        gNa, eNa, alpham_rate, alpham_midpoint, alpham_scale, betam_rate, betam_midpoint_betam_scale,
                        h_q10, alphah_rate, alphah_midpoint, alphah_scale, betah_rate, betah_scale, betah_midpoit,
                        gK, eK, n_q10, alphan_rate, alphan_midpoint, alphan_scale1, alphan_scale2,
                        betan_rate, betan_midpoint, betan_scale):
                      
                            
# Define Wang - Buzsáki 1996 synapse
def wangBuzsakiSynapse(id, g_s, e_s, Vth, Vscale, alpha, beta):
    


# Define Wang - Buzsáki 1996 network
def generate_WB_network(network_id           = ref+'netwok',
                    cell_id,
                    synapse_id,
                    numCells_bc              = 100,
                    connection               = True,
                    connection_probablity,
                    I_mean,
                    I_sigma,
                    temperature              = 37 degC,
                    validate                 = True,
                    generate_LEMS_simulation = True,
                    duration                 = 100,  # ms
                    dt                       = 0.01):
    
    nml_doc = neuroml.NeuroMLDocument(id=network_id)
    
    # Create network
    net = neuroml.Network(id=network_id, type='networkWithTemperature', temperature=temperature)
    net.notes = 'Network generated using libNeuroML v%s'%__version__
    nml_doc.networks.append(net)
    
    # Create population
    pop = neoroml.Population(id=ref+'pop', component=cell_id, type='populationList', size=numCells_bc, color='None')
    if color in not None:
        pop.properties.append(Property('color', color))
    net.populations.append(pop)
    
    # Add connections
    proj = neuroml.Projection(id=ref+'proj' synapse=synapse_id, presynaptic_population=pop, postsynaptic_population=pop)
    
    conn_count = 0
    for in in range(0, numCells_bs):
        for j in range(0, numCell_bs):
            if i != j and rand() < connection_probability:
                connection = neuroml.Connection(id=conn_count, pre_cell_id='../%s[%i]'%(pop, i), pro_cell_id='../%s[%i]'%(pop, j))
                proj.connections.append(connection)
                conn_count += 1
                
    net.projection.append(proj)
    
    # Add outer input
    for i in range(0, numCells_bs):
        expInp = neuroml.ExplicitInput(target='%s[%i]'%(pop.id, i), input= , destination='synapses')
    
    # Write to file
    nml_file = '%sNet.nml'%ref
    print 'Writing network file to:', nml_file, '...'
    neuroml.writers.NeoroMLWriter.write(nml_doc, nml_file)
    
    if validate:
        
        # Validate the NeuroML
        neuroml.utils.validate_neuroml2(nml_file)
        
    if generate_LEMS_simulation:
        
        # Vreate a LEMSSimulation to manage creation of LEMS file
        ls = LEMSSimulation('LEMS_%s'%network_id, duration, dt)
        
        # Point to network as target of simulation
        ls.assign_simulation_target(net.id)
        
        # Incude generated/existing NeuroML2 files
        ls.include_neuroml2_file(nml_file)
        
        # Specify Display and output files
        disp_bc = 'display_bc'
        ls.create_display(disp_bc, 'Basket Cell Voltage trace', '-80', '40')
        
        of_bc = 'volts_file_bc'
        ls.create_output_file(of_bc, 'wangbuzsaki_network.dat')
        
        max_traces = 25
        for i in range(size):
            quantity = '%s[%i]/v'%(pop.id, i)
            if i < max_traces:
                ls.add_line_to_display(disp_bc, 'BC %i: Vm'%i, quantitiy, '1mV', pynml.get_next_hex_color())
            ls.add_column_to_outputfile(of_bc, 'v_%i'%i, quantity)
            
        # Save to LEMS file
        print 'Writing LEMS file...'
        lems_file_name = ls.save_to_file()
        
    else:
        
        ls = None
                
    return ls, lems_file_name


if __name__ == '__main__':
    
    ls, lems_file_name = generate_WB_network(cell_id=, synapse_id=, connection_probability=0.6, I_mean=1, I_sigma=0.1)
    
    # run with jNeuroML
    sim = pynml.run_lems_with_jneuroml(lems_file_name, nogui='True', load_saved_data='False', plot='True')
    
    # run with jNeuroML_NEURON
    # sim = pynml.run_lems_with_jneuroml_neuron(lems_file_name, nogui='True', load_saved_data='False', plot='True')
            
    