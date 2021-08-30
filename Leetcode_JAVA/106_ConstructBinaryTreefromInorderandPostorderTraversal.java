/*
Medium
*/
class Solution {
    public TreeNode helper(int[] inorder, int[] postorder, int inStart, int inEnd, int postStart, int postEnd){
        if(inStart > inEnd) return null;
        int val = postorder[postEnd];
        TreeNode root = new TreeNode(val);
        int index = 0;
        for(int i = inEnd; i >= inStart; i--){
            if(inorder[i] == val){
                index = i;
                break;
            }
        }
        
        int right = inEnd - index;
        root.left = helper(inorder, postorder, inStart, index - 1, postStart, postEnd - right - 1);
        root.right = helper(inorder, postorder, index + 1, inEnd, postStart + right, postEnd - 1);
        return root;
    }
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        return helper(inorder, postorder, 0, inorder.length - 1, 0, postorder.length - 1);
    }
}