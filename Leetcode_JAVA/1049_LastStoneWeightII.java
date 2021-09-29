class Solution {
    public int lastStoneWeightII(int[] stones) {
        int len = stones.length;
        int sum = 0;
        int max = 0;
        for(int i : stones) sum += i;
        boolean[][] dp = new boolean[sum + 1][len + 1];
        for(int i = 0; i <= len; i++){
            dp[0][i] = true;
        }
        for(int i = 1; i <= len; i++){
            for(int j = 1; j <= sum / 2; j++){
                if(dp[j][i - 1] || (j >= stones[i - 1] && dp[j - stones[i - 1]][i - 1])){
                    dp[j][i] = true;
                    max = Math.max(max, j);
                }
            }
        }
        
        return sum - max * 2;
    }
}