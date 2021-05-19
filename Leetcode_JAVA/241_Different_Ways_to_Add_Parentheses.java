/*
Medium

Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

 

Constraints:

    1 <= expression.length <= 20
    expression consists of digits and the operator '+', '-', and '*'.


*/


class Solution {
    public List<Integer> diffWaysToCompute(String expression) {
        List<Integer> ans = new ArrayList<>();
        //int res = 0;
        int len = expression.length();
        for(int i = 0; i < len; i++){
            char c = expression.charAt(i);
            if(c == '+' || c == '-' || c == '*'){
                List<Integer> first = diffWaysToCompute(expression.substring(0, i));
                List<Integer> second = diffWaysToCompute(expression.substring(i + 1));
                for(int f : first){
                    for(int s : second){
                        int res = 0;
                        switch(c){
                            case '+' : res = f + s;
                                break;
                            case '-' : res = f - s;
                                break;
                            case '*' : res = f * s;
                                break;
                        }
                        ans.add(res);
                    }
                }
            }
        }
        if(ans.size() == 0)
            ans.add(Integer.valueOf(expression));
        return ans;
    }
}

