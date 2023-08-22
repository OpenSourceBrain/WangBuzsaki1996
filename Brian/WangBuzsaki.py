from brian2 import *

def main(dt):
    '''
    Modified (in order to set different dt) version of http://www.briansimulator.org/docs/examples-frompapers_Wang_Buszaki_1996.html
    :param dt: time step of numerical solver [ms]
    :return M: StateMonitor with membrane potential values
    '''

    Cm = 1 * uF  # /cm**2
    Iapp = 2 * uA
    gL = 0.1 * msiemens
    EL = -65 * mV
    ENa = 55 * mV
    EK = -90 * mV
    gNa =  35 * msiemens
    gK =  9 * msiemens

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
    M = StateMonitor(neuron, 'v', record=True)

    defaultclock.dt=dt*ms

    run(100*ms)

    return M


if __name__ == '__main__':
    
    dt = 0.01
    M = main(dt)


