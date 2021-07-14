/*
Medium
*/
class Solution {
    public void dfs(int[] nums, int i, List<Integer> list, List<List<Integer>> res){
        res.add(new ArrayList(list));
        if(i == nums.length)
            return;
        
        for(int j = i; j < nums.length; j++){
            if(j != i && nums[j] == nums[j - 1])
                continue;
            list.add(nums[j]);
            dfs(nums, j + 1, list, res);
            list.remove(list.size() - 1);
        }
        
    }
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList();
        Arrays.sort(nums);
        dfs(nums, 0, new ArrayList(), res);
        return res;
    }
}