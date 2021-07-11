/*
Medium
*/

class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        int maxLen = 0;
        int len = nums.length;
        //int[] preSum = new int[len + 1];
        int sum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < len; i++){
            sum += nums[i];
            if(sum == k)
                maxLen = Math.max(maxLen, i + 1);
            else if(map.containsKey(sum - k))
                maxLen = Math.max(maxLen, i - map.get(sum - k));
            //preSum[i + 1] = preSum[i] + nums[i];
            if(!map.containsKey(sum))
                map.put(sum, i);
                
        }
        return maxLen;
    }
}