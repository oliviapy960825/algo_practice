/*
Medium
*/

class Solution {
    public boolean dfs(int n, int curr, int[] res, boolean[] visited){
        if(curr == res.length)
            return true;
        if(res[curr] != 0)
            return dfs(n, curr + 1, res, visited);
        else{
            for(int i = n; i >= 1; i--){
                if(visited[i])
                    continue;
                visited[i] = true;
                res[curr] = i;
                if(i == 1){
                    if(dfs(n, curr + 1, res, visited))
                        return true;
                }
                else if(curr + i < res.length && res[curr + i] == 0){
                    res[curr + i] = i;
                    if(dfs(n, curr + 1, res, visited))
                        return true;
                    res[curr + i] = 0;
                }
                visited[i] = false;
                res[curr] = 0;
            }
        }
        
        return false;
    }
    
            
    
    public int[] constructDistancedSequence(int n) {
        int[] res = new int[n * 2 - 1];
        boolean[] visited = new boolean[n + 1];
        dfs(n, 0, res, visited);
        return res;
    }
}