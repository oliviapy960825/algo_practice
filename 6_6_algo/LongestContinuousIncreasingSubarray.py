#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:04:17 2020

@author: wangpeiyu
"""

"""
397. Longest Continuous Increasing Subsequence

Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

Can be from right to left or from left to right.
Indices of the integers in the subsequence should be continuous.
Have you met this question in a real interview?  
Example
Example 1:

Input: [5, 4, 2, 1, 3]
Output: 4
Explanation:
For [5, 4, 2, 1, 3], the LICS  is [5, 4, 2, 1], return 4.
Example 2:

Input: [5, 1, 2, 3, 4]
Output: 4
Explanation:
For [5, 1, 2, 3, 4], the LICS  is [1, 2, 3, 4], return 4.
Challenge
O(n) time and O(1) extra space.
"""

class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if not A or len(A)==0:
            return 0
            
        if len(A)==1:
            return 1
            
        incr=1
        decr=1
        count=1
        
        for i in range(1, len(A)):
            if A[i]>A[i-1]:
                incr+=1
                decr=1
            elif A[i]<A[i-1]:
                incr=1
                decr+=1
                
            else:
                incr=1
                decr=1
                
            count=max(count,incr,decr)
            
        return count
        