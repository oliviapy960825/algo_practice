#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:42:39 2020

@author: wangpeiyu
"""

"""
Lintcode 390. Find Peak Element II

Given an integer matrix A which has the following features :

The numbers in adjacent positions are different.
The matrix has n rows and m columns.
For all i < n, A[i][0] < A[i][1] && A[i][m - 2] > A[i][m - 1].
For all j < m, A[0][j] < A[1][j] && A[n - 2][j] > A[n - 1][j]
We define a position [i, j] is a peak if:

  A[i][j] > A[i + 1][j] && A[i][j] > A[i - 1][j] && 
  A[i][j] > A[i][j + 1] && A[i][j] > A[i][j - 1]
Find a peak element in this matrix. Return the index of the peak.

Guarantee that there is at least one peak, and if there are multiple peaks, return any one of them.

Have you met this question in a real interview?  
Example
Example 1:

Input: 
    [
      [1, 2, 3, 6,  5],
      [16,41,23,22, 6],
      [15,17,24,21, 7],
      [14,18,19,20,10],
      [13,14,11,10, 9]
    ]
Output: [1,1]
Explanation: [2,2] is also acceptable. The element at [1,1] is 41, greater than every element adjacent to it.
Example 2:

Input: 
    [
      [1, 5, 3],
      [4,10, 9],
      [2, 8, 7]
    ]
Output: [1,1]
Explanation: There is only one peek.
Challenge
Solve it in O(n+m) time.

If you come up with an algorithm that you thought it is O(nlogm) or O(mlogn), can you prove it is actually O(n+m) or propose a similar but O(n+m) algorithm?
"""
class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        if not A or not A[0]:
            return None
            
        return self.find_peak(A, 0, len(A) - 1, 0, len(A[0]) - 1)
        
    def find_peak(self, matrix, top, bottom, left, right):
        if top + 1 >= bottom and left + 1 >= right:
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    if self.is_peak(matrix, row, col):
                        return [row, col]
            return [-1, -1]
            
        if bottom - top < right - left:
            col = (left + right) // 2
            row = self.find_col_peak(matrix, col, top, bottom)
            if self.is_peak(matrix, row, col):
                return [row, col]
            if matrix[row][col - 1] > matrix[row][col]:
                return self.find_peak(matrix, top, bottom, left, col - 1)
            return self.find_peak(matrix, top, bottom, col + 1, right)
            
        row = (top + bottom) // 2
        col = self.find_row_peak(matrix, row, left, right)
        if self.is_peak(matrix, row, col):
            return [row, col]
        if matrix[row - 1][col] > matrix[row][col]:
            return self.find_peak(matrix, top, row - 1, left, right)
        return self.find_peak(matrix, row + 1, bottom, left, right)
        
    def is_peak(self, matrix, x, y):
        return matrix[x][y] == max(
            matrix[x][y],
            matrix[x - 1][y],
            matrix[x][y - 1],
            matrix[x][y + 1],
            matrix[x + 1][y],
        )

    def find_row_peak(self, matrix, row, left, right):
        peak_val = -sys.maxsize
        peak = []
        for col in range(left, right + 1):
            if matrix[row][col] > peak_val:
                peak_val = matrix[row][col]
                peak = col
        return peak
        
    def find_col_peak(self, matrix, col, top, bottom):
        peak_val = -sys.maxsize
        peak = None
        for row in range(top, bottom + 1):
            if matrix[row][col] > peak_val:
                peak_val = matrix[row][col]
                peak = row
        return peak