#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:23:04 2020

@author: wangpeiyu
"""

"""
1891. Travel Plan

There are n cities, and the adjacency matrixarr represents the distance between any two cities.arr[i][j] represents the distance from city i to city j.Alice made a travel plan on the weekend. She started from city 0, then she traveled other cities 1 ~ n-1, and finally returned to city 0. Alice wants to know the minimum distance she needs to walk to complete the travel plan. Return this minimum distance. Each city can only pass once except city 0.

n<=10
arr[i][j]<=10000

Have you met this question in a real interview?  
Example
Example 1:

Input:[[0,1,2],[1,0,2],[2,1,0]]
Output:4
Explanation:
There are two possible plans.
The first, city 0-> city 1-> city 2-> city 0, cost = 5.
The second, city 0-> city 2-> city 1-> city 0, cost = 4.
Return 4
Example 2:

Input:[[0,10000,2],[5,0,10000],[10000,4,0]]
Output:11

"""

class Solution:
    """
    @param arr: the distance between any two cities
    @return: the minimum distance Alice needs to walk to complete the travel plan
    """
    def travelPlan(self, arr):
        # Write your code here.
        if not arr or len(arr)==0 or len(arr[0])==0:
            return 0
        col=len(arr[0])
        self.min_d=float('INF')
        for i in range(1, col):
            visited=[i]
            d=arr[0][i]
            self.dfs(arr, visited, d, col)
        return self.min_d
            
            
    def dfs(self, arr, visited, d, l):
        if len(visited)==l-1:
            c=visited[-1]
            self.min_d=min(self.min_d, d+arr[c][0])
            return 
        for i in range(1, l):
            c=visited[-1]
            if i not in visited:
                self.dfs(arr, visited + [i], d + arr[c][i], l)
                    
                
        
        