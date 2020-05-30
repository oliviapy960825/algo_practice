#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:24:27 2020

@author: wangpeiyu
"""

"""
Leetcode 322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

#TOP-DOWN DP

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount<1:
            return 0
        def helper(coins, rem, count):
            if rem<0:
                return -1
            if rem==0:
                return 0
            if count[rem-1]!=0:
                return count[rem-1]
            min_val=float('INF')
            for coin in coins:
                res=helper(coins, rem-coin, count)
                if res>=0 and res<min_val:
                    min_val=res+1
            count[rem-1]= -1 if (min_val==float('INF')) else min_val
            return count[rem-1]
        
        return helper(coins,amount,[0]*amount)
    
    
#BOTTOM-UP DP
        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount<1:
            return 0
        dp=[float('INF')]*(amount+1)
        dp[0]=0
        
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x]=min(dp[x],dp[x-coin]+1)
                
        return dp[amount] if dp[amount]!=float('INF') else -1
    
