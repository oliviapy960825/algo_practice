#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:18:32 2020

@author: wangpeiyu
"""

"""
#149 Hard

This problem was asked by Goldman Sachs.

Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
"""
L=[1, 2, 3, 4, 5]
def sum(i,j):
    num=0
    for x in range(i, j):
        num+=L[x]
        
    return num

print(sum(1,3))