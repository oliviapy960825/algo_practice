#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 00:00:22 2020

@author: wangpeiyu
"""

"""
#134

This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

    init(arr, size): initialize with the original large array and size.
    set(i, val): updates index at i with val.
    get(i): gets the value at index i.

"""
class SparseArray(object):
    def __init__(self,arr,size):
        self.dic={}
        for i in range(size):
            self.dic[i]=arr[i]
            
    def set(self,i,val):
        self.dic[i]=val
        
    def get(self,i):
        return self.dic.get(i,0)