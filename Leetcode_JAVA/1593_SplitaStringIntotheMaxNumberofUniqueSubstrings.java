/*
Medium
*/

class Solution {
    public int dfs(String s, int index, Set<String> seen){
        if(index == s.length())
            return 0;
        int res = -1;
        for(int i = index + 1; i <= s.length(); i++){
            String sub = s.substring(index, i);
            if(seen.contains(sub))
                continue;
            seen.add(sub);
            int next = dfs(s, i, seen);
            if(next >= 0)
                res = Math.max(res, next + 1);
            seen.remove(sub);
        }
        
        return res;
    }
    public int maxUniqueSplit(String s) {
        //int max = 0;
        Set<String> seen = new HashSet<String>();
        return dfs(s, 0, seen);
        //return max;
    }
}