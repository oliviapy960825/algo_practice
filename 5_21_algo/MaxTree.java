/*
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
*/
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param A: Given an integer array with no duplicates.
     * @return: The root of max tree.
     */
    public TreeNode maxTree(int[] A) {
        // write your code here
        int len = A.length;
        TreeNode[] stk = new TreeNode[len];
        for (int i = 0; i < len; ++i)
            stk[i] = new TreeNode(0);			
        int cnt = 0;
        for (int i = 0; i < len; ++i) {
            TreeNode tmp = new TreeNode(A[i]);
            while (cnt > 0 && A[i] > stk[cnt-1].val) {		
                tmp.left = stk[cnt-1];						
                cnt --;
            }
            if (cnt > 0)									
                stk[cnt - 1].right = tmp;					
            stk[cnt++] = tmp;
        }
        return stk[0];
    }
}