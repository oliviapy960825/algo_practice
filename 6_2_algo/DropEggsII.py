#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:53:24 2020

@author: wangpeiyu
"""

"""
Lintcode 584. Drop Eggs II

There is a building of n floors. If an egg drops from the k th floor or above, it will break. If it's dropped from any floor below, it will not break.

You're given m eggs, Find k while minimize the number of drops for the worst case. Return the number of drops in the worst case.

Have you met this question in a real interview?  
Example
Example 1:

Input: m = 2, n = 100 
Output: 14
Example 2:

Input: m = 2, n = 36 
Output: 8
"""

class Solution:
    """
    @param m: the number of eggs
    @param n: the number of floors
    @return: the number of drops in the worst case
    """
    def dropEggs2(self, m, n):
        # write your code here
        dp=[[float('INF')]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            dp[i][1]=1
            dp[i][0]=0
            
        for i in range(1, n+1):
            dp[1][i]=i
            
        for i in range(2, m+1):
            for j in range(2, n+1):
                for k in range(1, j+1):
                    dp[i][j]=min(dp[i][j], 1+ max(dp[i-1][k-1], dp[i][j-k]))
                    
        return dp[m][n]
        
