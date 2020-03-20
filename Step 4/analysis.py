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

def create_array(name):
    
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

s = create_array("receiver_data1.txt")
p = create_array("receiver_data2.txt")
q = create_array("receiver_data3.txt")
r = create_array("receiver_data4.txt")
t = create_array("receiver_data5.txt")

def acc_array(array):
    t = array[:,0]
    x = array[:,1]
    y = array[:,2]
    z = array[:,3]
    plt.plot(t, x, 'r--', t, y, 'bs', t, z, 'g^')
    plt.xlabel('Time')
    plt.ylabel('Accelerations')
    plt.title('Acceleration vs Time')
    plt.legend(('X values', 'Y values', 'Z values'))
    plt.show()


def theta_array(array):
     
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

l = theta_array(s)
m = theta_array(p)
n = theta_array(q)
o = theta_array(r)
p = theta_array(t)

def theta_graph(new_array):
    ti = new_array[:,0]
    th = new_array[:,1]
    plt.plot(ti, th, 'b.')
    plt.xlabel('Time')
    plt.ylabel('Theta')
    plt.title('Theta vs. Time')
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



















