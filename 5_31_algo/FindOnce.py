#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:57:46 2020

@author: wangpeiyu
"""

"""
#140 Medium
This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and 
all other elements appear exactly twice, find the two elements that appear 
only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. 
The order does not matter.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        length=len(nums)
        lst=[]
        dic={}
        for i in range(length):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
                
        for i in dic.keys():
            if dic[i]==1:
                lst.append(i)
                
        return lst