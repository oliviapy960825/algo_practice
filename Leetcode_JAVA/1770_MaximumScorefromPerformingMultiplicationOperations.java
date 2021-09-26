class Solution {
    Integer[][] memo;
    int[] nums, multipliers;
    int m, n;
    public int dp(int l, int i){
        if(i == m)
            return 0;
        if(memo[l][i] != null)
            return memo[l][i];
        int left = dp(l + 1, i + 1) + multipliers[i] * nums[l];
        int right = dp(l, i + 1) + multipliers[i] * nums[n - (i - l) - 1];
        memo[l][i] = Math.max(left, right);
        return memo[l][i];
        
    }
    public int maximumScore(int[] nums, int[] multipliers) {
        this.m = multipliers.length;
        this.n = nums.length;
        this.nums = nums;
        this.multipliers = multipliers;
        this.memo = new Integer[m][m];
        
        return dp(0, 0);
    }
}