/*
Medium
*/
class Solution {
    public TreeNode helper(int[] preorder, int[] inorder, int inStart, int inEnd, int preStart, int preEnd){
        if(inStart > inEnd) return null;
        int val = preorder[preStart];
        TreeNode root = new TreeNode(val);
        int index = 0;
        for(int i = inStart; i <= inEnd; i++){
            if(inorder[i] == val) {
                index = i;
                break;
            }
        }
        int leftSize = index - inStart;
        root.left = helper(preorder, inorder, inStart, index - 1, preStart + 1, preStart + leftSize);
        root.right = helper(preorder, inorder, index + 1, inEnd, preStart + leftSize + 1, preEnd);
        return root;
    }
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return helper(preorder, inorder, 0, inorder.length - 1, 0, preorder.length - 1);
    }
}