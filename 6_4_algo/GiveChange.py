#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:28:20 2020

@author: wangpeiyu
"""

"""
1503. Give change

A country's currency system contains 44 kinds coins, their values are 11, 44, 1616, 6464, and a kind paper money, values 10241024.
You now used a paper money values 10241024 to buy a product values N, 0 < N <= 1024N,0<N<=1024, please calculate how many coins you'll received at least, for change.

Have you met this question in a real interview?  
Example
Sample Input1:
amount = 1014

Sample Output1:
4

there will be 2 coins value 4, and 2 coins value 1.
Sample Input2:
amount = 1004

Sample Output2:
2

there will be 1 coin value 16, and 1 coins value 4.
"""
#dp

PAPER=1024
COINS=[1,4,16,64]
class Solution:
    """
    @param amount: The amount you should pay.
    @return: Return the minimum number of coins for change.
    """
    def giveChange(self, amount):
        # write you code here.
        charge=PAPER-amount
        dp=[float('INF')]*(charge+1)
        dp[0]=0
        for coin in COINS:
            for i in range(coin, charge+1):
                dp[i]=min(dp[i],dp[i-coin]+1)
        return dp[-1] if dp[-1]!=float('INF') else -1
            

#greedy
    
class Solution:
    """
    @param amount: The amount you should pay.
    @return: Return the minimum number of coins for change.
    """
    def giveChange(self, amount):
        # write you code here.
        charge=PAPER-amount
        num1=charge//64
        print(num1)
        num2=(charge%64)//16
        print(num2)
        num3=((charge%64)%16)//4
        print(num3)
        num4=((charge%64)%16)%4
        print(num4)
        
        return num1+num2+num3+num4