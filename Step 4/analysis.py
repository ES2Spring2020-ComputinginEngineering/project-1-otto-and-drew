# Step 4: Analysis of Results

import os
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

#path = "/Users/ottolaakso/Desktop/Tufts Classes/ES2/GitHub/project-1-otto-and-drew/Step 3"
path = "c:/Users/drewh/Documents/GitHub/project-1-otto-and-drew/Step 3"
os.chdir(path)

fin1 = open("receiver_data1.txt", "r")
fin2 = open("receiver_data2.txt", "r")
fin3 = open("receiver_data3.txt", "r")
fin4 = open("receiver_data4.txt", "r")
fin5 = open("receiver_data5.txt", "r")
#These variables represent the data files for each of the five pendulum lengths

L = [.14, .19, .24, .29, .34]
#These are the pendulum length in meters

def create_array(name):
# Takes the name of a data file as a parameter and turns the contents of 
# the file into an array
# Returns the array    
    fin = open(name, "r")
    outname = "new" + name
    fout = open(outname, "w")
    for line in fin:
        line = line.replace("(", "")
        line = line.replace(")", "")
        fout.write(line)
    fin.close()
    fout.close()

    array = np.loadtxt(outname, delimiter=",", dtype=float)
    return array


def acc_array(array, length):
# Takes an array of time and x, y, and z acceleration values and length as 2 parameters
# Graphs the x, y, and z acceleration values in relation to time
# Void function    
    t = array[:,0]
    x = array[:,1]
    y = array[:,2]
    z = array[:,3]
    plt.plot(t, x, 'r--', t, y, 'bs', t, z, 'g^')
    plt.xlabel('Time (s)')
    plt.ylabel('Accelerations (m/s^2)')
    plt.title('Acceleration vs Time ' + str(length) + ' meters')
    plt.legend(('X values', 'Y values', 'Z values'))
    plt.show()


def theta_array(array):
# Takes an array of time and x, y, and z acceleration values
# creates a new array containing the angle of the pendulum at each time value.
# Returns the new array with theta and time.     
    
    new_list = []
    time = array[0:,0]
    acc_x = array[:,1]
    acc_y = array[:,2]
    acc_z = array[:,3]
    
    for i in range(len(acc_x)):
        tilt_x = (math.atan2(acc_x[i], math.sqrt((acc_y[i] ** 2) + (acc_z[i] **2))))
        tilt_y = (math.atan2(acc_y[i], math.sqrt((acc_x[i] ** 2) + (acc_z[i] **2))))
        theta = (math.atan2(tilt_y, tilt_x)*180)/(math.pi)
        new_list.append([time[i], theta])
    
    new_array = np.array(new_list)
    return new_array

def theta_graph(new_array, length):
# Takes an array with angle and time values as a parameter and length as another parameter and graphs them
# Void function
    
    ti = new_array[:,0]
    th = new_array[:,1]
    plt.plot(ti, th, 'b.')
    plt.xlabel('Time (s)')
    plt.ylabel('Theta in degrees')
    plt.title('Theta vs. Time ' + str(length) + ' meters')
    plt.show()

def find_period(new_array, length):
 # Takes an array of time and pendulum angle values as a parameter as well as length
 # Calculates the period and graphs period vs. time
 # Void function
 
    time = new_array[:,0]
    y = new_array[:,1]
    y_filt = sig.medfilt(y)
    y_filt_pks, _ = sig.find_peaks(y_filt)
    plt.plot(time, y, 'r-', time[y_filt_pks], y_filt[y_filt_pks], 'b.')
    plt.title('Period of pendulum ' + str(length) + ' meters')
    plt.xlabel('Time (s)')
    plt.ylabel('Theta in degrees')
    plt.show()
    
s = create_array("receiver_data1.txt")
v = create_array("receiver_data2.txt")
q = create_array("receiver_data3.txt")
r = create_array("receiver_data4.txt")
t = create_array("receiver_data5.txt")
#These variables will simplify the plotting process

l = theta_array(s)
m = theta_array(v)
n = theta_array(q)
o = theta_array(r)
p = theta_array(t)
#these variables will make it easier to create the graph and find the period

def main():
#Main will create all the graphs and period comparison
#Takes no parameters
#Void function
    
    acc_array(s, .14)
    acc_array(v, .19)
    acc_array(q, .24)
    acc_array(r, .29)
    acc_array(t, .34)
    
    theta_graph(l, .14)
    theta_graph(m, .19)
    theta_graph(n, .24)
    theta_graph(o, .29)
    theta_graph(p, .34)
    
    find_period(l, .14)
    find_period(m, .19)
    find_period(n, .24)
    find_period(o, .29)
    find_period(p, .34)
    
    pr = [.64, .67, .71, .73, .75]

    plt.plot(L, pr, 'r--', L, pr, 'b.')
    plt.xlabel('Length in m')
    plt.ylabel('Period in s')
    plt.title('Length vs Period Real-World')
    plt.show()




















