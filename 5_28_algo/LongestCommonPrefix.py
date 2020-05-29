#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:42:09 2020

@author: wangpeiyu
"""

"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0 or not strs:
            return ""
        if len(strs)<=1:
            return strs[0]
        def common_pre(str1,str2):
            new_str=""
            if not str1 or not str2:
                return ""
            if len(str1)<len(str2):
                return common_pre(str2,str1)
            i=0
            while i<len(str2):
                if str1[i]==str2[i]:
                    new_str+=str1[i]
                    i+=1
                else:
                    break
            return new_str
        
        prefix=strs[0]
        for i in range(1,len(strs)):
            prefix=common_pre(prefix,strs[i])
            
        return prefix