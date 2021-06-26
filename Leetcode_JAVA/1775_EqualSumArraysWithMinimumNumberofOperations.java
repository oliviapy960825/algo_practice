/*
Medium
*/

class Solution {
    public int minOperations(int[] nums1, int[] nums2) {
        if(nums1.length * 6 < nums2.length || nums1.length > nums2.length * 6)
            return -1;
        int sum1 = IntStream.of(nums1).sum();
        int sum2 = IntStream.of(nums2).sum();
        
        if(sum1 > sum2)
            return minOperations(nums2, nums1);
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int ops = 0, p1 = 0, p2 = nums2.length - 1;
        while(sum2 > sum1){
            if(p2 < 0 || p1 < nums1.length && 6 - nums1[p1] > nums2[p2] - 1){
                sum1 += 6 - nums1[p1];
                p1++;
            }
            else{
                sum2 -= nums2[p2] - 1;
                p2--;
            }
            ops++;
        }
        
        return ops;
        
    }
}