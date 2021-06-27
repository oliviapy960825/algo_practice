/*
Hard
*/

class Solution {
    public int maxSum(int[] nums1, int[] nums2) {
        int len1 = nums1.length, len2 = nums2.length;
        long mod = (long) 1e9 + 7;
        long sum1 = 0, sum2 = 0;
        int i = 0, j = 0;
        while(i < len1 || j < len2){
            if(i < len1 && (j == len2 || nums1[i] < nums2[j])){
                sum1 += nums1[i];
                i++;
            }
            else if(j < len2 && (i == len1 || nums1[i] > nums2[j])){
                sum2 += nums2[j];
                j++;
            }
            else{
                sum1 = sum2 = Math.max(sum1, sum2) + nums1[i];
                i++;
                j++;
            }
        }
        
        return (int) (Math.max(sum1, sum2) % mod);
    }
}