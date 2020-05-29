#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:50:42 2020

@author: wangpeiyu
"""

"""
141. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

Have you met this question in a real interview?  
Example
Example 1:
	Input:  0
	Output: 0


Example 2:
	Input:  3
	Output: 1
	
	Explanation:
	return the largest integer y that y*y <= x. 
	
Example 3:
	Input:  4
	Output: 2
	

Challenge
O(log(x))

"""
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x<2:
            return x
        left=0
        right=x//2
        
        while left+1<right:
            mid=left+(right-left)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                right=mid
            else:
                left=mid
                
        if right*right<=x:
            return right
        else:
            return left