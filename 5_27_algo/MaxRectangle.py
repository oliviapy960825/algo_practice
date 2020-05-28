#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:53:05 2020

@author: wangpeiyu
"""

"""
Lintcode 510. Maximal Rectangle

Given a 2D boolean matrix filled with False and True, find the largest rectangle containing all True and return its area.

Have you met this question in a real interview?  
Example
Example 1

Input:
[
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]
Output: 6
Example 2

Input:
[
    [0,0],
    [0,0]
]
Output: 0
"""

class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        if not matrix:
            return 0
            
        max_rec=0
        heights=[0]*len(matrix[0])
        for row in matrix:
            for index, num in enumerate(row):
                heights[index]=heights[index]+1 if num else 0
            max_rec=max(max_rec,self.find_max_rec(heights))
            
        return max_rec
        
    def find_max_rec(self,heights):
        indices_stack=[]
        max_rec=0
        for index, height in enumerate(heights+[-1]):
            while indices_stack and heights[indices_stack[-1]]>=height:
                popped=indices_stack.pop()
                left_bound=indices_stack[-1] if indices_stack else -1
                max_rec=max(max_rec,(index-left_bound-1)*heights[popped])
                print("max_rec is: "+str(max_rec))
            indices_stack.append(index)
            print(indices_stack)
            
        return max_rec
        