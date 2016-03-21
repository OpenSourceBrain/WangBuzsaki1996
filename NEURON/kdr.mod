NEURON { SUFFIX kdr }
NEURON { USEION k WRITE ik }         
ASSIGNED { ik }
PARAMETER {
	erev 		= -90.  (mV)
	gmax 		= 0.009    (mho/cm2)
        vrest           = 0.

	exptemp		= 27
	maflag 		= 3
	malphaA 	= -0.01
	malphaB		= -10.0
	malphaV0	= -34.
	mbflag 		= 1
	mbetaA 		= 0.125
	mbetaB		= -80.
	mbetaV0		= -44.
	mq10		= 5
	mexp 		= 4

	haflag 		= 0
	halphaA 	= 0
	halphaB		= 0
	halphaV0	= 0
	hbflag 		= 0
	hbetaA 		= 0
	hbetaB		= 0
	hbetaV0		= 0
	hq10		= 5
	hexp 		= 0

	cao                (mM)
	cai                (mM)

	celsius			   (degC)
	dt 				   (ms)
	v 			       (mV)

	vmax 		= 100  (mV)
	vmin 		= -100 (mV)
} : end PARAMETER

INCLUDE "geneval_cvode.inc"

PROCEDURE iassign () { i = g*(v-erev) ik=i }

:* SYNAPSES
:** AMPA
