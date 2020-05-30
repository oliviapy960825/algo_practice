#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:23:57 2020

@author: wangpeiyu
"""

"""
Lintcode 617. Maximum Average Subarray II

Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or equal to given length k.

It's guaranteed that the size of the array is greater or equal to k.

Have you met this question in a real interview?  
Example
Example 1:

Input:
[1,12,-5,-6,50,3]
3
Output:
15.667
Explanation:
 (-6 + 50 + 3) / 3 = 15.667
Example 2:

Input:
[5]
1
Output:
5.000
"""

class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        if not nums or len(nums)==0 or not k or k==0:
            return 0
        if len(nums)<=k:
            return sum(nums)/len(nums)
        def check_array(nums,k,average):
            prefix_sum=[0]
            for num in nums:
                prefix_sum.append(prefix_sum[-1]+num-average)
            min_prefix_sum=0
            for i in range(k,len(nums)+1):
                if prefix_sum[i]-min_prefix_sum>=0:
                    return True
                min_prefix_sum=min(min_prefix_sum,prefix_sum[i-k+1])
            return False
        start=min(nums)
        end=max(nums)
        while start<end-1e-5:
            mid=start+(end-start)/2
            if check_array(nums,k,mid):
                start=mid
            else:
                end=mid
                
        return start
            