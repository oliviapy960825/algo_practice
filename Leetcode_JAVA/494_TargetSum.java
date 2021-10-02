class Solution {
    public int count = 0;
    public void dfs(int[] nums, int sum, int index, int target){
        if(index == nums.length){
            if(sum == target) count++;
            return;
        } 
        
        dfs(nums, sum + nums[index], index + 1, target);
        dfs(nums, sum - nums[index], index + 1, target);
    }
    public int findTargetSumWays(int[] nums, int S) {
        dfs(nums, 0, 0, S);
        return count;
    }
}
