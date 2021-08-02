/*
Hard
*/

class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        boolean speedUp = true;
        for(int c : capital){
            if(w < c)
                speedUp = false;
        }
        if(speedUp){
            PriorityQueue<Integer> pq = new PriorityQueue<>();
            for(int p : profits){
                pq.add(p);
                if(pq.size() > k)
                    pq.poll();
            }
            for(int h : pq)
                w += h;
            return w;
        }
        
        int n = profits.length;
        PriorityQueue<int[]> projects = new PriorityQueue<>((x, y) -> (x[0] - y[0]));
        
        for(int i = 0; i < n; i++){
            projects.add(new int[]{capital[i], profits[i]});
        }
        
        PriorityQueue<Integer> avail = new PriorityQueue<>((x, y) -> (y - x));
        
        while(k > 0){
            while(!projects.isEmpty() && projects.peek()[0] <= w)
                avail.add(projects.poll()[1]);
            
            if(!avail.isEmpty())
                w += avail.poll();
            else break;
            --k;
        }
        
        return w;
    }
}