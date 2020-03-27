# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

g = 9.81
L = 13.5
pos = [0]
vel = [0]
acc = [0,1,2,3,4,4,2,2,1,0,0,0,0,-1,-1,-2,-2,-2,-3,-4,-4]
time = np.linspace(0,20,21)


def update_system(acc,pos,vel,time1,time2):
    # position and velocity update below
    dt = time2-time1
    posNext = pos+vel*dt
    velNext = vel+(g/L)*np.sin(theta)*dt
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
plt.title('Position vs Time')
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
























# =============================================================================
# g = 9.81
# l = 0.50
# time = np.arange(0, 10, 0.010)
# initial_position = 60.0
# initial_theta = np.radians(initial_position)
# initial_velocity = np.radians(0)
# 
# def equations(initial_vector, time):
#     
#     theta, velocity = initial_vector
#     functions = [velocity, -(g/l) * sin(theta)]
#     
#     return functions
# 
# def plot_position(time, position):
#    
#     plt.plot(time, position[:,0])
#     plt.title("Pendulum Position vs. Time")
#     plt.xlabel("Time (s)")
#     plt.ylabel("Position")
#     plt.grid(True)
#     plt.show() 
# 
# position = odeint(equations, [initial_theta, initial_velocity], time)
# 
# plot_position(time, position)
# =============================================================================
