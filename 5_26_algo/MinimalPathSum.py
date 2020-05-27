#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:01:18 2020

@author: wangpeiyu
"""

"""
#135

This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1

"""

def isLeaf(root):
    if not root:
        return False
    if not root.left and not root.right:
        return True
    return False

def helper(root,pa_sum):
    if isLeaf(root):
        return pa_sum+root.val
    if root.left and not root.right:
        return helper(root.left,pa_sum+root.val)
    if root.right and not root.left:
        return helper(root.right, pa_sum+root.val)
    return min(helper(root.left,pa_sum+root.val),helper(root.right,pa_sum+root.val))


def minPathSum(root):
    if not root:
        return 0
    return helper(root,0)
    
    