class Solution {
    public int tallestBillboard(int[] rods) {
        int len = rods.length;
        int[][] max = new int[len + 1][10001];
        boolean[][] dp = new boolean[len + 1][10001];
        dp[0][5000] = true;
        
        for(int i = 0; i < len; i++){
            for(int j = 0; j <= 10000; j++){
                if(j - rods[i] >= 0 && dp[i][j - rods[i]]){
                    dp[i + 1][j] = true;
                    max[i + 1][j] = Math.max(max[i + 1][j], max[i][j - rods[i]] + rods[i]);
                }
                if(j + rods[i] <= 10000 && dp[i][j + rods[i]]){
                    dp[i + 1][j] = true;
                    max[i + 1][j] = Math.max(max[i + 1][j], max[i][j + rods[i]]);
                }
                
                if(dp[i][j]){
                    dp[i + 1][j] = true;
                    max[i + 1][j] = Math.max(max[i + 1][j], max[i][j]);
                }
            }
        }
        return max[len][5000];
    }
}