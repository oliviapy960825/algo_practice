class Solution {
    public int profitableSchemes(int g, int p, int[] group, int[] profit) {
        int MOD = 1_000_000_007;
        int N = group.length;
        int[][][] dp = new int[2][p + 1][g + 1];
        dp[0][0][0] = 1;
        
        for(int i = 0; i < N; i++){
            int p0 = profit[i];
            int g0 = group[i];
            
            int[][] cur = dp[i % 2];
            int[][] cur2 = dp[(i + 1) % 2];
            
            for(int jp = 0; jp <= p; jp++)
                for(int jg = 0; jg <= g; jg++)
                    cur2[jp][jg] = cur[jp][jg];
            
            for(int p1 = 0; p1 <= p; p1++){
                int p2 = Math.min(p1 + p0, p);
                for(int g1 = 0; g1 <= g - g0; g1++){
                    int g2 = g1 + g0;
                    cur2[p2][g2] += cur[p1][g1];
                    cur2[p2][g2] %= MOD;
                }
            }
        }
        
        int ans = 0;
        for(int x : dp[N % 2][p])
            ans = (ans + x) % MOD;
        
        return ans;
    }
}