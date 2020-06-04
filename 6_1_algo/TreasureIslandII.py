#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:16:00 2020

@author: wangpeiyu
"""

"""
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.

Example:

Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).

Related problems:

    https://leetcode.com/problems/01-matrix


"""
def treasure_island(self, island):
    if not island or len(island)==0 or len(island[0])==0:
        return 0
    self.distance=float('INF')
    self.visited=[[False] for x in range(len(island[0])) for y in range(len(island))]
    
    def dfs(island, r, c, row, col, count):
        if r>=0 and r<row and c>=0 and c<col:
            if island[r][c]=='X':
                self.distance=min(self.distance, count+1)
                return
            self.visited[r][c]=True
            elif island[r][c]=='O' and not visited[r][c]:
                
                dfs(island, r+1, c, row, col, count+1)
                dfs(island, r-1, c, row, col, count+1)
                dfs(island, r, c+1, row, col, count+1)
                dfs(island, r, c-1, row, col, count+1)
            self.visited[r][c]=False
    row=len(island)
    col=len(island[0])
    for i in range(len(island)):
        for j in range(len(island[0])):
            if island[i][j]=='S':
                dfs(island,i,j,row,col)
                
    return self.distance
                
                
    