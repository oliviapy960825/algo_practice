/* Lintcode 363. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Trapping Rain Water

Have you met this question in a real interview?  
Example
Example 1:

Input: [0,1,0]
Output: 0
Example 2:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Challenge
O(n) time and O(1) memory

O(n) time and O(n) memory is also acceptable.
*/

public class Solution {
    /**
     * @param heights: a list of integers
     * @return: a integer
     */
    public int trapRainWater(int[] heights) {
        // write your code here
        if (heights.length==0){
            return 0;
        }
        int[] maxHeights=new int[heights.length+1];
        maxHeights[0]=0;
        for(int i=0;i<heights.length;i++){
            maxHeights[i+1]=Math.max(maxHeights[i],heights[i]);
        }
        int max=0;
        int area=0;
        
        for(int i=heights.length-1;i>=0;i--){
            area+=Math.min(max,maxHeights[i])>heights[i] ? Math.min(max,maxHeights[i])-heights[i]: 0;
            max=Math.max(max,heights[i]);
        }
        
        return area;
}
}
//version 2 
public class Solution {
    /**
     * @param heights: a list of integers
     * @return: a integer
     */
    public int trapRainWater(int[] heights) {
        
        if(heights.length==0){
            return 0;
        }
        // write your code here
        int l=0;
        int r=heights.length-1;
        int left=heights[l];
        int right=heights[r];
        int sum=0;
        while (l<r){
            if(left<right){
                l++;
                if (left>heights[l]){
                    sum+=left-heights[l];
                }
                else{
                    left=heights[l];
                }
            }
            else{
                r--;
                if(right>heights[r]){
                    sum+=right-heights[r];
                }
                else{
                    right=heights[r];
                }
            }
        }
        return sum;
    }
}