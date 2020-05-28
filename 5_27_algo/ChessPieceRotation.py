#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 20:40:43 2020

@author: wangpeiyu
"""

"""
Lintcode 1146. Chess piece rotation
The 4x4 board is filled with black and white pieces. The positions and numbers of black and white are random. The coordinates of the upper left corner are (1,1) and the coordinates of the lower right corner are (4,4). Now there are some flip operations in turn. The colors of the four pieces up, down, left, and right are centered on the given pivot coordinates. Please calculate the color of the board after the flip.
Given two arrays A and f, they are the initial chessboard and flip position, respectively. There are 3 flip positions.

Please return to the flipped board.

Have you met this question in a real interview?  
Example
Example 1:

Input: 
A:[[0,0,1,1],[1,0,1,0],[0,1,1,0],[0,0,1,0]]
F：[[2,2],[3,3],[4,4]]
Output: [[0,1,1,1],[0,0,1,0],[0,1,1,0],[0,0,1,0]]
"""
class Solution:
    """
    @param A: Initial chessboard
    @param F: Flipped coordinates
    @return:  return to the flipped board.
    """
    def ChessPieceRotation(self, A, F):
        # write your code here
        if not A:
            return [[]]
        if not F:
            return A
        dx=[0,-1,0,1]
        dy=[1,0,-1,0]
        for index in F:
            x=index[0]-1
            y=index[1]-1
            for i in range(4):
                if x + dx[i] > -1 and x + dx[i] < 4 and y + dy[i] > -1 and y + dy[i] < 4:
                    A[x + dx[i]][y + dy[i]] = 1 - A[x + dx[i]][y + dy[i]]
                    
        return A