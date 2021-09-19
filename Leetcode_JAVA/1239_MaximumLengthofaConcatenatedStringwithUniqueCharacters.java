class Solution {
    public int maxLength(List<String> arr) {
        return dfs(arr, 0, "");
    }
    
    private int dfs(List<String> arr, int pos, String res){
        Set<Character> resSet = new HashSet<>();
        for(char c : res.toCharArray())
            resSet.add(c);
        if(res.length() != resSet.size())
            return 0;
        int best = res.length();
        for(int i = pos; i < arr.size(); i++)
            best = Math.max(best, dfs(arr, i + 1, res + arr.get(i)));
        return best;
    }
}