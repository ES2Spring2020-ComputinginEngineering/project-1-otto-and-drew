# -*- coding: utf-8 -*-
import numpy as np
from numpy import cos, sin
from matplotlib import pyplot as plt
from scipy.integrate import odeint

g = 9.81
l = 0.50
time = np.arange(0, 10, 0.010)
initial_position = 60.0
initial_theta = np.radians(initial_position)
initial_velocity = np.radians(0)

def equations(initial_vector, time):
    
    theta, velocity = initial_vector
    functions = [velocity, -(g/l) * sin(theta)]
    
    return functions

def plot_position(time, position):
   
    plt.plot(time, position[:,0])
    plt.title("Pendulum Position vs. Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Position")
    plt.grid(True)
    plt.show() 

position = odeint(equations, [initial_theta, initial_velocity], time)

plot_position(time, position)