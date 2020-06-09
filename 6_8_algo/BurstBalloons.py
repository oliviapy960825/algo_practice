#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:02:18 2020

@author: wangpeiyu
"""

"""
168. Burst Balloons
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Have you met this question in a real interview?  
Example
Example 1:

Input：[4, 1, 5, 10]
Output：270
Explanation：
nums = [4, 1, 5, 10] burst 1, get coins 4 * 1 * 5 = 20
nums = [4, 5, 10]   burst 5, get coins 4 * 5 * 10 = 200 
nums = [4, 10]    burst 4, get coins 1 * 4 * 10 = 40
nums = [10]    burst 10, get coins 1 * 10 * 1 = 10
Total coins 20 + 200 + 40 + 10 = 270
Example 2:

Input：[3,1,5]
Output：35
Explanation：
nums = [3, 1, 5] burst 1, get coins 3 * 1 * 5 = 15
nums = [3, 5] burst 3, get coins 1 * 3 * 5 = 15
nums = [5] burst 5, get coins 1 * 5 * 1 = 5
Total coins 15 + 15 + 5  = 35

"""

class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        # write your code here
        if not nums:
            return 0
        
        lst=[1, *nums, 1]
        
        return self.memoSearch(lst, 0, len(lst)-1, {})
        
    def memoSearch(self, nums, i, j, memo):
        if i==j:
            return 0
        if (i,j) in memo:
            return memo[(i,j)]
        best=0
        
        for k in range(i+1,j):
            left=self.memoSearch(nums, i, k, memo)
            right=self.memoSearch(nums, k, j, memo)
            best=max(best, left+right+nums[i]*nums[k]*nums[j])
        
        memo[(i,j)]=best
        return best
        