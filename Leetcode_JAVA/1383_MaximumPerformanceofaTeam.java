/*
Hard
*/
class Solution {
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        int modulo = (int) Math.pow(10, 9) + 7;
        List<Pair<Integer, Integer>> cands = new ArrayList<>();
        for(int i = 0; i < n; i++){
            cands.add(new Pair(efficiency[i], speed[i]));
        }
        
        Collections.sort(cands, Comparator.comparing(o -> -o.getKey()));
        
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> o1 - o2);
        
        long sum = 0, perf = 0;
        
        for(Pair<Integer, Integer> p : cands){
            Integer eff = p.getKey();
            Integer sp = p.getValue();
            if(pq.size() > k - 1){
                sum -= pq.remove();
            }
            pq.add(sp);
            sum += sp;
            perf = Math.max(perf, sum * eff);
        }
        
        return (int) (perf % modulo);
    }
}