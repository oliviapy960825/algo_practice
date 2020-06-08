#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:36:15 2020

@author: wangpeiyu
"""

"""
191. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

It is guaranteed that the length of nums doesn't exceed 20000
The product of the largest subsequence of the product, less than 2147483647

Have you met this question in a real interview?  
Example
Example 1:

Input:[2,3,-2,4]
Output:6
Example 2:

Input:[-1,2,4,1]
Output:8
"""
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if not nums:
            return 0
        global_max=nums[0]
        prev_max=nums[0]
        prev_min=nums[0]
        
        for num in nums[1:]:
            if num>0:
                curr_max=max(num, prev_max*num)
                curr_min=min(num, prev_min*num)
                
            else:
                curr_max=max(num, prev_min*num)
                curr_min=min(num, prev_max*num)
                
            global_max=max(global_max, curr_max)
            prev_max, prev_min=curr_max, curr_min
        return global_max
                
            
