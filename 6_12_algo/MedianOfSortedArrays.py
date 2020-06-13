#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 20:17:27 2020

@author: wangpeiyu
"""

"""
65. Median of two Sorted Arrays

There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

Have you met this question in a real interview?  
Clarification
The definition of the median:

The median here is equivalent to the median in the mathematical definition.

The median is the middle of the sorted array.

If there are n numbers in the array and n is an odd number, the median is A[(n-1)/2].

If there are n numbers in the array and n is even, the median is (A[n / 2] + A[n / 2 + 1]) / 2.

For example, the median of the array A=[1,2,3] is 2, and the median of the array A=[1,19] is 10.

Example
Example 1

Input:
A = [1,2,3,4,5,6]
B = [2,3,4,5]
Output: 3.5
Example 2

Input:
A = [1,2,3]
B = [4,5]
Output: 3
Challenge
The overall run time complexity should be O(log (m+n)).
"""
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        len_A=len(A)
        len_B=len(B)
        p1, p2=0,0
        left, right=-1, -1
        
        for i in range((len_A+len_B)//2+1):
            left=right
            if p1>=len_A or p2<len_B and A[p1]>B[p2]:
                right=B[p2]
                p2+=1
            else:
                right=A[p1]
                p1+=1
                
        if (len_B+len_A)%2==1:
            return right
        else:
            return (left+right)/2
                    