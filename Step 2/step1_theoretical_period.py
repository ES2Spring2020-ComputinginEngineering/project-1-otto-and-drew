# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:10:26 2020

@author: drewh
"""

import numpy as np
import matplotlib.pyplot as plt

length = [.140, .191, .241, .292, .343]
arr1d = np.array(length)

def period(L):
# This function takes the parameter L (length of pendulum) and
# converts it into the theoretical period of the pendulum
    t = (L/9.8)**.5
    return t

def theoretical_graph():
# This function runs the function "period" and graphs the correlation
# between the pendulum length and the period
   
    p = period(arr1d)
    plt.plot(length, p, "bo-")
    plt.ylabel("Period (s)")
    plt.xlabel("Length (m)")
    plt.grid(True)
    plt.title(" Theoretical Correlation of Pendulum Length vs. Period")
    plt.axis(0, .5, 0, 1.5)
    plt.show()
    
theoretical_graph()

"""The limits of this model:
The theoretical evaluation of the pendulum period given its length assumes
that friction and air resistance are negligible and do not affect the motion of the 
pendulum. Additionally, the theoretical model assumes that the pendulum swings in a 
perfect trajectory, whereas in reality, its motion is directed in multiple directions."""

