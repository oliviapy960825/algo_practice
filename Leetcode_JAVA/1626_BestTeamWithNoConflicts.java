class Solution {
    public int bestTeamScore(int[] scores, int[] ages) {
        int len = scores.length;
        int[][] mem = new int[len][2];
        for(int i = 0; i < len; i++){
            mem[i][1] = scores[i];
            mem[i][0] = ages[i];
        }
        
        Arrays.sort(mem, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        int res = 0;
        int[] dp = new int[len];
        dp[0] = mem[0][1];
        for(int i = 0; i < len; i++){
            int max = mem[i][1];
            for(int j = 0; j < i; j++){
                if(mem[i][1] >= mem[j][1]){
                    max = Math.max(max, dp[j] + mem[i][1]);
                }
            }
            dp[i] = max;
            res = Math.max(res, max);
        }
        return res;
    }
}