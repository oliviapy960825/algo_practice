/*
Medium
*/

class Solution {
    public int mctFromLeafValues(int[] arr) {
        int sum = 0;
        int currMax = 0;
        int len = arr.length;
        //Arrays.sort(arr);
        Stack<Integer> stack = new Stack<>();
        stack.add(Integer.MAX_VALUE);
        for(int a : arr){
            while(stack.peek() < a){
                int mid = stack.pop();
                sum += mid * Math.min(stack.peek(), a);
            }
            stack.push(a);
        }
        while(stack.size() > 2){
            sum += stack.pop() * stack.peek();
        }
        return sum;
    }
}