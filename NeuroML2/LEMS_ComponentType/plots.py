# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def raster_plot(spikeTimes, spikingNeurons, tstop, nnumber, show=False):

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
