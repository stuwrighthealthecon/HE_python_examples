# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:20:12 2024

@author: mdxassw4
"""

import numpy as np
import time
import math
import matplotlib.pyplot

n=100000
startage=30
discount_health=0.035
rng = np.random.default_rng()

utility_ages=np.array([[30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
                      [0.9383,0.9145,0.9069,0.8824,0.8639,0.8344,0.8222,0.8072,0.8041,0.779,0.7533,0.6985,0.6497,0.6497,0.6497]])

t0=time.time()
results=np.zeros((n,3))
results[:,0]=np.arange(1,n+1,1)
results[:,1]=np.random.weibull(7.937,n)*86.788-([startage]*(n))

for i in range(n):
    
    #Set up a QALY vector of length equal to life years
    QALY_length = math.ceil(results[i,1])-(startage-1)

    #If less than 1 life year lived, set length to 1
    if QALY_length<1:QALY_length=1

    #Fill QALY vector with 0's
    QALY_vect = np.zeros(QALY_length)

    #Fill QALY vector with discounted age related utility values
    for y in range(QALY_length):
       QALY_vect[y] = (utility_ages[1,round(y/5)])*((1/(1+discount_health))**(y+1))
       QALY_vect[QALY_length-1]=QALY_vect[QALY_length-1]*(1-(math.ceil(results[i,1])-results[i,1]))

       results[i,2]=sum(QALY_vect)

    print(i)
    
t1=time.time()
timeelapsed=t1-t0
print(timeelapsed)

matplotlib.pyplot.hist(results[:,2],bins=20)
print(results[:,2])
