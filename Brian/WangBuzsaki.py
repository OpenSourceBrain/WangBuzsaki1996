from brian import *
import matplotlib.pyplot as plt
import sys

defaultclock.dt=0.01*ms

Cm = 1 * uF  # /cm**2
Iapp = 2 * uA
gL = 0.1 * msiemens
EL = -65 * mV
ENa = 55 * mV
EK = -90 * mV
gNa = 35 * msiemens
gK = 9 * msiemens

eqs='''
dv/dt = (-gNa*m**3*h*(v-ENa) -gK*n**4*(v-EK) -gL*(v-EL) + Iapp) / Cm : volt
m = alpham/(alpham+betam) : 1
alpham = -0.1/mV*(v+35*mV)/(exp(-0.1/mV*(v+35*mV))-1)/ms : Hz
betam = 4*exp(-(v+60*mV)/(18*mV))/ms : Hz
dh/dt = 5*(alphah*(1-h)-betah*h) : 1
alphah = 0.07*exp(-(v+58*mV)/(20*mV))/ms : Hz
betah = 1./(exp(-0.1/mV*(v+28*mV))+1)/ms : Hz
dn/dt = 5*(alphan*(1-n)-betan*n) : 1
alphan = -0.01/mV*(v+34*mV)/(exp(-0.1/mV*(v+34*mV))-1)/ms : Hz
betan = 0.125*exp(-(v+44*mV)/(80*mV))/ms : Hz
'''

neuron = NeuronGroup(1, eqs)
neuron.v = -70 * mV
neuron.h = 1
M = StateMonitor(neuron, 'v', record=0)

run(100*ms)

if not '-nogui' in sys.argv:
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(M.times, M[0]/mV)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Membrane Potential (mV)")
    ax.set_title('Wang Buzsaki PV cell model with 2uA input')
    plt.show()

#### save trace to file ####
save = True
if save:
    filename = 'wangbuzsaki.dat'
    outfile = open(filename, 'w')
    t = M.times.tolist()
    v = M[0].tolist()
    print("Saving results to: %s" %filename)
    for i in range(len(t)):
        line = '%s\t%s\n'%(t[i], v[i])
        outfile.write(line)
    outfile.close()