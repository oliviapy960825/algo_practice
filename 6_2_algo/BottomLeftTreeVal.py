#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:31:37 2020

@author: wangpeiyu
"""

"""
Leetcode 513. Find Bottom Left Tree Value

 Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

    2
   / \
  1   3

Output:
1

Example 2:

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Note: You may assume the tree (i.e., the given root node) is not NULL. 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.level=0
        self.value=root.val
        def bottomLeft(root, level):
            if not root:
                return 
            bottomLeft(root.left, level+1)
            if level>self.level:
                self.level=level
                self.value=root.val
            bottomLeft(root.right, level+1)
            
        bottomLeft(root,0)
        return self.value