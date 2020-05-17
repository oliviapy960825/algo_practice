/* Leetcode 653. Two Sum IV - Input is a BST
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

*/

class Solution {
    public boolean findTarget(TreeNode root, int k) {
        Set<Integer> set=new HashSet();
        Queue<TreeNode> queue=new LinkedList();
        queue.add(root);
        while(!queue.isEmpty()){
            if(queue.peek()!=null){
                TreeNode node=queue.remove();
                if (set.contains(k-node.val)){
                    return true;
                }
                set.add(node.val);
                queue.add(node.left);
                queue.add(node.right);
            }
            else{
                queue.remove();
            }
        }
        return false;
    }
}