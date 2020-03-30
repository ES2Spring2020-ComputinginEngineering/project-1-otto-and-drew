""" Step 2 Theoretical Model Code """

import math
import numpy as np
import matplotlib.pyplot as plt

def period(L):
# This function takes the parameter L (length of pendulum) and
# converts it into the theoretical period of the pendulum
# Void function
    
    t = 2*math.pi*(L/9.8)**.5
    return t

def theoretical_graph(length):
# This function takes the parameter "lengths" (list of pendulum lengths)
# and runs the function "period" for all elements in the list, then
# graphs the pendulum lenght vs. the period
# Void function
    
    p = period(length)
    plt.plot(length, p, "bo-")
    plt.ylabel("Period (s)")
    plt.xlabel("Length (m)")
    plt.grid(True)
    plt.title("Theoretical Correlation of Pendulum Length vs. Period")
    plt.axis(0, .5, 0, 1.5)
    plt.show()
    
pendulum_lengths = [.140, .191, .241, .292, .343]
length_array = np.array(pendulum_lengths)

theoretical_graph(length_array)

"""The limits of this model:
The theoretical evaluation of the pendulum period given its length assumes
that friction and air resistance are negligible and do not affect the motion of the 
pendulum. Additionally, the theoretical model assumes that the pendulum swings in a 
perfect trajectory, whereas in reality, its motion is directed in multiple directions."""