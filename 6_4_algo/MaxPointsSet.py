#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:19:30 2020

@author: wangpeiyu
"""

"""
1356. Maximum Points Set

Given a list of coordinate points Points, where Points Point [i] [0] represents the horizontal axis coordinates, Points [i] [1] represents the vertical axis coordinates.
There is a point p that satisfies any point in Points that is not in the upper right area of p (both horizontal and vertical coordinates are greater than p), The point p is called the maximum point.
Return all max points, max points in the list are sorted in the order of X axis from small to large.

The number of points is within range: [1, 50000]
points[i][0] and points[i][1] are within range: [0, 100000]
Guarantee that the x and y are not repeated
Have you met this question in a real interview?  
Example
Example 1:
Input:
Points = [[1, 2], [5, 3], [4, 6], [7, 5], [9, 0]]
Output: [[4, 6], [7, 5], [9, 0]]
Explanation: There no point that x and y all greater than [4, 6], [7, 5], [9, 0]
Example 2:
Input:
Points = [[9,10],[7,8],[8,9],[1,1],[5,2]]
Output: [[9, 10]]
Explanation:  There no point that x and y all greater than [9, 10]
"""

class Solution:
    """
    @param Points: a list of [x, y]
    @return: return a list of points
    """
    def MaximumPointsSet(self, Points):
        # write your code here
        if not Points or len(Points)<=1:
            return Points
            
        lst=[]
        
        Points=sorted(Points, reverse=True)
        vis=[0]*len(Points)
        height=-1
        for i in range(len(Points)):
            if Points[i][1]>height:
                vis[i]=0
                height=max(height,Points[i][1])
                
        for i in range(len(Points)-1, -1, -1):
            if vis[i]==1:
                lst.append([Points[i][0],Points[i][1]])
                
        return lst