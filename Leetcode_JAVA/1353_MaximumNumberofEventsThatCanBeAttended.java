/*
Medium

*/

class Solution {
    public int maxEvents(int[][] events) {
        int res = 0;
        PriorityQueue<Integer> pq = new PriorityQueue();
        Arrays.sort(events, (a, b) -> a[0] - b[0]);
        int i = 0, n = events.length;
        for(int j = 1; j <= 100000; j++){
            while(!pq.isEmpty() && pq.peek() < j)
                pq.poll();
            while(i < n && events[i][0] == j)
                pq.offer(events[i++][1]);
            if (!pq.isEmpty()) {
                pq.poll();
                ++res;
            }
        }
        
        return res;
    }
}