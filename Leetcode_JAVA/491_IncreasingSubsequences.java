/*
Medium
*/

class Solution {
    public void dfs(int[] nums, int index, Set<List<Integer>> res, List<Integer> curr){
        if(curr.size() >= 2)
            res.add(new ArrayList(curr));
        for(int i = index; i < nums.length; i++){
            if(curr.size() == 0 || curr.get(curr.size() - 1) <= nums[i]){
                curr.add(nums[i]);
                dfs(nums, i + 1, res, curr);
                curr.remove(curr.size() - 1);
            }
        }
    }
    public List<List<Integer>> findSubsequences(int[] nums) {
        Set<List<Integer>> res = new HashSet<>();
        List<Integer> curr = new ArrayList<>();
        dfs(nums, 0, res, curr);
        return new ArrayList(res);
    }
}