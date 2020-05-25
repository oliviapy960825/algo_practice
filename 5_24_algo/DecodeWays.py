#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:20:05 2020

@author: wangpeiyu
"""

"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        self.dic={}
        index=0
        def dp(s,index):
            if index==len(s):
                return 1
            if s[index]=='0':
                return 0
            if index==len(s)-1:
                return 1
            if index in self.dic:
                return self.dic[index]
            else:
                ans=dp(s,index+1)+(dp(s,index+2) if (int(s[index:index+2])<=26) else 0)
                self.dic[index]=ans 
                return ans
                    
        count=dp(s,0)
        return count
            