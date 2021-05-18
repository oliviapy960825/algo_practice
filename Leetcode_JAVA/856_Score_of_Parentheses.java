/*
Medium

Given a balanced parentheses string s, compute the score of the string based on the following rule:

    () has score 1
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.

 

Example 1:

Input: s = "()"
Output: 1

Example 2:

Input: s = "(())"
Output: 2

Example 3:

Input: s = "()()"
Output: 2

Example 4:

Input: s = "(()(()))"
Output: 6

 

Note:

    s is a balanced parentheses string, containing only ( and ).
    2 <= s.length <= 50



*/

class Solution {
    public int scoreOfParentheses(String s) {
        if(s == null || s.length() == 0)
            return 0;
        int sum = 0;
        //char op = '';
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < s.length(); i++){
            if(stack.isEmpty() || s.charAt(i) == '('){
                stack.push(s.charAt(i));
                continue;
            }
            else{//s.charAt(i) == ')'
                if(stack.peek() == '('){
                    stack.pop();
                    stack.push('1');
                }
                else{//stack.peek() is digit
                    int res = 0;
                    while(stack.peek() != '('){
                        res += (int) (stack.pop() - '0');
                        //System.out.println(res);
                    }
                    stack.pop();
                    res *= 2;
                    stack.push((char) (res + '0'));
                }
            }
        }
        
        while(!stack.isEmpty()){
            sum += stack.pop() - '0';
        }
        
        return sum;
    }
}