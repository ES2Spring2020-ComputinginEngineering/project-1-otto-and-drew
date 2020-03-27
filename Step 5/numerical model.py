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

def plot_model(time, position):
   
    plt.plot(time, position[:,0])
    plt.title("Pendulum Model")
    plt.xlabel("Time (s)")
    plt.ylabel("Position")
    plt.grid(True)
    plt.show() 

position = odeint(equations, [initial_theta, initial_velocity], time)

plot_model(time, position)

"""def update_system(pos,vel, acc):
    
    dt = 0.1
    pos_next = 
    vel_next = 
    acc_next = 
    
    return pos_next, vel_next, acc_next

pos = [60]
vel = [0]
acc = [0]
time = np.arange(0, 20, 0.1)
values = []
i = 1
    while i < len(time):
    
        pos_next, vel_next, acc_next = update_system(pos[i], vel[i], acc[i])
        time_next = time(i)
    
        pos.append(pos_next)
        vel.append(vel_next)
        acc.append(acc_next)
        values.append(time_next, pos_next, vel_next, acc_next)

    array = np.array(values)"""

    
    