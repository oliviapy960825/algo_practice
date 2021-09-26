class Solution {
    int[] preSum;
    final int INF = Integer.MAX_VALUE;
    int[][] memo;
    public int findDiff(int start, int end, boolean alice){
        if(start == end)
            return 0;
        if(memo[start][end] != INF)
            return memo[start][end];
        int diff;
        int first = preSum[end + 1] - preSum[start + 1];
        int last = preSum[end] - preSum[start];
        if(alice)
            diff = Math.max(findDiff(start + 1, end, !alice) + first, findDiff(start, end - 1, !alice) + last);
        else
            diff = Math.min(findDiff(start + 1, end, !alice) - first, findDiff(start, end - 1, !alice) - last);
        memo[start][end] = diff;
        return diff;
    }
    public int stoneGameVII(int[] stones) {
        int n = stones.length;
        memo = new int[n][n];
        for(int[] arr : memo)
            Arrays.fill(arr, INF);
        preSum = new int[n + 1];
        for(int i = 0; i < n; i++){
            preSum[i + 1] = preSum[i] + stones[i];
        }
        return Math.abs(findDiff(0, n - 1, true));
    }
}