#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:26:29 2020

@author: wangpeiyu
"""

"""
1426. Robot jumping

The robot is playing an ancient DOS-based game. There are N + 1 buildings in the game-numbered from 0 to N, arranged from left to right. The height of the building numbered 0 is 0 units, and the height of the building numbered i is H (i) units.
At first, the robot was at building number 0. At each step, it jumps to the next (right) building. Suppose the robot is in the k-th building and its current energy value is E. Next, it will jump to the k + 1 building. It will gain or lose energy proportional to the difference between H (k + 1) and E. If H (k + 1)> E then the robot will lose the energy value of H (k + 1)-E, otherwise it will get the energy value of E-H (k + 1).
The goal of the game is to reach the Nth building. In this process, the energy value cannot be a negative number of units. The question now is how much energy does the robot start the game in order to successfully complete the game?

1 \leq height.size() \leq 10^51≤height.size()≤10
​5
​​ 
1 \leq height[i] \leq 10^51≤height[i]≤10
​5
​​ 
Have you met this question in a real interview?  
Example
Example 1:

Input:
height:[3,4,3,2,4]
Output: 4
Explanation:
The initial energy is 4 to go from 0 to 4

"""

#binary search
class Solution:
    """
    @param height: the Building height
    @return: The minimum unit of initial energy required to complete the game
    """
    def LeastEnergy(self, height):
        # write your code here
        
        if not height or len(height)==0:
            return 0
        l=min(height)
        r=max(height)
        
        while l+1<r:
            mid=l+(r-l)//2
            if self.isDoable(height,mid):
                r=mid
            else:
                l=mid
                
        if self.isDoable(height, l):
            return l
        return r
            
    def isDoable(self, height, e):
        for i in range(len(height)):
            e=2*e-height[i]
            if e<0:
                return False
        return True
    
#dp
import math
class Solution:
    """
    @param height: the Building height
    @return: The minimum unit of initial energy required to complete the game
    """
    def LeastEnergy(self, height):
        # write your code here
        
        if not height or len(height)==0:
            return 0
        e=0
        for i in range(len(height)-1, -1, -1):
            e=(e+height[i]+1)//2
            
        return e