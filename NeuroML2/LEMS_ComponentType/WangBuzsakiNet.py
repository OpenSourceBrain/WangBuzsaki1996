# -*- coding: utf-8 -*-

import neuroml
from neuroml import __version__

from pyneuroml import pynml
from pyneuroml.lems.LEMSSimulation import LEMSSimulation

import numpy.random as rnd
rnd.seed(43297)

ref = 'WangBuzsaki'
nml_doc = neuroml.NeuroMLDocument(id=ref)

# Define Wang - Buzsáki 1996 network
def generate_WB_network(cell_id,
                    synapse_id,
                    connection_probability,
                    I_mean,
                    I_sigma,
                    generate_LEMS_simulation,
                    x_size                   = 100,
                    y_size                   = 100,
                    z_size                   = 100,
                    network_id               = ref+'Network',
                    numCells_bc              = 10,
                    color                    = '0 0 1',
                    connection               = True,
                    temperature              = '37 degC',
                    validate                 = True,
                    duration                 = 500,  # ms
                    dt                       = 0.01):
    
    nml_doc = neuroml.NeuroMLDocument(id=network_id)
    nml_doc.includes.append(neuroml.IncludeType(href='WangBuzsakiCell.xml'))
    nml_doc.includes.append(neuroml.IncludeType(href='WangBuzsakiSynapse.xml'))
    
    
    # Create network
    net = neuroml.Network(id=network_id, type='networkWithTemperature', temperature=temperature)
    net.notes = 'Network generated using libNeuroML v%s'%__version__
    nml_doc.networks.append(net)
    
    
    # Create population
    pop = neuroml.Population(id=ref+'pop', component=cell_id, type='populationList', size=numCells_bc)
    if color is not None:
        pop.properties.append(neuroml.Property('color', color))
    net.populations.append(pop)
    
    for i in range(0, numCells_bc):
        inst = neuroml.Instance(id=i)
        pop.instances.append(inst)
        inst.location = neuroml.Location(x=str(x_size*rnd.random()), y=str(y_size*rnd.random()), z=str(z_size*rnd.random()))
        
    
    # Add connections
    proj = neuroml.Projection(id=ref+'proj', synapse=synapse_id, presynaptic_population=pop.id, postsynaptic_population=pop.id)
    
    conn_count = 0
    for i in range(0, numCells_bc):
        for j in range(0, numCells_bc):
            if i != j and rnd.random() < connection_probability:
                connection = neuroml.Connection(id=conn_count, pre_cell_id='../%s/%i/%s'%(pop.id, i, cell_id), post_cell_id='../%s/%i/%s'%(pop.id, j, cell_id))
                proj.connections.append(connection)
                conn_count += 1
                
    net.projections.append(proj)
    
    '''
    # Add outer input (IClamp)
    tmp = rnd.normal(I_mean, I_sigma**2, numCells_bc)  # random numbers from Gaussian distribution
    for i in range(0, numCells_bc):
        pg = neuroml.PulseGenerator(id='IClamp%i'%i, delay='0ms', duration='%sms'%duration, amplitude='%fpA'%(tmp[i]))
        
        nml_doc.pulse_generators.append(pg)
    
        input_list = neuroml.InputList(id='input%i'%i, component='IClamp_%i'%i, populations=pop.id)
        input = neuroml.Input(id=i, target='../%s[%i]'%(pop.id, i), destination='wbs1')
        input_list.input.append(input)
        
        net.input_lists.append(input_list)
    '''
    
    # Write to file
    nml_file = '%sNet.nml'%ref
    print 'Writing network file to:', nml_file, '...'
    neuroml.writers.NeuroMLWriter.write(nml_doc, nml_file)
    
    
    if validate:
        
        # Validate the NeuroML
        from neuroml.utils import validate_neuroml2
        validate_neuroml2(nml_file) 
    
    
    if generate_LEMS_simulation:
        
        # Vreate a LEMSSimulation to manage creation of LEMS file
        ls = LEMSSimulation(sim_id='%sNetSim'%ref, duration=duration, dt=dt)
        
        # Point to network as target of simulation
        ls.assign_simulation_target(net.id)
        
        # Incude generated/existing NeuroML2 files
        ls.include_neuroml2_file('WangBuzsakiCell.xml', include_included=False)
        ls.include_neuroml2_file('WangBuzsakiSynapse.xml', include_included=False)
        ls.include_neuroml2_file(nml_file, include_included=False)
        
        # Specify Display and output files
        disp_bc = 'display_bc'
        ls.create_display(disp_bc, 'Basket Cell Voltage trace', '-80', '40')
        
        of_bc = 'volts_file_bc'
        ls.create_output_file(of_bc, 'wangbuzsaki_network.dat')
        
        '''
        of_spikes_bc = 'of_spikes_bc'
        ls.create_event_output_file(of_spikes_bc, 'wangbuzsaki_network_spikes.dat')
        '''
        
        max_traces = 25
        for i in range(numCells_bc):
            quantity = '%s/%i/%s/v'%(pop.id, i, cell_id)
            if i < max_traces:
                ls.add_line_to_display(disp_bc, 'BC %i: Vm'%i, quantity, '1mV', pynml.get_next_hex_color())
            ls.add_column_to_output_file(of_bc, 'v_%i'%i, quantity)
            
        # Save to LEMS file
        print 'Writing LEMS file...'
        lems_file_name = ls.save_to_file()
        
    else:
        
        ls = None
        lems_file_name = ''
                
    return ls, lems_file_name


if __name__ == '__main__':
    
    generate_LEMS_simulation = True
    
    ls, lems_file_name = generate_WB_network('wb1', 'wbs1', 0.6, 1, 0.1, generate_LEMS_simulation)
    
    # if generate_LEMS_simulation:
        # run with jNeuroML
        # sim = pynml.run_lems_with_jneuroml(lems_file_name, nogui='True', load_saved_data='False', plot='True')
    
        # run with jNeuroML_NEURON
        # sim = pynml.run_lems_with_jneuroml_neuron(lems_file_name, nogui='True', load_saved_data='False', plot='True')    