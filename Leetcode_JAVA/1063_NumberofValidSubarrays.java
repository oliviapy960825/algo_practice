/*
Hard
*/

class Solution {
    public int validSubarrays(int[] nums) {
        if(nums.length == 1)
            return 1;
        Stack<Integer> stack = new Stack<>();
        int res = 0;
        for(int num : nums){
            while(!stack.isEmpty() && stack.peek() > num)
                stack.pop();
            stack.push(num);
            res += stack.size();
        }
        
        return res;
    }
}