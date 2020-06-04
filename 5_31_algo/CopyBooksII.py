#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:33:58 2020

@author: wangpeiyu
"""

"""
Lintcode 438. Copy Books II

Given n books and each book has the same number of pages. There are k persons to copy these books and the i-th person needs times[i] minutes to copy a book.

Each person can copy any number of books and they start copying at the same time. What's the best strategy to assign books so that the job can be finished at the earliest time?

Return the shortest time.

Have you met this question in a real interview?  
Example
Example 1:

Input: n = 4, times = [3, 2, 4]
Output: 4
Explanation: 
    First person spends 3 minutes to copy 1 book.
    Second person spends 4 minutes to copy 2 books.
    Third person spends 4 minutes to copy 1 book.
Example 2:

Input: n = 4, times = [3, 2, 4, 5]
Output: 4
Explanation: Use the same strategy as example 1 and the forth person does nothing.
"""

class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copyBooksII(self, n, times):
        # write your code here
        
        l=1
        r=min(times)*n
        
        while l+1<r:
            mid=l+(r-l)//2
            if self.ok(n,times,mid):
                r=mid
            else:
                l=mid
                
        if self.ok(n,times,l):
            return l
        return r
        
    def ok(self, n, times, tm):
        num=0
        for i in times:
            num+=tm//i
        return num>=n