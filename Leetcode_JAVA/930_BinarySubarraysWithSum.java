/*
Medium

In an array nums of 0s and 1s, how many non-empty subarrays have sum goal?

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

 

Note:

    nums.length <= 30000
    0 <= goal <= nums.length
    nums[i] is either 0 or 1.


*/


class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        int len = nums.length;
        int[] preSum = new int[len];
        preSum[0] = nums[0];
        for(int i = 1; i < len; i++){
            preSum[i] = preSum[i - 1] + nums[i];
        }
        
        int count = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for(int c : preSum){
            count += map.getOrDefault(c, 0);
            map.put(c + goal, map.getOrDefault(c + goal, 0) + 1);
        }
        return count;
    }
}