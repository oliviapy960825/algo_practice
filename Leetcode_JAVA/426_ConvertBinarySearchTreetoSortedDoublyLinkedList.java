/*
Medium
*/
class Solution {
    Node first = null, last = null;
    public void helper(Node root){
        if(root == null)
            return ;
        helper(root.left);
        if(last != null){
            last.right = root;
            root.left = last;
        }
        else
            first = root;
        
        last = root;
        helper(root.right);
    }
    public Node treeToDoublyList(Node root) {
        if(root == null)
            return null;
        
        helper(root);
        first.left = last;
        last.right = first;
        
        return first;
    }
}