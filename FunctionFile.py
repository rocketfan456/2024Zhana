# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:28:47 2024

@author: Zhana
"""

import numpy as np

# vis-viva equation
# v = sqrt(mu*((2/r)-(1/a)))

def raise_orbit(alt0):
    mu = 398600 # km^2/s^2
    r_earth = 6378 # km
    r = 185+r_earth
    a0 = ((185+r_earth)+(alt0+r_earth))/2
    a = ((185+r_earth)+(410000+r_earth))/2
    v0 = np.sqrt(mu*((2/r)-(1/a0)))
    v = np.sqrt(mu*((2/r)-(1/a)))
    dv = v - v0
    dv = dv*1000 # convert to m/s
    return dv