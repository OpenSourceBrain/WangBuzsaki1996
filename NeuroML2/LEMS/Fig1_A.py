import sys
from pyneuroml.analysis import generate_current_vs_frequency_curve
    
nogui = '-nogui' in sys.argv  # Used to supress GUI in tests for Travis-CI
    
generate_current_vs_frequency_curve(nml2_file =           'WangBuzsaki.cell.nml', 
                                    cell_id =             'wb1', 
                                    start_amp_nA =         -0.002, 
                                    end_amp_nA =           0.022, 
                                    step_nA =              0.001, 
                                    analysis_duration =    500, 
                                    analysis_delay =       50,
                                    temperature =          "35degC",
                                    spike_threshold_mV =   0.0,
                                    plot_voltage_traces =  False, # not nogui,
                                    plot_if =              True,  # not nogui,
                                    plot_iv =              False,  # not nogui,
                                    include_included =     False,
                                    verbose = True)
