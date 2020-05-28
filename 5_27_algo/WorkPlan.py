#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 20:42:04 2020

@author: wangpeiyu
"""

"""
Lintcode 1147. Work Plan

Xiaomei is the manager in charge of the team and needs to make the work plans for the team to help the team generate the most value. Every week, the team will have alternative tasks, one is a simple task, and the other is a complex task. In week i, the value of the team’s completion of simple tasks is low_ilow
​i
​​ , and the value of completion of complex tasks is high_ihigh
​i
​​ . Due to the technical difficulty of the complex task itself, if the team chooses to perform the complex task in week i, they need to concentrate on preparation without doing any task in week i-1. If the team choose to perform a simple task in week i, there is no need to make any preparations in advance. Now that Xiaomei's team has received a list of expected tasks for the next n weeks, please help Xiaomei determine the weekly work schedule that help the team generate the most value.

1 \leq |low|,|high| \leq 100001≤∣low∣,∣high∣≤10000
1 \leq low[i],high[i] \leq 100001≤low[i],high[i]≤10000

Have you met this question in a real interview?  
Example
Example 1:

Input:low=[4,2,3,7],hard=[3,5,6,9]
output:17
Explanation:
Pick simple task in the first week, value = 4
Prepare for the second week and pick complex task in the third week, value = 4 + 6 = 10
Pick a simple task in the fourth week, value = 10 + 7 = 17
Example 2:

Input:low=[1,3,5,9],high=[3,5,7,9]
Output:19
"""

class Solution:
    """
    @param low: the simple task
    @param high: the complex task
    @return: the most value
    """
    def workPlan(self, low, high):
        # Write your code here.
        n=len(low)
        dp=[0 for i in range(10500)]
        dp[1]=low[0]
        for i in range(2,n+1):
            dp[i]=max(dp[i-1]+low[i-1], dp[i-2]+high[i-1])
            
        return dp[n]