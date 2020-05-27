#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:56:16 2020

@author: wangpeiyu
"""
"""

Lintcode 1161. goods transfer 

There are n backpacks, each of which can carry a[i] goods, and the maximum capacity of each backpack is b[i]. If it takes 1 second to transfer one piece of goods, how many backpacks can hold all the goods at least, and how much time does it take to transfer?

1<=n<=100
1<=ai<=1000
1<=bi<=1000
ai<=bi
Have you met this question in a real interview?  
Example
Example

Input
4
[3, 3, 4, 3]
[4, 7, 6, 5]
Output 2 6 
Explanation:
We can put the goods in the first bag all moved to the second backpack, take time for 3 seconds, at this point the second of the residual capacity of backpack is 1, and then put the goods in the fourth incubator transfer a into the second bag, transfer the last two to the third in the backpack. Take time for 3 seconds, so the minimum heat preservation box number is 2, at least spend time for 6 seconds.

"""
class Solution:
    """
    @param n: the number of backpacks
    @param a: the number of goods each backpack carries
    @param b:  the maximum capacity of each backpack
    @return: given n, ai and bi,return the minimum number of backpacks and the minimum time
    """
    def goodsTransfer(self, n, a, b):
        # write your code here
        INF = 0x3f3f3f3f
        k = INF
        sum_good = 0
        sum_cap = 0
        max_weight = 0
        for good in a:
            sum_good += good
        for cap in b:
            sum_cap += cap
        dp = [INF for _ in range(sum_cap + 1)]
        weight = [0 for _ in range(sum_cap + 1)]
        dp[0] = 0
        for i in range(n):
            j = sum_cap
            while j > 0:
                res = max(j - b[i], 0)
                if dp[j] < dp[res] + 1:
                    j -= 1
                    continue
                if dp[j] > dp[res] + 1:
                    dp[j] = dp[res] + 1
                    weight[j] = weight[res] + a[i]
                else :
                    weight[j] = max(weight[j], weight[res] + a[i])
                j -= 1
        for i in range(sum_good, sum_cap + 1):
            if dp[i] < k:
                k, max_weight = [dp[i],  weight[i]]
            elif dp[i] == k:
                max_weight = max(max_weight, weight[i])
        return [k, sum_good - max_weight]