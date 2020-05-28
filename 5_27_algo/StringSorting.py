#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 20:43:26 2020

@author: wangpeiyu
"""

"""
Lintcode 1153. string sorting

Given some string splited by ,, please sort them in lexicographical order.

String only contains lower cases.
The number of string is \leq 1\,000≤1000 and total length is \leq 10^5≤10
​5
​​ .
Have you met this question in a real interview?  
Example
Example 1

Input: "bb,aa,lintcode,c"
Output: "aa,bb,c,lintcode"
Explanation: "aa" < "bb" < "c" < "lintcode" in lexicographical order.
Challenge
Can you write sort function by yourself?

"""
class Solution:
    """
    @param s: string
    @return: sort string in lexicographical order
    """
    def sorting(self, s):
        # write your code here
        strings = s.split(',')
        self.qsort(0, len(strings) - 1, strings)
        ans = ""
        for i in range(len(strings)):
            if i > 0:
                ans += ","
            ans += strings[i]
        return ans
    def qsort(self, n, m, a):
        i = n
        j = m
        k = a[(n + m) // 2]
        while i <= j:
            while a[i] < k:
                i += 1
            while a[j] > k:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        if i < m:
            self.qsort(i, m, a)
        if n < j:
            self.qsort(n, j, a)
            