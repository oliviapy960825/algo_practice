#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:53:37 2020

@author: wangpeiyu
"""

"""
#137 Medium

This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

    init(size): initialize the array with size
    set(i, val): updates index at i with val where val is either 1 or 0.
    get(i): gets the value at index i.

"""

class BitArray:
    def __init__(self, size):
        self.lst=[0]*size
        self.size=size
        
    def set(self,i,val):
        if i>self.size:
            return None
        self.lst[i]=val
        
    def get(self,i):
        if i>self.size:
            return None
        return self.lst[i]