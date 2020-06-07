#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:03:18 2020

@author: wangpeiyu
"""

"""
436. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

Have you met this question in a real interview?  
Example
Example 1:

Input:
[
  [1, 0, 1, 0, 0],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0]
]
Output: 4
Example 2:

Input:
[
  [0, 0, 0],
  [1, 1, 1]
]
Output: 1
"""
class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return 0
        row=len(matrix)
        col=len(matrix[0])
        dp=[[0]*col for _ in range(row)]
        
        edge=max(matrix[0])
        
        for i in range(col):
            dp[0][i]=matrix[0][i]
            
        for i in range(row):
            dp[i][0]=matrix[i][0]
            
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j]:
                    dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    
                else:
                    dp[i][j]=0
                    
            edge=max(edge, max(dp[i]))
        return edge**2
