/*
Medium
*/

class Solution {
    public long helper(long i, int[] n) {
        Map<Long, Long> m = new HashMap<>();
        long cnt = 0;
        for (long v : n) {
            if (i % v == 0)
                cnt += m.getOrDefault(i / v, 0l);
            m.put(v, m.getOrDefault(v, 0l) + 1);
        }
        return cnt;
    }  
    public int numTriplets(int[] nums1, int[] nums2) {
        long cnt = 0;
        for(long n : nums1)
            cnt += helper(n * n, nums2);
        for(long n : nums2)
            cnt += helper(n * n, nums1);
        
        return (int) cnt;
    }
}

