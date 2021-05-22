/*
Hard

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:

Input: s = ""
Output: 0

 

Constraints:

    0 <= s.length <= 3 * 104
    s[i] is '(', or ')'.


*/

//dynamic programming

class Solution {
    public int longestValidParentheses(String s) {
        if(s == null || s.length() <= 1)
            return 0;
        int len = s.length();
        int max = 0;
        int[] dp = new int[len];
        for(int i = 1; i < len; i++){
            if(s.charAt(i) == ')'){
                if(s.charAt(i - 1) == '(' )
                    dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
                else if(i - dp[i - 1] > 0 && s.charAt(i - dp[i - 1] - 1) == '('){
                    dp[i] = dp[i - 1] + (i - dp[i - 1] - 2 >= 0 ? dp[i - dp[i - 1] - 2] : 0) + 2;
                }
            }
            max = Math.max(max, dp[i]);
        }
        
        return max;
    }
}


//monotonic stack

class Solution {
    public int longestValidParentheses(String s) {
        if(s == null || s.length() <= 1)
            return 0;
        int len = s.length();
        Stack<Integer> stack = new Stack<>();
        int max = 0;
        stack.push(-1);
        for(int i = 0; i < len; i++){
            char c = s.charAt(i);
            if(c == '(')
                stack.push(i);
            else{//c == ')'
                stack.pop();
                if(stack.isEmpty())
                    stack.push(i);
                else
                    max = Math.max(max, i - stack.peek());
            }
        }
        
        return max;
    }
}