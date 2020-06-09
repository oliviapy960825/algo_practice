#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:47:32 2020

@author: wangpeiyu
"""

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character *, which can be treated as one of the numbers from 1 to 9.
Given the encoded message containing digits and the character *, return the total number of ways to decode it.
Also, since the answer may be very large, you should return the output mod 10^9 + 7.

The length of the input string will fit in range [1, 10^5].
The input string will only contain the character * and digits 0 - 9.
Have you met this question in a real interview?  
Example
Example 1

Input: "*"
Output: 9
Explanation: You can change it to "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2

Input: "1*"
Output: 18

"""

class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """
    def numDecodings(self, s):
        # write your code here
        if not s or len(s)==0 or s=='0':
            return 0
        if len(s)==1 and s[0]!='*':
            return 1
        if len(s)==1 and s[0]=='*':
            return 9
        n=len(s)
        MOD=1000000007
        dp=[0]*(len(s)+1)
        dp[0]=1
        dp[1]=1
        if s[0]!='*':
            dp[1]=1
        else:
            dp[1]=9
            
        for i in range(2, len(s)+1):
            if s[i-1]=='0':
                if s[i-2]=='1' or s[i-2]=='2':
                    dp[i]+=dp[i-2]
                elif s[i-2]=='*':
                    if s[i-1]<='6':
                        dp[i]+=2*dp[i-2]
                    else:
                        dp[i]+=dp[i-2]
            elif s[i-1]>='1' and s[i-1]<='9':
                dp[i]+=dp[i-1]
                if s[i-2]=='1' or s[i-2]=='2' and s[i-1]<='6':
                    dp[i]+=dp[i-2]
                elif s[i-2]=='*':
                    if s[i-1]<='6':
                        dp[i]+=2*dp[i-2]
                    else:
                        dp[i]+=dp[i-2]
            
            else: #s[i-1]=='*'
                dp[i]+=9*dp[i-1]
                if s[i-2]=='1':
                    dp[i]+=9*dp[i-2]
                elif s[i-2]=='2':
                    dp[i]+=6*dp[i-2]
                    
                elif s[i-2]=='*':
                    dp[i]+=15*dp[i-2]
                    
            dp[i]%=MOD
        return dp[n]
                