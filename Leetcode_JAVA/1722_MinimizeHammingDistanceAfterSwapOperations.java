/*
Medium
*/
class Solution {
    public int minimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        int len = source.length;
        int[] union = new int[len];
        for(int i = 0; i < len; i++)
            union[i] = i;
        for(int[] pair : allowedSwaps){
            int a = pair[0], b = pair[1];
            int parentA = find(union, a), parentB = find(union, b);
		    if (parentA != parentB) 
                union[parentA] = parentB;
        }
        
        Map<Integer, Map<Integer, Integer>> map = new HashMap<>();
        for(int i = 0; i < len; i++){
            int num = source[i];
            int root = find(union, i);
            
            map.putIfAbsent(root, new HashMap<>());
            Map<Integer, Integer> store = map.get(root);
            store.put(num, store.getOrDefault(num, 0) + 1);
        }
        
        int res = 0;
        for (int i = 0; i < len; ++i) {
            int num = target[i];
            int root = find(union, i);

            Map<Integer, Integer> store = map.get(root);

            if (store.getOrDefault(num, 0) == 0) res++;
            else store.put(num, store.get(num) - 1);
        }

        return res;
        
        
    }
    public int find(int[] union, int i){
        if(union[i] == i)
            return i;
        return union[i] = find(union, union[i]);
    }
}