# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

g = 9.81
L = [.14, .19, .24, .29, .34]
pos = [0]
vel = [0]
acc = [0,1,2,3,4,4,2,2,1,0,0,0,0,-1,-1,-2,-2,-2,-3,-4,-4]
time = np.linspace(0,20,21)
theta = np.radians(110)

def update_system(acc,pos,vel,time1,time2):
    # position and velocity update below
    dt = time2-time1
    posNext = pos+vel*dt
    velNext = vel+(g/L[4])*np.sin(theta)*dt
    return posNext,velNext

def print_system(time,pos,vel):
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel, "\n")


i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    posNext, velNext = update_system(acc[i],pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    #print_system(time[i],pos[i],vel[i])
    i += 1


plt.subplot(3,1,1)
plt.plot(time, pos, 'ro--') 

plt.xlabel('Time (seconds)')
plt.ylabel('Position (m)')
plt.title('Position vs Time .34 meters at 110 deg')
plt.xlim((0, 20)) # set x range to -1 to 8
plt.grid()


plt.subplot(3,1,2)
plt.plot(time, vel, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 20)) # set x range to -1 to 8
plt.grid()


plt.subplot(3,1,3)
plt.plot(time, acc, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 20)) # set x range to -1 to 8
plt.grid()
plt.tight_layout()
plt.show()

def find_period(new_array):
    time = new_array[:,0]
    y = new_array[:,1]
    y_filt = sig.medfilt(y)
    y_filt_pks, _ = sig.find_peaks(y_filt)
    plt.plot(time, y, 'r-', time[y_filt_pks], y_filt[y_filt_pks], 'b.')
    plt.title('Period of pendulum')
    plt.show()
    print(y_filt[y_filt_pks][7]-y_filt[y_filt_pks][8])
    
    
p = [.24, .28, .31, .34, .37]

plt.plot(L, p, 'r--')
plt.xlabel('Length in m')
plt.ylabel('Period in s')
plt.title('Length vs Period')
plt.show()

















