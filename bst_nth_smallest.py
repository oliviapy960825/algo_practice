class BST:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        if not self.left and not self.right: # leaf node
            return str(self.data)
        else:
            left_str = str(self.left) if self.left else "_"
            right_str = str(self.right) if self.right else "_"
            return "(" + left_str + " " + str(self.data) + " " + right_str + ")"

    # Returns the nth smallest element of the binary search tree,
    # where n=0 returns the smallest, n=1 returns the second smallest, etc
    # Returns None if there are not n elements in the tree
    def count(self):
      #return the count of the nodes
      root=self
      if not root:
        return 0

      if self.left and self.right:
        return self.left.count()+self.right.count()+1
      if self.left and not self.right:
        return self.left.count()
      if self.right and not self.left:
        return self.right.count()
      if not self.left and not self.right:
        return 1

    def nth_smallest(self, n):
        #****************
        # YOUR CODE HERE
        #****************

        #root=self
        if n>self.count()+1:
          return None
        if not self.left:
          if n==0:
            return self.data
          if self.right:
            return self.right.nth_smallest(n-1)
          else:
            return None
        if self.left and self.left.count()>n:
          return self.left.nth_smallest(n)
        if self.left and self.left.count()==n:
          return self.data
        if self.left and self.left.count()<n:
          return self.right.nth_smallest(n-self.left.count()-1)



test_bst = BST(8,
               BST(3,
                   BST(1),
                   BST(6,
                       BST(4),
                       BST(7))),
               BST(10,
                   None,
                   BST(14,
                       BST(13),
                       None)));

print ("test_bst = " + str(test_bst))
# test_bst = ((1 3 (4 6 7)) 8 (_ 10 (13 14 _)))

for n in range(0, 10):
    print (str(n) + "th smallest: " + str(test_bst.nth_smallest(n)))

# 0th smallest: 1
# 1th smallest: 3
# 2th smallest: 4
# 3th smallest: 6
# ...
# 8th smallest: 14
# 9th smallest: None
