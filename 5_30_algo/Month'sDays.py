#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:59:23 2020

@author: wangpeiyu
"""

"""
Lintcode 1141. The month's days

Given a year and month, return the days of that month.

1 \leq year \leq 100001≤year≤10000
1 \leq month \leq 121≤month≤12

Have you met this question in a real interview?  
Example
Example 1:

Input: 
2020 
2
Output: 
29
Example 2:

Input: 
2020 
3
Output: 
31
"""
class Solution:
    """
    @param year: a number year
    @param month: a number month
    @return: Given the year and the month, return the number of days of the month.
    """
    
    def getTheMonthDays(self, year, month):
        NORMAL_YM=[-1,31,28,31,30,31,30,31,31,30,31,30,31]
        # write your code here
        if month==0:
            return NORMAL_YM[0]
        def isLeapYear(year):
            if year%4==0 and year%100!=0 or year%400==0:
                return True
            return False
        
        if month==2 and isLeapYear(year):
            return 29
        else:
            return NORMAL_YM[month]
            