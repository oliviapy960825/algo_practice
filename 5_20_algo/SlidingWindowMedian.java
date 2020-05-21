/*
Lintcode 360. Sliding Window Median

Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the median of the element inside the window at each moving. (If there are even numbers in the array, return the N/2-th number after sorting the element in the window. )
Example
Example 1:

Input:
[1,2,7,8,5]
3
Output:
[2,7,7]

Explanation:
At first the window is at the start of the array like this `[ | 1,2,7 | ,8,5]` , return the median `2`;
then the window move one step forward.`[1, | 2,7,8 | ,5]`, return the median `7`;
then the window move one step forward again.`[1,2, | 7,8,5 | ]`, return the median `7`;
Example 2:

Input:
[1,2,3,4,5,6,7]
4
Output:
[2,3,4,5]

Explanation:
At first the window is at the start of the array like this `[ | 1,2,3,4, | 5,6,7]` , return the median `2`;
then the window move one step forward.`[1,| 2,3,4,5 | 6,7]`, return the median `3`;
then the window move one step forward again.`[1,2, | 3,4,5,6 | 7 ]`, return the median `4`;
then the window move one step forward again.`[1,2,3,| 4,5,6,7 ]`, return the median `5`;
Challenge
O(nlog(n)) time
*/

public class Solution {
    /**
     * @param nums: A list of integers
     * @param k: An integer
     * @return: The median of the element inside the window at each moving
     */
    PriorityQueue<Integer> maxHeap, minHeap;
    public List<Integer> medianSlidingWindow(int[] A, int k) {
        // write your code here
        List<Integer> res = new ArrayList<Integer>();
        int n = A.length;
        if (n == 0) {
            return res;
        }
        
        maxHeap = new PriorityQueue<Integer>(n, Collections.reverseOrder());
        minHeap = new PriorityQueue<Integer>(n);
        
        int i;
        for (i = 0; i < n; ++i) {
            if (maxHeap.size() == 0 || A[i] <= maxHeap.peek()) {
                maxHeap.offer(A[i]);
            }
            else {
                minHeap.offer(A[i]);
            }
            
            balance();
            if (i - k >= 0) {
                if (A[i - k] > maxHeap.peek()) {
                    minHeap.remove(A[i - k]);
                }
                else {
                    maxHeap.remove(A[i - k]);
                }
            }
            
            balance();
            
            if (i >= k - 1) {
                res.add(maxHeap.peek());
            }
        }
        
        return res;
    }
    
    private void balance() {
        while (maxHeap.size() < minHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
        
        while (minHeap.size() < maxHeap.size() - 1) {
            minHeap.offer(maxHeap.poll());
        }
    }
}