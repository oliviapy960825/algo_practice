#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:39:08 2020

@author: wangpeiyu
"""

"""
94. Binary Tree Maximum Path Sum

Description
中文
English
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

Have you met this question in a real interview?  
Example
Example 1:
	Input:  For the following binary tree（only one node）:
	2
	Output：2
	
Example 2:
	Input:  For the following binary tree:

      1
     / \
    2   3
		
	Output: 6


"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
            
        max_sum, _ = self.helper(root)
        return max_sum
            
    def helper(self, root):
        if not root:
            return -float('INF'), 0
        left=self.helper(root.left)
        right=self.helper(root.right)
        max_sum=max(left[0], right[0], left[1]+right[1]+root.val)
        single=max(left[1]+root.val, right[1]+root.val, 0)
        
        return max_sum, single
