#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:40:34 2020

@author: wangpeiyu
"""

"""
Lintcode 122. Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Have you met this question in a real interview?  
Example
Example 1:

Input：[2,1,5,6,2,3]
Output：10
Explanation：
The third and fourth rectangular truncated rectangle has an area of 2*5=10.
Example 2:

Input：[1,1]
Output：2
Explanation：
The first and second rectangular truncated rectangle has an area of 2*1=2.
"""

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        # write your code here
        indices_stack=[]
        area=0
        for index, height in enumerate(heights+[0]):
            while indices_stack and heights[indices_stack[-1]]>=height:
                popped_index=indices_stack.pop()
                left_index=indices_stack[-1] if indices_stack else -1
                width=index-left_index-1
                area=max(area, heights[popped_index]*width)
                
            indices_stack.append(index)
            
        return area