# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

#Set General Parameters
ncycles=20
pop=1000

#Transition probabilities
probAtoB=0.202
probAtoC=0.067
probAtoD=0.010
probAtoA=1-(probAtoB+probAtoC+probAtoD)

probBtoC=0.407
probBtoD=0.012
probBtoB=1-(probBtoC+probBtoD)

probCtoD=0.250
probCtoC=1-probCtoD

#Costs
costHIVA=7119
costHIVB=7415
costAIDS=13370

#QoL
qolHIVA=0.9
qolHIVB=0.8
qolAIDS=0.3

#Make Transition Matrix
transmat=np.array([[probAtoA,probAtoB,probAtoC,probAtoD],
                      [0,probBtoB,probBtoC,probBtoD],
                      [0,0,probCtoC,probCtoD],
                      [0,0,0,1]])

#Set Initial Distribution
startdist=np.array([pop,0,0,0])

#Set up Markov Trace
markovtrace=np.zeros((ncycles+1,4))
markovtrace[0,]=startdist

#Fill Markov Trace
for i in range(ncycles):
    markovtrace[i+1,]=markovtrace[i,].dot(transmat)
    
#Costs to append
costvector=np.array(markovtrace[:,1]*costHIVA)+(markovtrace[:,2]*costHIVB)+(markovtrace[:,3]*costAIDS)
markovtrace=np.column_stack([markovtrace,costvector])

#QoL to append
qolvector=np.array(markovtrace[:,1]*qolHIVA)+(markovtrace[:,2]*qolHIVB)+(markovtrace[:,3]*qolAIDS)
markovtrace=np.column_stack([markovtrace,qolvector])
