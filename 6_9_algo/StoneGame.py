#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:52:11 2020

@author: wangpeiyu
"""

"""

"""
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # write your code here
            
        return self.memoSearch(A, 0, len(A)-1, {})
    def memoSearch(self, A, left, right, memo):
        if (left, right) in memo:
            return memo[(left, right)]
        if left>=right:
            return 0
        cost=sum(A[left:right+1])
        minimum=float('INF')
        for mid in range(left, right):
            l=self.memoSearch(A, left, mid, memo)
            r=self.memoSearch(A, mid+1, right, memo)
            minimum=min(minimum, l+r+cost)
            
        memo[(left, right)]=minimum
        return minimum