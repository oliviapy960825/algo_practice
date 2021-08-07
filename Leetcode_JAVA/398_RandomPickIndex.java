/*
Medium
*/

class Solution {
    public Map<Integer, List<Integer>> map = new HashMap();
    public Random rand;
    public Solution(int[] nums) {
        this.rand = new Random();
        for(int i = 0; i < nums.length; i++){
            if(!map.containsKey(nums[i]))
                map.put(nums[i], new ArrayList());
            map.get(nums[i]).add(i);
        }
    }
    
    public int pick(int target) {
        int size = map.get(target).size();
        int ind = map.get(target).get(rand.nextInt(size));
        return ind;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */