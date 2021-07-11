/*
Medium
*/

class Solution {
    int[] preSum;
    int sum;
    public Solution(int[] w) {
        int len = w.length;
        this.sum = 0;
        this.preSum = new int[len];
        this.preSum[0] = w[0];
        this.sum += w[0];
        for(int i = 1; i < len; i++){
            preSum[i] = preSum[i - 1] + w[i];
            sum += w[i];
        }
    }
    
    public int pickIndex() {
        Random rand = new Random();
        int ind = rand.nextInt(this.sum);
        int left = 0;
        int right = this.preSum.length - 1;
        while(left + 1 < right){
            int mid = left + (right - left) / 2;
            if(ind >= this.preSum[mid])
                left = mid;
            else
                right = mid;
        }
        
        if(ind < this.preSum[left])
            return left;
        else
            return right;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */