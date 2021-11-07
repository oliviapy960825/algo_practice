class Solution {
    public int findPaths(int m, int n, int N, int x, int y) {
        int mod = (int)1e9+7;
        int[][] dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        int[][][] dp = new int[N+1][m][n];
        // dp[0][r][c] = 1;
        for(int s = 1; s<=N; s++){
            for(int i = 0; i<m; i++){
                for(int j = 0; j<n; j++){
                    for(int[] dir: dirs){
                        int r0 = i+dir[0];
                        int c0 = j+dir[1];
                        if(r0<0 || r0>=m || c0<0 || c0>=n){
                            dp[s][i][j] +=1;
                        }
                        else{
                            dp[s][i][j] = (dp[s][i][j]+dp[s-1][r0][c0])%mod;
                        }
                    }
                }
            }
        }
        return dp[N][x][y];
    }
}