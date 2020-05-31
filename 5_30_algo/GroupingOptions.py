#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:24:20 2020

@author: wangpeiyu
"""

"""
Lintcode 1834. Grouping Options

There are nn people in a row. They must all be divided into mm contiguous groups from left to right. If each group must be at least as large as the group to its left, determine how many distinct ways groups can be formed. For a group to be distinct, it must differ in size for at least one group when sorted ascending. For example, [1, 1, 1, 3] is distinct from [1, 1, 1, 2] but not from [1, 3, 1, 1].

1 \leq n,m \leq 2001≤n,m≤200

Have you met this question in a real interview?  
Example
Input:
8
4
Output: 5
Explanation: [1, 1, 1, 5], [1, 1, 2, 4], [1, 1, 3, 3], [1, 2, 2, 3], [2, 2, 2, 2]
"""

class Solution:
    """
    @param n: the number of people
    @param m: the number of groups
    @return: the number of grouping options
    """
    def groupingOptions(self, n, m):
        # write your code here
        if m>n:
            return 0
            
        dp=[[0]*(n+1) for j in range(n+1) ]
        for i in range(n+1):
            dp[i][i]=1
        for i in range(2,n+1,1):
            for j in range(1,i,1):
                for k in range(1,j+1,1):
                    dp[i][j]=dp[i][j]+dp[i-j][k]
                    
        return dp[n][m]