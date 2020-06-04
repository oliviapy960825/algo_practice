#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:51:51 2020

@author: wangpeiyu
"""

"""
Lintcode 362. Sliding Window Maximum

Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.

Have you met this question in a real interview?  
Example
Example 1:

Input:
[1,2,7,7,8]
3
输出:
[7,7,8]

Explanation：
At first the window is at the start of the array like this `[|1, 2, 7| ,7, 8]` , return the maximum `7`;
then the window move one step forward.`[1, |2, 7 ,7|, 8]`, return the maximum `7`;
then the window move one step forward again.`[1, 2, |7, 7, 8|]`, return the maximum `8`;
Example 2:

Input:
[1,2,3,1,2,3]
5
Output:
[3,3]

Explanation:
At first, the state of the window is as follows: ` [,2,3,1,2,1 | , 3] `, a maximum of ` 3 `;
And then the window to the right one. ` [1, | 2,3,1,2,3 |] `, a maximum of ` 3 `;
Challenge
o(n) time and O(k) memory
"""

#O(k*n)
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums or not k:
            return []
        if k>=len(nums):
            return [max(nums)]
        lst=[]
        for i in range(len(nums)-k+1):
            lst.append(max(nums[i:i+k]))
            
        return lst
                


#O(n)
    
from collections import deque
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums or not k:
            return []
        if k>=len(nums):
            return [max(nums)]
        
        dq=deque([])
        
        for i in range(k-1):
            self.push(dq,nums,i)
            
        result=[]
        
        for i in range(k-1, len(nums)):
            self.push(dq, nums, i)
            result.append(nums[dq[0]])
            if dq[0]==i-k+1:
                dq.popleft()
                
        return result
        
        
    def push(self, dq, nums, i):
        while dq and nums[i]>nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        
        
        
        
                
              
