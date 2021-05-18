"""
92. Backpack
Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

You can not divide any item into small pieces.

Have you met this question in a real interview?  
Example
Example 1:
	Input:  [3,4,8,5], backpack size=10
	Output:  9

Example 2:
	Input:  [2,3,5,7], backpack size=12
	Output:  12
	
Challenge
O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.
"""

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        if m<=0 or not A or len(A)==0:
            return 0
        dp=[0]*(m+1)
        dp[0]=1
        
        ans=0
        
        for i in A:
            for j in range(m, -1, -1):
                if j-i>=0 and dp[j-i]>0:
                    ans=max(ans, j)
                    dp[j]=1
        return ans
        