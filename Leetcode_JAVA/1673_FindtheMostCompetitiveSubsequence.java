/*
Medium
*/

class Solution {
    public int[] mostCompetitive(int[] nums, int k) {
        int[] res = new int[k];
        Deque<Integer> stack = new ArrayDeque<>();
        int count = nums.length - k;
        for(int i = 0; i < nums.length; i++){
            while(!stack.isEmpty() && nums[i] < stack.peekLast() && count > 0){
                stack.pollLast();
                count--;
            }
            stack.addLast(nums[i]);
        }
        for(int i = 0; i < k; i++){
            res[i] = stack.pollFirst();
        }
        return res;
    }
}