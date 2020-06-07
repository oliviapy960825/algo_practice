#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:17:33 2020

@author: wangpeiyu
"""

"""
395. Coins in a Line II
There are n coins with different value in a line. Two players take turns to take one or two coins from left side until there are no more coins left. The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?

If the first player wins, return true, otherwise return false.

Have you met this question in a real interview?  
Example
Example 1:

Input: [1, 2, 2]
Output: true
Explanation: The first player takes 2 coins.
Example 2:

Input: [1, 2, 4]
Output: false
Explanation: Whether the first player takes 1 coin or 2, the second player will gain more value.


"""

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        if len(values)<=2:
            return True
            
        dp=[0]*(len(values)+1)
        Sum=0
        size=len(values)
        dp[len(values)]=0
        dp[len(values)-1]=values[-1]
        dp[len(values)-2]=values[-2]+values[-1]
        dp[len(values)-3]=values[-2]+values[-3]
        Sum += (values[size - 1] + values[size - 2] + values[size - 3])
        for i in range(len(values)-4, -1, -1):
            Sum+=values[i]
            dp[i]=max(values[i]+ min(dp[i+2], dp[i+3]), values[i]+values[i+1]+min(dp[i+3], dp[i+4]))
            
        return dp[0]>Sum-dp[0]