#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:50:39 2020

@author: wangpeiyu
"""

"""
#144 Medium

This problem was asked by Google.

Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""
def NearestLargerNumber(lst, index):
    curr=max(lst)-lst[index]
    num=lst.index(max(lst))
    for i in range(len(lst)):
        if lst[i]-lst[index]>0 and lst[i]-lst[index]<curr and abs(i-index)<abs(num-index):
            num=i
    return num
            
        
print(NearestLargerNumber([4, 1, 3, 5, 6],0))