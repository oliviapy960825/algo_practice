#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:40:59 2020

@author: wangpeiyu
"""

"""
77. Longest Common Subsequence

Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.

Have you met this question in a real interview?  
Clarification
What's the definition of Longest Common Subsequence?

https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
http://baike.baidu.com/view/2020307.htm
Example
Example 1:
	Input:  "ABCD" and "EDCA"
	Output:  1
	
	Explanation:
	LCS is 'A' or  'D' or 'C'


Example 2:
	Input: "ABCD" and "EACB"
	Output:  2
	
	Explanation: 
	LCS is "AC"
"""

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        if not A or len(A)==0 or not B or len(B)==0:
            return 0
        length=min(len(A), len(B))
        dp=[[0]*(len(A)+1) for _ in range(len(B)+1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j])
                    
        return dp[len(A)][len(B)]