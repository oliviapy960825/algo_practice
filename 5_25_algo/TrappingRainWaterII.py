#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:29:32 2020

@author: wangpeiyu
"""

"""
364. Trapping Rain Water II


Given n x m non-negative integers representing an elevation map 2d where the area of each cell is 1 x 1, compute how much water it is able to trap after raining.



Have you met this question in a real interview?  
Example
Example 1:

Given `5*4` matrix 
Input:
[[12,13,0,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
Output:
14
Example 2:

Input:
[[2,2,2,2],[2,2,3,4],[3,3,3,1],[2,3,4,5]]
Output:
0
"""
import heapq


class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        if not heights:
            return 0
    
        self.initialize(heights)
        
        water = 0
        while self.borders:
            height, x, y = heapq.heappop(self.borders)
            for x_, y_ in self.adjcent(x, y):
                water += max(0, height - heights[x_][y_])
                self.add(x_, y_, max(height, heights[x_][y_]))

        return water

    def initialize(self, heights):
        self.n = len(heights)
        self.m = len(heights[0])
        self.visited = set()
        self.borders = []
        
        for index in range(self.n):
            self.add(index, 0, heights[index][0])
            self.add(index, self.m - 1, heights[index][self.m - 1])
            
        for index in range(self.m):
            self.add(0, index, heights[0][index])
            self.add(self.n - 1, index, heights[self.n - 1][index])
            
    def add(self, x, y, height):
        # add x, y, height to borders
        heapq.heappush(self.borders, (height, x, y))
        self.visited.add((x, y))
        
    def adjcent(self, x, y):
        adj = []
        for delta_x, delta_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_ = x + delta_x
            y_ = y + delta_y
            if 0 <= x_ < self.n and 0 <= y_ < self.m and (x_, y_) not in self.visited:
                adj.append((x_, y_))
        return adj