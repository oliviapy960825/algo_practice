class Solution {
    public int min(int[][] mat, Integer[][] dp, int index, int val, int target){
        if(index == mat.length)
            return Math.abs(val - target);
        if(dp[index][val] != null) return dp[index][val];
        int res = Integer.MAX_VALUE;
        for(int i = 0; i < mat[0].length; i++){
            res = Math.min(res, min(mat, dp, index + 1, val + mat[index][i], target));
        }
        dp[index][val] = res;
        return res;
    }
    public int minimizeTheDifference(int[][] mat, int target) {
        int m = mat.length, n = mat[0].length;
        Integer[][] dp = new Integer[m][5001];
        return min(mat, dp, 0, 0, target);
    }
}