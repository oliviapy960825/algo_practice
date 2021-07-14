/*
Medium
*/


class Solution {
    public boolean dfs(int[] nums, boolean[] visited, int start, int k, int goal, int sum){
        if(k == 1)
            return true;
        if(sum == goal)
            return dfs(nums, visited, 0, k - 1, goal, 0);
        for(int i = start; i < nums.length; i++){
            if(visited[i])
                continue;
            visited[i] = true;
            if(dfs(nums, visited, i + 1, k, goal, sum + nums[i]))
                return true;
            visited[i] = false;
        }
        
        return false;
    }
    
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = 0;
        for(int n : nums)
            sum += n;
        if(sum % k != 0)
            return false;
        int goal = sum / k;
        
        return dfs(nums, new boolean[nums.length], 0, k, goal, 0);
    }
}