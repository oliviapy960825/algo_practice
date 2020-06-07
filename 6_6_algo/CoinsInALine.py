#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:46:26 2020

@author: wangpeiyu
"""

"""
394. Coins in a Line

There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.

Could you please decide the first player will win or lose?

If the first player wins, return true, otherwise return false.

Have you met this question in a real interview?  
Example
Example 1:

Input: 1
Output: true
Example 2:

Input: 4
Output: true
Explanation:
The first player takes 1 coin at first. Then there are 3 coins left.
Whether the second player takes 1 coin or two, then the first player can take all coin(s) left.
Challenge
O(n) time and O(1) memory
"""
class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n==0:
            return False
        if n<=2:
            return True
        dp=[False, True, True]
        
        for i in range(3,n+1):
            dp.append(not dp[i-1] or not dp[i-2])
            
        return dp[-1]
    
#O(N) time and O(1) space:
class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n==0:
            return False
        if n<=2:
            return True
        dp_1=True
        dp_2=True
        dp=False
        for i in range(3,n+1):
            dp=not dp_1 or not dp_2
            dp_1=dp_2
            dp_2=dp
            
        return dp