# Step 4: Analysis of Results

import os
#import math
import numpy as np
import matplotlib.pyplot as plt

path = "/Users/ottolaakso/Desktop/Tufts Classes/ES2/GitHub/project-1-otto-and-drew/Step 3"
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

    array = np.loadtxt(outname, delimiter=",", dtype=int)
    print(array)
    t = array[[0][0]]
    print(t)
    
create_array("receiver_data1.txt")
  




























  
# =============================================================================
# def new_array(array):
#     
#     new_list = []
#    
#     for row in array:
#         time_value = array[np.array(0)]
#         acc_values = array[np.array(1,4)]
#         acc_x = acc_values[0]
#         acc_y = acc_values[1]
#         acc_z = acc_values[2]
#         tilt_x = (math.atan2(acc_x, math.sqrt((acc_y ** 2) + (acc_z **2))))
#         tilt_y = (math.atan2(acc_y, math.sqrt((acc_x ** 2) + (acc_z **2))))
#         theta = (math.atan2(tilt_y, tilt_x)*180)/(math.pi)
#         new_list = new_list + time_value + theta
#     
#     new_array = np.array(new_list)
#     return new_array
# =============================================================================


