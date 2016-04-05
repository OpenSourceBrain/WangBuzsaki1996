# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def raster_plot(data, tstop, nnumber, show=False):
    
    tmp = np.loadtxt(data, delimiter='\t')
    spikingNeurons = tmp[:, 0].tolist()
    spikeTimes = tmp[:, 1].tolist()

    fig = plt.figure(figsize=(10, 8))

    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(spikeTimes, spikingNeurons, c='blue', marker='.', lw=0)
    ax.set_title('Raster plot')
    ax.set_xlim([0, tstop])
    ax.set_xlabel('Time [ms]')
    ax.set_ylim([0, nnumber])
    ax.set_ylabel('Neuron number')
    
    if show:
        plt.show()
    fig.savefig('raster_plot.png')
    
def voltage_plots(data, neuron_nums, show=False):
    
    assert (len(neuron_nums) < 8), 'to many columns to plot (len(neuron_nums) shold be < 8)!'
    cols = ['k-', 'r-', 'b', 'g-', 'c-', 'm-', 'y-']
    
    tmp = np.loadtxt(data)
    t = (tmp[:, 0]*1000).tolist()  # ms
    
    fig = plt.figure(figsize=(10, 8))
    
    ax = fig.add_subplot(1, 1, 1)
    for i, col in zip(neuron_nums, cols):
        v = (tmp[:, i]*1000).tolist()  # mV
        ax.plot(t, v, col, linewidth=2, label='net.[%s].soma.v(0.5)'%i)
        
    ax.set_xlim([t[0], t[-1]])
    ax.set_ylim([-80, 40])
    ax.set_xlabel('time [ms]')
    ax.set_ylabel('V [mV]')
    ax.set_title('Voltage plot')
    ax.legend()
    
    if show:
        plt.show()
    fig.savefig('voltage_plot.png')
