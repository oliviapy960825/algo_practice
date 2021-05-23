/*
Hard

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("
Output: [""]

 

Constraints:

    1 <= s.length <= 25
    s consists of lowercase English letters and parentheses '(' and ')'.
    There will be at most 20 parentheses in s.


*/

class Solution {
    public void dfs(String s, int i, int left, int right, int open, StringBuilder sb, Set<String> res){
        if(left < 0 || right < 0 || open < 0)
            return ;
        if(i == s.length()){
            if(left == 0 && right == 0 && open == 0)
                res.add(sb.toString());
            return;
        }
        
        int len = sb.length();
        if(s.charAt(i) == '('){
            dfs(s, i + 1, left - 1, right, open, sb, res);
            dfs(s, i + 1, left, right, open + 1, sb.append('('), res);
        }
        else if(s.charAt(i) == ')'){
            dfs(s, i + 1, left, right - 1, open, sb, res);
            dfs(s, i + 1, left, right, open - 1, sb.append(')'), res);
        }
        else{
            dfs(s, i + 1, left, right, open, sb.append(s.charAt(i)), res);
        }
        
        sb.setLength(len);
    }
    public List<String> removeInvalidParentheses(String s) {
        Set<String> res = new HashSet<>();
        int left = 0, right = 0;
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == '(')
                left++;
            else if(c == ')'){
                if(left != 0)
                    left--;
                else
                    right++;
            }
        }
        
        dfs(s, 0, left, right, 0, new StringBuilder(), res);
        
        return new ArrayList<>(res);
    }
}