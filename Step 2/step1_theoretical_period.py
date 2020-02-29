# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:10:26 2020

@author: drewh
"""

import numpy as np
#import math as mt

length = [.140, .191, .241, .292, .343]
arr1d = np.array(length)

def period(a):
    t = (a/9.8)**.5
    return t

