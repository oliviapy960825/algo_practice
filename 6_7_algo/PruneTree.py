#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 14:32:10 2020

@author: wangpeiyu
"""

"""
#146 Medium
This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0

should be pruned to:

   0
  / \
 1   0
    /
   1

We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root:
                return None
            left=helper(root.left)
            right=helper(root.right)
            if not left:
                root.left=None
            if not right:
                root.right=None
            return root.val==1 or left or right
        
            
        return root if helper(root) else None
                
    
#or
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if not root.left and not root.right and root.val==0:
            return None
        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)
        if not root.left:
            root.left=None
        if not root.right:
            root.right=None
        if root.val==1 or root.left or root.right:
            return root
        return None
                