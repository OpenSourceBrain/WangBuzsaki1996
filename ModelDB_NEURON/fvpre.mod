: $Id: fvpre.mod,v 1.10 2003/07/29 23:37:22 billl Exp $
COMMENT
synapse taken from Wang, X.-J. and Buzsaki G. (1996) Gamma oscillations by
synaptic inhibition in a hippocampal interneuronal network.  
J. Neurosci. 16, 6402-6413.
ENDCOMMENT
					       
NEURON {
  POINT_PROCESS fvpre
  RANGE gmax, g, i
  GLOBAL alpha,beta,thetasyn,e
  NONSPECIFIC_CURRENT i
  POINTER vpre
}

UNITS {
  (nA) = (nanoamp)
  (mV) = (millivolt)
  (uS) = (microsiemens)
}

PARAMETER {
  gmax=1e-4 (uS)
  alpha=12 (/ms)
  beta=0.1 (/ms)
  e=-75	   (mV)
  thetasyn=0 (mV) 
}

ASSIGNED { vpre (mV) v (mV) i (nA)  g (uS)}

STATE { s }

INITIAL {
  s =  alpha*F(vpre)/(alpha*F(vpre)+beta)
}

BREAKPOINT {
  SOLVE state METHOD cnexp
  g = gmax * s
  i = g*(v - e)
}

DERIVATIVE state {
  s' = alpha*F(vpre)*(1-s) - beta*s
}

FUNCTION F (v1 (mV)) {
  F = 1/(1 + exp(-(v1-thetasyn)/2))
}  
