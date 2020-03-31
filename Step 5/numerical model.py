# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.signal as sig

g = 9.81
#gravity constant

L = [.14, .19, .24, .29, .34]
#The lengths for our pendulum


def update_system(pos,vel,time1,time2, length):
# Takes position, velocity, time1, time2, and length as parameters
# Calculates and returns next acceleration, velocity, and position values 
    dt = time2-time1
    accNext = (g/length)*np.sin(pos)
    velNext = vel+(accNext*dt)
    posNext = pos+(velNext*dt)
    return posNext,velNext, accNext



def pen_sim(length, start_angle):
# Takes the length and starting angle of the pendulum as parameters
# Calculates and graphs position, velocity, acceleration, and period
# Void function
    if start_angle < 90:
        pos = [math.pi/3]
    elif start_angle > 90:
        pos = [2*math.pi/3]
    vel = [0]
    acc = [0]
    time = np.arange(0,20,.1)
    i = 1
    while i < len(time):
    # update position and velocity using previous values and time step
        posNext, velNext, accNext = update_system(pos[i-1],vel[i-1],time[i-1],time[i], length)
        pos.append(posNext)
        vel.append(velNext)
        acc.append(accNext)
        i += 1


    plt.subplot(3,1,1)
    plt.plot(time, pos, 'r--') 
    plt.xlabel('Time (seconds)')
    plt.ylabel('Position (m)')
    plt.title('Position vs Time at ' + str(length) + ' meters and ' + str(start_angle) + ' deg')
    plt.xlim((0, 20)) # set x range to -1 to 8
    plt.grid()


    plt.subplot(3,1,2)
    plt.plot(time, vel, 'r--') 
    plt.xlabel('Time (seconds)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity vs Time')
    plt.xlim((0, 20)) # set x range to -1 to 8
    plt.grid()


    plt.subplot(3,1,3)
    plt.plot(time, acc, 'r--') 
    plt.xlabel('Time (seconds)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.title('Acceleration vs Time')
    plt.xlim((0, 20)) # set x range to -1 to 8
    plt.grid()
    plt.tight_layout()
    plt.show()
    
    p_filt_pks, _ = sig.find_peaks(pos)
    pt = time[p_filt_pks]
    period = pt[5] - pt[4]
    print('Period of pendulum ' + str(length) + ' meters and the period is ' + str(period) + 'sec')
   
def main():
#Will take previous functions and create readable graphs for them
#Takes no parameters
#Void function
    
    
    pen_sim(.14, 60)    
    pen_sim(.19, 60) 
    pen_sim(.24, 60)
    pen_sim(.29, 60) 
    pen_sim(.34, 60) 
    pen_sim(.14, 120) 
    pen_sim(.19, 120) 
    pen_sim(.24, 120) 
    pen_sim(.29, 120) 
    pen_sim(.34, 120) 

    p = [1.0, 1.2, 1.299, 1.5, 1.6]
    #these values were obtained by running the function pen_sim with 60 degrees

    plt.plot(L, p, 'bo-')
    plt.xlabel('Length (m)')
    plt.ylabel('Period (s)')
    plt.grid(True)
    plt.title('Numerical Correlation of Pendulum Length vs. Period at 60 deg')
    plt.show()

    p1 = [.799, 1, 1, 1.2, 1.2]
    #These values were obtained by running the function pen_sim with 120 degrees

    plt.plot(L, p1, 'bo-')
    plt.xlabel('Length (m)')
    plt.ylabel('Period (s)')
    plt.grid(True)
    plt.title('Numerical Correlation of Pendulum Length vs. Period at 120 deg')
    plt.show()













