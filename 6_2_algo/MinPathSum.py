#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:52:42 2020

@author: wangpeiyu
"""

"""
Lintcode 110. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

You can only go right or down in the path..

Have you met this question in a real interview?  
Example
Example 1:
	Input:  [[1,3,1],[1,5,1],[4,2,1]]
	Output: 7
	
	Explanation:
	Path is: 1 -> 3 -> 1 -> 1 -> 1


Example 2:
	Input:  [[1,3,2]]
	Output: 6
	
	Explanation:  
	Path is: 1 -> 3 -> 2
"""

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid or len(grid)==0 or len(grid[0])==0:
            return 0
        if len(grid)==1:
            return sum(grid[0])
            
        dp=grid.copy()
        row=len(dp)
        col=len(dp[0])
        for i in range(1,col):
            dp[0][i]=dp[0][i-1]+dp[0][i]
        for i in range(1,row):
            dp[i][0]=dp[i-1][0]+dp[i][0]
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j]=min(dp[i][j]+dp[i-1][j], dp[i][j]+dp[i][j-1])
                
        return dp[-1][-1]