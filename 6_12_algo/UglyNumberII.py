#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:36:41 2020

@author: wangpeiyu
"""

"""
4. Ugly Number II

Ugly number is a number that only have prime factors 2, 3 and 5.

Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Note that 1 is typically treated as an ugly number.

Have you met this question in a real interview?  
Example
Example 1:

Input: 9
Output: 10
Example 2:

Input: 1
Output: 1
Challenge
O(n log n) or O(n) time.
"""

import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        if n==1:
            return 1
            
        heap=[]
        heapq.heappush(heap, 1)
        seen=set()
        seen.add(1)
        curr=1
        for _ in range(n):
            small=heapq.heappop(heap)
            for j in [2,3,5]:
                new=small*j
                if new not in seen:
                    seen.add(new)
                    heapq.heappush(heap, new)
                    
        return small
                
