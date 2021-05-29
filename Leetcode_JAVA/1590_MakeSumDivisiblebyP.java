/*
Medium

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

 

Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.

Example 4:

Input: nums = [1,2,3], p = 7
Output: -1
Explanation: There is no way to remove a subarray in order to get a sum divisible by 7.

Example 5:

Input: nums = [1000000000,1000000000,1000000000], p = 3
Output: 0

 

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= p <= 109


*/


class Solution {
    public int minSubarray(int[] nums, int p) {
        int len = nums.length;
        long[] preSum = new long[len];
        preSum[0] = (long) nums[0];
        for(int i = 1; i < len; i++)
            preSum[i] = preSum[i - 1] + nums[i];
        
        System.out.println(preSum[len - 1]);
        if(preSum[len - 1] < p)
            return -1;
        long rmv = preSum[len - 1] % p;
        if(rmv == 0)
            return 0;
        Map<Long, Integer> lastSeen = new HashMap<>();
        lastSeen.put(new Long(0), -1);
        int min = len;
        for(int i = 0; i < len; i++){
            long rem = preSum[i] % p;
            long target = (rem + p - rmv) % p;
            if(lastSeen.containsKey(target))
                min = Math.min(min, i - lastSeen.get(target));
            lastSeen.put(rem, i);
        }
        
        return min < len ? min : -1;
    }
}