#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:04:01 2020

@author: wangpeiyu
"""

"""
Lintcode 1159. Longest Common Prefix III

You are given a string array arrarr consisting of nn strings, and a binary query array qq with size k. Each query consists of 2 integers x,y, and answer for the query is the length of the Longest Common Prefix of arr[x]arr[x] and arr[y]arr[y]. You are expected to return a array of size KK.

1 \leq n \leq 50001≤n≤5000
1 \leq K \leq 10^51≤K≤10
​5
​​ 
length of all stringsLL 1 \leq L \leq 10^51≤L≤10
​5
​​ 
string only have lower character

Have you met this question in a real interview?  
Example
input:["aab","aac","aacd"]
[[0,1],[0,2],[1,2]]
output:[2,2,3]
explation:
arr[0] and arr[1] LCP="aa" length=2
arr[0] and arr[2] LCP="aa" length=2
arr[1] and arr[2] LCP="aac" length=3
"""


class Solution:
    """
    @param arr: string array
    @param query: query array
    @return: return  LCP ans array
    """
    def queryLCP(self, arr, query):
        # write your code here
        if not arr or not query or len(arr)==0 or len(query)==0:
            return []
        lst=[]
        dic={}
        for (index1, index2) in query:
            if (index1, index2) not in dic:
                str1=arr[index1]
                str2=arr[index2]
                num=self.common_pre(str1,str2)
                lst.append(num)
                dic[(index1,index2)]=num
            else:
                lst.append(dic[(index1, index2)])
            
        return lst
        
    def common_pre(self, str1, str2):
        if not str1 or not str2:
            return 0
        if len(str1)<len(str2):
            return self.common_pre(str2,str1)
        r=len(str1)
        i=0
        while i<len(str2):
            if str1[i]==str2[i]:
                i+=1
            else:
                break
        return i
            