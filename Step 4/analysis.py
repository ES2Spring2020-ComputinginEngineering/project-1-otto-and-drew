# Step 4: Analysis of Results

import os
import numpy as np
import matplotlib.pyplot as plt

fin1 = open("receiver_data1.txt", "r")
fin2 = open("receiver_data2.txt", "r")
fin3 = open("receiver_data3.txt", "r")
fin4 = open("receiver_data4.txt", "r")
fin5 = open("receiver_data5.txt", "r")

def create_array(fin):
    array = []
    for line in fin:
        row = line.split()
        array = np.append(array, row)
    return array

def new_array(array):
    new_array = []
    array.index()