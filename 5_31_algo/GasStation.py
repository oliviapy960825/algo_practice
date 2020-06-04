#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:57:22 2020

@author: wangpeiyu
"""

"""
Lintcode 187. Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

The solution is guaranteed to be unique.

Have you met this question in a real interview?  
Example
Example 1:

Input:gas[i]=[1,1,3,1],cost[i]=[2,2,1,1]
Output:2
Example 2:

Input:gas[i]=[1,1,3,1],cost[i]=[2,2,10,1]
Output:-1
Challenge
O(n) time and O(1) extra space
"""

class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        n = len(gas)        
        diff = []
        for i in range(n): diff.append(gas[i]-cost[i])
        for i in range(n): diff.append(gas[i]-cost[i])
        if n==1:
            if diff[0]>=0: return 0
            else: return -1
        st = 0
        now = 1
        tot = diff[0]
        while st<n:
            while tot<0:
                st = now
                now += 1
                tot = diff[st]
                if st>n: return -1
            while now!=st+n and tot>=0:
                tot += diff[now]
                now += 1
            if now==st+n and tot>=0: return st
        return -1