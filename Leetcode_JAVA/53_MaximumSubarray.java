/*
Easy
*/

class Solution {
    public int maxSubArray(int[] nums) {
        if(nums.length == 1)
            return nums[0];
        int len = nums.length;
        int[] dp = new int[len];
        dp[0] = nums[0];
        for(int i = 1; i < len; i++){
            dp[i] = Math.max(dp[i - 1], 0) + nums[i];
        }
        int maxSum = Integer.MIN_VALUE;
        for(int i = 0; i < len; i++){
            maxSum = Math.max(maxSum, dp[i]);
        }
        return maxSum;
    }
}