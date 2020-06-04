#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:59:10 2020

@author: wangpeiyu
"""

"""
#142 Hard


This problem was asked by Google.

You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
"""

#Greedy

class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s or len(s)==0:
            return True
        lo=hi=0
        for c in s:
            lo+=1 if c=="(" else -1
            hi+=1 if c!=")" else -1
            
            if hi<0:
                break
            lo=max(lo,0)
            
        return lo==0
    
#DP
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s or len(s)==0:
            return True
        LEFTY='(*'
        RIGHTY=')*'
        n=len(s)
        dp=[[False] * n for _ in s]
        for i in range(n):
            if s[i]=="*":
                dp[i][i]=True
            if i<n-1 and s[i] in LEFTY and s[i+1] in RIGHTY:
                dp[i][i+1]=True
        for size in range(2, n):
            for i in range(n-size):
                if s[i]=='*' and dp[i+1][i+size]:
                    dp[i][i+size]=True
                elif s[i] in LEFTY:
                    for k in range(i+1, i+size+1):
                        if s[k] in RIGHTY and (k==i+1 or dp[i+1][k-1]) and (k==i+size or dp[k+1][i+size]):
                            dp[i][i+size]=True
                            
        return dp[0][-1]