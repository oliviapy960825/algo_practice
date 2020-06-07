#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:39:03 2020

@author: wangpeiyu
"""

"""
41. Maximum Subarray

Given an array of integers, find a contiguous subarray which has the largest sum.

The subarray should contain at least one number.

Have you met this question in a real interview?  
Example
Example1:

Input: [−2,2,−3,4,−1,2,1,−5,3]
Output: 6
Explanation: the contiguous subarray [4,−1,2,1] has the largest sum = 6.
Example2:

Input: [1,2,3,4]
Output: 10
Explanation: the contiguous subarray [1,2,3,4] has the largest sum = 10.
Challenge
Can you do it in time complexity O(n)?
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums or len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
           
        curr_sum=0
        max_sum=-float('INF')
        for i in range(len(nums)):
            curr_sum+=nums[i]
            max_sum=max(max_sum,curr_sum)
            curr_sum=max(curr_sum, 0)
            
            
        return max_sum