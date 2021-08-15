/*
Medium
*/

class Solution {
    public int longestBeautifulSubstring(String word) {
        int max = 0;
        Set<Character> seen = new HashSet<>();
        for(int low = -1, high = 0; high < word.length(); high++){
            if(high > 0 && word.charAt(high - 1) > word.charAt(high)){
                seen = new HashSet();
                low = high - 1;
            }
            
            seen.add(word.charAt(high));
            if(seen.size() == 5)
                max = Math.max(max, high - low);
        }
        return max;
    }
}