/*
Medium
*/

class Solution {
    public int longestWPI(int[] hours) {
        if(hours.length == 1){
            if(hours[0] <= 8)
                return 0;
            else
                return 1;
        }
        int res = 0;
        int len = hours.length;
        Stack<Integer> stack = new Stack<>();
        int[] pre = new int[len + 1];
        for(int i = 0; i < len; i++){
            pre[i + 1] = pre[i] + (hours[i] > 8 ? 1 : -1);
        }
        
        for(int i = 0; i <= len; i++){
            if(stack.isEmpty() || pre[stack.peek()] > pre[i])
                stack.push(i);
        }
        
        for (int j = len; j >= 0; j--) {  // start from end
            while (!stack.isEmpty() && pre[stack.peek()] < pre[j]) {
                res = Math.max(res, j-stack.pop());
            }
        }
        return res;
    }
}

