#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:39:02 2020

@author: wangpeiyu
"""

"""
392. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Have you met this question in a real interview?  
Example
Example 1:

Input: [3, 8, 4]
Output: 8
Explanation: Just rob the second house.
Example 2:

Input: [5, 2, 1, 3]
Output: 8
Explanation: Rob the first and the last house.
Challenge
O(n) time and O(1) memory.
"""

class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        if not A or len(A)==0:
            return 0
        if len(A)==1:
            return A[0]
            
        if len(A)==2:
            return max(A[0], A[1])
            
        dp=[0]*len(A)
        dp[0]=A[0]
        dp[1]=A[1]
        for i in range(2, len(A)):
            dp[i]=max((dp[i-2]+A[i]),dp[i-1])
            
        return dp[-1]
