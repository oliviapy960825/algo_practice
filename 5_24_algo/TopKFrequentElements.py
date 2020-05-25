#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:11:13 2020

@author: wangpeiyu
"""

"""
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        if len(set(nums))<=k:
            return set(nums)
        nums=sorted(nums)
        index=0
        ele=nums[0]
        count=0
        dic={}
        while index<len(nums):
            if nums[index]==ele:
                count+=1
                index+=1
            else: #nums[index]!=ele
                dic[ele]=count
                ele=nums[index]
                count=1
                index+=1
        #we have an index of all elements
        
        dic={k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
        return list(dic.keys())[:k]
        

#heap  
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k==len(nums):
            return nums
        count=Counter(nums)
        return heapq.nlargest(k,count.keys(),key=count.get)             


