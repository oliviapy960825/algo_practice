#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:34:45 2020

@author: wangpeiyu
"""

"""
Lintcode 437. Copy Books

Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Return the shortest time that the slowest copier spends.

The sum of book pages is less than or equal to 2147483647

Have you met this question in a real interview?  
Example
Example 1:

Input: pages = [3, 2, 4], k = 2
Output: 5
Explanation: 
    First person spends 5 minutes to copy book 1 and book 2.
    Second person spends 4 minutes to copy book 3.
Example 2:

Input: pages = [3, 2, 4], k = 3
Output: 4
Explanation: Each person copies one of the books.
"""

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages or len(pages)==0:
            return 0
        def is_doable(pages,tl):
            count=0
            time_cost=0
            for page in pages:
                if time_cost+page>tl:
                    count+=1
                    time_cost=0
                time_cost+=page
            return count+1
                    
        l=max(pages)
        r=sum(pages)
        while l+1<r:
            mid=l+(r-l)//2
            if is_doable(pages,mid)<=k:
                r=mid
            else:
                l=mid
                
        if is_doable(pages,l)<=k:
            return l
            
        return r