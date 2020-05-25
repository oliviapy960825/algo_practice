#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:38:35 2020

@author: wangpeiyu
"""

"""
286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

DIRECTION=[[0,1],[1,0],[-1,0],[0,-1]]
GATE=0
EMPTY=2147483647
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        if len(rooms)==0 or not rooms:
            return None
        m=len(rooms)
        n=len(rooms[0])
        lst=[]
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==GATE:
                    lst.append([i,j])
                    
        while lst:
            [row,col]=lst.pop(0)
            for direction in DIRECTION:
                r=row+direction[0]
                c=col+direction[1]
                if r<0 or c<0 or r>=m or c>=n or rooms[r][c]!=EMPTY:
                    continue
                rooms[r][c]=rooms[row][col]
                lst.append([r,c])
                
                
        
                