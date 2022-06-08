/*
This problem was asked by Yelp.

The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

    The horizontal distance of the root is 0.
    The horizontal distance of a left child is hd(parent) - 1.
    The horizontal distance of a right child is hd(parent) + 1.

For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8

The bottom view of a tree, then, consists of the lowest node at each horizontal distance. If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].

Given the root to a binary tree, return its bottom view.
*/
public class Solution{
	public List<Integer> bottomView(TreeNode root){
		List<Integer> res = new ArrayList<>();
		if(root == null)
			return res;
		Map<Integer, Integer> horizontalDistances = new HashMap<>();
		preorder(root, 0, horizontalDistances);
		Set<Integer> keys = Collections.sort(horizontalDistances.keySet());
		for(int i : keys){
			res.add(horizontalDistances.get(i));
		}

		return res;

	}
	private void preorder(TreeNode root, int distance, Map<Integer, Integer> horizontalDistances){
		if(root == null)
			return;
		preorder(root.left, distance - 1, horizontalDistances);
		horizontalDistances.put(distance, root.val);
		preorder(root.right, distance + 1, horizontalDistances)
	}
}