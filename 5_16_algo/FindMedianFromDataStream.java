/* 81. Find Median from Data Stream
Numbers keep coming, return the median of numbers at every time a new number added.

Have you met this question in a real interview?  
Clarification
What's the definition of Median?

The median is not equal to median in math.
Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]A[(n−1)/2].
For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.
Example
Example 1

Input: [1,2,3,4,5]
Output: [1,1,2,2,3]
Explanation:
The medium of [1] and [1,2] is 1.
The medium of [1,2,3] and [1,2,3,4] is 2.
The medium of [1,2,3,4,5] is 3.
Example 2

Input: [4,5,1,3,2,6,0]
Output: [4,4,4,3,3,3,3]
Explanation:
The medium of [4], [4,5], [4,5,1] is 4.
The medium of [4,5,1,3], [4,5,1,3,2], [4,5,1,3,2,6] and [4,5,1,3,2,6,0] is 3.
Challenge
Total run time in O(nlogn).
*/

public class Solution {
    /**
     * @param nums: A list of integers
     * @return: the median of numbers
     */
    private PriorityQueue<Integer> minHeap, maxHeap;
    private int numOfEle=0;
    public int[] medianII(int[] nums) {
        // write your code here
        Comparator<Integer> comp=new Comparator<Integer>(){
            @Override
            public int compare(Integer left, Integer right){
                return right.compareTo(left);
            }
        };
        int cnt=nums.length;
        maxHeap=new PriorityQueue<Integer>(cnt,comp);
        minHeap=new PriorityQueue<Integer>(cnt);
        int[] ans=new int[cnt];
        for(int i=0;i<cnt;i++){
            addNumber(nums[i]);
            ans[i]=getMedian();
        }
       return ans;
    }
    
    void addNumber(int value){
        maxHeap.add(value);
        if(numOfEle%2==0){
            if (minHeap.isEmpty()){
                numOfEle++;
                return;
            }
            else if(maxHeap.peek()>minHeap.peek()){
                Integer maxRoot=maxHeap.poll();
                Integer minRoot=minHeap.poll();
                maxHeap.add(minRoot);
                minHeap.add(maxRoot);
            }
        }
        else{
            minHeap.add(maxHeap.poll());
        }
        numOfEle++;
    }
    
    int getMedian(){
        return maxHeap.peek();
    }
}