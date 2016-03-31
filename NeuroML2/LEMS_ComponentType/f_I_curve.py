import sys
from pyneuroml.analysis import generate_current_vs_frequency_curve
    
nogui = '-nogui' in sys.argv  # Used to supress GUI in tests for Travis-CI
    
generate_current_vs_frequency_curve(nml2_file =           'WangBuzsakiCell.xml', 
                                    cell_id =             'wb1', 
                                    start_amp_nA =         -0.005, 
                                    end_amp_nA =           0.05, 
                                    step_nA =              0.002, 
                                    analysis_duration =    500, 
                                    analysis_delay =       50,
                                    temperature =          "35degC",
                                    spike_threshold_mV =   0.0,
                                    plot_voltage_traces =  not nogui,
                                    plot_if =              True,  # not nogui,
                                    plot_iv =              True, #,  # not nogui,
                                    include_included =     False)
                                    # simulator="jNeuroML")  
