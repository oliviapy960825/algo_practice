#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:53:48 2020

@author: wangpeiyu
"""

"""
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums)<2:
            return nums
        def reverse(nums,start):
            i=start
            j=len(nums)-1
            while i<j:
                swap(nums,i,j)
                i+=1
                j-=1
                
        def swap(nums, i, j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            
        index=len(nums)-2
        while index>=0 and nums[index+1]<=nums[index]:
            index-=1
        if index>=0:
            j=len(nums)-1
            while j>=0 and nums[j]<=nums[index]:
                j-=1
            swap(nums,index,j)
        reverse(nums,index+1)
            
        