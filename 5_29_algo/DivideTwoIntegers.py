#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:16:36 2020

@author: wangpeiyu
"""

"""
Lintcode 414. Divide Two Integers

Divide two integers without using multiplication, division and mod operator.

If it will overflow(exceeding 32-bit signed integer representation range), return 2147483647

The integer division should truncate toward zero.

Have you met this question in a real interview?  
Example
Example 1:

Input: dividend = 0, divisor = 1
Output: 0
Example 2:

Input: dividend = 100, divisor = 9
Output: 11
"""

class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        INT_MAX=2147483647
        if divisor==0:
            return INT_MAX
            
        neg=dividend>0 and divisor<0 or dividend<0 and divisor>0
        a,b=abs(dividend), abs(divisor)
        ans, shift=0, 31
        while shift>=0:
            if a>=b<<shift:
                a-=b<<shift
                ans+=1<<shift
            shift-=1
        if neg:
            ans=-ans
        if ans>INT_MAX:
            return INT_MAX
        return ans