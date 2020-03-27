# -*- coding: utf-8 -*-
import os
import math
import numpy as np
import matplotlib.pyplot as plt

def update_system(pos,vel, acc):
    
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

    array = np.array(values)

    
    