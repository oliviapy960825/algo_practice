#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:07:39 2020

@author: wangpeiyu
"""

"""
398. Longest Continuous Increasing Subsequence II
Given an integer matrix. Find the longest increasing continuous subsequence in this matrix and return the length of it.

The longest increasing continuous subsequence here can start at any position and go up/down/left/right.

Have you met this question in a real interview?  
Example
Example 1:

Input: 
    [
      [1, 2, 3, 4, 5],
      [16,17,24,23,6],
      [15,18,25,22,7],
      [14,19,20,21,8],
      [13,12,11,10,9]
    ]
Output: 25
Explanation: 1 -> 2 -> 3 -> 4 -> 5 -> ... -> 25 (Spiral from outside to inside.)
Example 2:

Input: 
    [
      [1, 2],
      [5, 3]
    ]
Output: 4
Explanation: 1 -> 2 -> 3 -> 5
Challenge
Assume that it is a N x M matrix. Solve this problem in O(NM) time and memory.

"""
DIRECTIONS=[(0,1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longestContinuousIncreasingSubsequence2(self, matrix):
        # write your code here
        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return 0
        n=len(matrix)
        m=len(matrix[0])
        memo={}
        longest=1
        for i in range(n):
            for j in range(m):
                longest=max(longest, self.dfs(matrix, i, j, memo))
                
        return longest
        
    def dfs(self, matrix, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        longest=1
        
        for dx, dy in DIRECTIONS:
            x_=x+dx
            y_=y+dy
            if not self.inside(matrix, x_, y_) or matrix[x_][y_]<=matrix[x][y]:
                continue
            else:
                longest=max(longest, self.dfs(matrix, x_, y_, memo)+1)
                
        memo[(x,y)]=longest
        return longest
        
    def inside(self, matrix, x, y):
        return x>=0 and x<len(matrix) and y>=0 and y<len(matrix[0])
    
#dp
        
DIRECTIONS=[(0,1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longestContinuousIncreasingSubsequence2(self, matrix):
        # write your code here
        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return 0
        n=len(matrix)
        m=len(matrix[0])
        memo={}
        self.dp=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                self.dfs(matrix, i, j)
        return max(max(row) for row in self.dp)
        
    def dfs(self, matrix, x, y):
        if self.dp[x][y] !=0:
            return self.dp[x][y]
        longest=1
        
        for dx, dy in DIRECTIONS:
            x_=x+dx
            y_=y+dy
            if not self.inside(matrix, x_, y_) or matrix[x_][y_]<=matrix[x][y]:
                continue
            else:
                longest=max(longest, self.dfs(matrix, x_, y_)+1)
                
        self.dp[x][y]=longest
        return self.dp[x][y]
        
    def inside(self, matrix, x, y):
        return x>=0 and x<len(matrix) and y>=0 and y<len(matrix[0])
            
            