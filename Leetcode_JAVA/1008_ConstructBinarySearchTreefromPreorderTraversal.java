/*
Medium
*/
class Solution {
    public TreeNode build(int[] preorder, int left, int right){
        if (left > right){
            return null;
        }
        if (left == right){
            return new TreeNode(preorder[left]);
        }
        TreeNode root = new TreeNode(preorder[left]);
        int idx = right;
        while (left < idx){
            if (preorder[idx] > root.val){
                idx --;
            }
            else{
                break;
            }
        }
        root.left = build(preorder, left + 1, idx);
        root.right = build(preorder, idx + 1, right);
        return root;
    }
    public TreeNode bstFromPreorder(int[] preorder) {
        if(preorder.length == 0){
            return null;
        }
        TreeNode root = build(preorder, 0, preorder.length - 1);
        return root;
    }
}