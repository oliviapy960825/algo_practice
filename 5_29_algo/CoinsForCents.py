#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:27:11 2020

@author: wangpeiyu
"""

"""
#138 Hard

This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount<1:
            return 0
        dp=[float('INF')]*(amount+1)
        dp[0]=0
        
        for coin in coins[::-1]:
            for x in range(coin, amount+1):
                dp[x]=min(dp[x],dp[x-coin]+1)
                
        return dp[amount] if dp[amount]!=float('INF') else -1