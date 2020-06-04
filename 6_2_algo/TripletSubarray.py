#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 10:44:37 2020

@author: wangpeiyu
"""

"""
Lintcode 1529. Triplet Subarray With Absolute Diff Less Than or Equal to Limit

Given an increasing array of integers nums and an integer limit, return the number of the triplet subarray in which the absolute difference between any two elements is less than or equal to limit.

In case there is no subarray satisfying the given condition return 0.

1 ≤ len(nums) ≤ 1e4，1 ≤ limit ≤ 1e6，0 ≤ nums[i] ≤ 1e6
Since the answer may be too large, return it modulo 99997867.

Have you met this question in a real interview?  
Example
Example 1:

Input：[1, 2, 3, 4], 3
Output：4
Explanation：We can choose (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4). Therefore, the number of the triplet subarray is 4.
Example 2:

Input: [1, 10, 20, 30, 50], 19
Output：1
Explanation：The only triplet array is (1, 10, 20), so the answer is 1。
Challenge
Can you figure out a solution with time complexity of O(n)?

"""

class Solution:
    """
    @param nums: the given array
    @param limit: the limit on the absolute difference of the subarray
    @return: Find the number of triplet subarray with the absolute difference less than or equal to limit
    """
    def tripletSubarray(self, nums, limit):
        # write your code here
        left=0
        res=0
        for right in range(2, len(nums)):
            while nums[right]-nums[left]>limit:
                left+=1
            if right-left>=2:
                res+=(right-left)*(right-left-1)//2
        return res