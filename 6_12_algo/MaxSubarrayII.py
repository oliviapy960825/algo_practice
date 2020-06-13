#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 17:32:52 2020

@author: wangpeiyu
"""

"""
42. Maximum Subarray II

Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.

The subarray should contain at least one number

Have you met this question in a real interview?  
Example
Example 1:

Input:
[1, 3, -1, 2, -1, 2]
Output:
7
Explanation:
the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2].
Example 2:

Input:
[5,4]
Output:
9
Explanation:
the two subarrays are [5] and [4].
Challenge
Can you do it in time complexity O(n) ?
"""
class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        n = len(nums)
        
        # 计算以i位置为结尾的前后缀最大连续和
        left_max = nums[:]
        right_max = nums[:]
        
        for i in range(1, n):
            left_max[i] = max(nums[i], left_max[i - 1] + nums[i])

        for i in range(n - 2, -1, -1):
            right_max[i] = max(nums[i], right_max[i + 1] + nums[i])
        
        # 计算前后缀部分最大连续和
        prefix_max = left_max[:]
        postfix_max = right_max[:]
    
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i], prefix_max[i - 1])
            
        for i in range(n - 2, -1, -1):
            postfix_max[i] = max(postfix_max[i], postfix_max[i + 1])
        
        result = -sys.maxsize
        for i in range(n - 1):
            result = max(result, prefix_max[i] + postfix_max[i + 1])
        
        return result