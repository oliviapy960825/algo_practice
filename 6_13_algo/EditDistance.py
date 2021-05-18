"""
119. Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Have you met this question in a real interview?  
Example
Example 1:

Input: 
"horse"
"ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: 
"intention"
"execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        dp=[[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        
        for i in range(1, len(word1)+1):
            dp[0][i]=i
        for i in range(1, len(word2)+1):
            dp[i][0]=i
        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word2[i-1]==word1[j-1]:
                    dp[i][j]=min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
                else:
                    dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                    
        return dp[-1][-1]
                