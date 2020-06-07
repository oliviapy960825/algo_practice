#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:51:25 2020

@author: wangpeiyu
"""

"""
512. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

we can't decode an empty string. So you should return 0 if the message is empty.
The length of message n \leq 100n≤100

Have you met this question in a real interview?  
Example
Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as AB (1 2) or L (12).
Example 2:

Input: "10"
Output: 1

"""
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if not s or len(s)==0 or s=='0':
            return 0
        if int(s)<=10:
            return 1
        dp=[0]*(len(s)+1)
        
        dp[0]=1
        dp[1]=1
        
        for i in range(2, len(s)+1):
            if 10<=int(s[i-2:i])<=26:
                dp[i]+=dp[i-2]
                
            if int(s[i-1:i])!=0:
                dp[i]+=dp[i-1]
                
            if dp[i]==0:
                return 0
                
        return dp[-1]

