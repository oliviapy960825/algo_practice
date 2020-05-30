#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:12:58 2020

@author: wangpeiyu
"""

"""
586. Sqrt(x) II

Implement double sqrt(double x) and x >= 0.

Compute and return the square root of x.

You do not care about the accuracy of the result, we will help you to output results.

Have you met this question in a real interview?  
Example
Example 1:

Input: n = 2 
Output: 1.41421356
Example 2:

Input: n = 3
Output: 1.73205081
"""

class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        if x>=1:
            start, end= 1, x
        else:
            start, end= x, 1
            
        while end-start>1e-10:
            mid=start+(end-start)/2
            if mid*mid==x:
                return mid
            if mid*mid<x:
                start=mid
            else:
                end=mid
                
        return start