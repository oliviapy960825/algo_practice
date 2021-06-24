/*
Medium
*/

class Solution {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        Arrays.sort(slots1, (a, b) -> a[0] - b[0]);
        Arrays.sort(slots2,  (a, b) -> a[0] - b[0]);
        
        int len1 = slots1.length, len2 = slots2.length;
        int p1 = 0, p2 = 0;
        List<Integer> res = new ArrayList<>();
        while(p1 < len1 && p2 < len2){
            int[] s1 = slots1[p1];
            int[] s2 = slots2[p2];
            int min = Math.max(s1[0], s2[0]);
            int max = Math.min(s1[1], s2[1]);
            if(min < max && max - min >= duration){
                res.add(min);
                res.add(min + duration);
                return res;
            }
            if(s1[1] < s2[1])
                p1++;
            else
                p2++;
        }
        
        return res;
    }
}