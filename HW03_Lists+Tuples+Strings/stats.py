# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import math

def list_min(l:list):
    return min(l)

def list_max(l:list):
    return max(l)

def list_range(l:list):
    return list_max(l) - list_min(l)

def list_mean(l:list):
    return sum(l) / len(l)

def list_median(l:list):
    l = sorted(l)
    middle = math.ceil(len(l) / 2) - 1
    return l[middle]