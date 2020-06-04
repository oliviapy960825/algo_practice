#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:58:44 2020

@author: wangpeiyu
"""

"""
Lintcode 200. Longest Palindromic Substring

Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

Have you met this question in a real interview?  
Example
Example 1:

Input:"abcdzdcab"
Output:"cdzdc"
Example 2:

Input:"aba"
Output:"aba"
Challenge
O(n2) time is acceptable. Can you do it in O(n) time.
"""
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s or len(s) < 2:
            return s
        
        string=""
        
        for i in range(len(s)):
            left=self.is_palindrom(s,i,i)
            if len(left)>len(string):
                string=left
            right=self.is_palindrom(s,i,i+1)
            if len(right)>len(string):
                string=right
                
        return string
            
    def is_palindrom(self, s, start, end):
        while start>=0 and end<len(s):
            if s[start]!=s[end]:
                break
            start-=1
            end+=1
            
        return s[start+1:end]