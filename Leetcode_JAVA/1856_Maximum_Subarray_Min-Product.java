class Solution {
    public int maxSumMinProduct(int[] nums) {
        long max = 0;
        Stack<Integer> stack = new Stack<>();
        long[] preSum = new long[nums.length + 1];
        for(int i = 0; i < nums.length; i++){
            preSum[i + 1] = preSum[i] + nums[i];
        }
        for(int i = 0; i <= nums.length; i++){
            while(!stack.isEmpty() && (i == nums.length || nums[i] < nums[stack.peek()])){
                int j = stack.pop();
                max = Math.max(max, (preSum[i] - preSum[stack.isEmpty() ? 0 : stack.peek() + 1]) * nums[j]);
        }
            stack.push(i);
    }
        return (int) (max % 1000000007);
    }
}

