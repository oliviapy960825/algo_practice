class Solution {
    int[][] dp;
    public int dfs(int i, int j, int[] arr){
        if(i > j)
            return 0;
        if(dp[i][j] > 0)
            return dp[i][j];
        int res = dfs(i, j - 1, arr) + 1;
        if(j > 0 && arr[j] == arr[j - 1])
            res = Math.min(res, dfs(i, j - 2, arr) + 1);
        for(int k = i; k < j - 1; k++){
            if(arr[k] == arr[j])
                res = Math.min(res, dfs(i, k - 1, arr) + dfs(k + 1, j - 1, arr));
        }
        dp[i][j] = res;
        return res;
    }
    public int minimumMoves(int[] arr) {
        int len = arr.length;
        this.dp = new int[len][len];
        return dfs(0, len - 1, arr);
    }
}