#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:45:36 2020

@author: wangpeiyu
"""

"""
Lintcode 75. Find Peak Element

There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.
Have you met this question in a real interview?  
Example
Example 1:
	Input:  [1, 2, 1, 3, 4, 5, 7, 6]
	Output:  1 or 6
	
	Explanation:
	return the index of peek.


Example 2:
	Input: [1,2,3,4,1]
	Output:  3
"""

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if not A or len(A)==0:
            return -1
        l=0
        r=len(A)-2
        while l+1<r:
            mid=l+(r-l)//2
            if A[mid-1]<mid and mid>A[mid+1]:
                return mid
            elif A[mid]<A[mid-1]:
                r=mid
            else:
                l=mid
                
        if A[l]>A[r] and A[l]>A[l-1]:
            return l
        return r