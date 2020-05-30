#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:09:38 2020

@author: wangpeiyu
"""

"""
Lintcode 633. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), guarantee that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
Have you met this question in a real interview?  
Example
Example 1:

Input:
[5,5,4,3,2,1]
Output:
5
Example 2:

Input:
[5,4,4,3,2,1]
Output:
4

"""

class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # write your code here
        if not nums or len(nums)==0:
            return None
        l=0
        r=len(nums)-1
        while l+1<r:
            mid=l+(r-l)//2
            if self.smaller_than_or_equal_to(nums,mid)>mid:
                r=mid
            else:
                l=mid
                
        if self.smaller_than_or_equal_to(nums,l)>l:
            return l
        return r
            
    def smaller_than_or_equal_to(self,nums,val):
        count=0
        for num in nums:
            if num<=val:
                count+=1
        return count