/*
Easy
*/

class Solution {
    public int missingNumber(int[] nums) {
        if(nums == null || nums.length == 0)
          return 0;
        for(int i = 0; i < nums.length; i++){
          if(nums[i] == i)
            continue;
          while(nums[i] < nums.length && nums[i] != nums[nums[i]]){
            int n1 = nums[i];
            nums[i] = nums[nums[i]];
            nums[n1] = n1;
          }
        }
        for(int i = 0; i < nums.length; i++){
          if(nums[i] != i)
            return i;
        }

        return nums.length;
    }
}