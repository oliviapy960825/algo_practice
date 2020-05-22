"""
Lintcode 126. Max Tree

Given an integer array with no duplicates. A max tree building on this array is defined as follow:

The root is the maximum number in the array
The left subtree and right subtree are the max trees of the subarray divided by the root number.
Construct the max tree by the given array.

Have you met this question in a real interview?  
Example
Example 1:

Input：[2, 5, 6, 0, 3, 1]
Output：{6,5,3,2,#,0,1}
Explanation：
the max tree constructed by this array is:
    6
   / \
  5   3
 /   / \
2   0   1
Example 2:

Input：[6,4,20]
Output：{20,6,#,#,4}
Explanation： 
     20
     / 
    6
     \
      4

Challenge
O(n) time and memory.

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
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        # write your code here
        stack=[]
        for num in A:
            node=TreeNode(num)
            while stack and num>stack[-1].val:
                node.left=stack.pop()
                
            if stack:
                stack[-1].right=node
                
            stack.append(node)
            
        return stack[0]