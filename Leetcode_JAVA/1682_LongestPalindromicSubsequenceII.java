/*
Medium
*/

class Solution {
    public int helper(String s, int i, int j, int prev, int[][][] memo){
        if(i >= j)
            return 0;
        if(memo[i][j][prev] != -1)
            return memo[i][j][prev];
        if(s.charAt(i) - 'a' == prev)
            return helper(s, i + 1, j, prev, memo);
        if(s.charAt(j) - 'a' == prev)
            return helper(s, i, j - 1, prev, memo);
        if(s.charAt(i) == s.charAt(j))
            return memo[i][j][prev] = helper(s, i + 1, j - 1, s.charAt(i) - 'a', memo) + 2;
        else{
            return memo[i][j][prev] = Math.max(helper(s, i + 1, j, prev, memo), helper(s, i, j - 1, prev, memo));
        }
    }
    public int longestPalindromeSubseq(String s) {
        int len = s.length();
        int[][][] memo = new int[len][len][27];
          for (int r = 0; r < len; r++) {
            for (int c = 0; c < len; c++) {
                Arrays.fill(memo[r][c], -1);
            }
        }
        return helper(s, 0, s.length() - 1, 26, memo);
    }
}
