class Solution {
    public int find(int[] f, int i){
        while(f[i] != i){
            f[i] = f[f[i]];
            i = f[i];
        }
        return i;
    }
    public boolean contains(Set<String> a, Set<String> b){
        if(a.size() <= b.size())
            return false;
        return a.containsAll(b);
    }
    public List<Integer> peopleIndexes(List<List<String>> c) {
        List<Integer> res = new LinkedList<>();
        List<Set<String>> list = new LinkedList<>();
        for(List<String> lst : c)
            list.add(new HashSet<>(lst));
        int length = list.size();
        int[] f = new int[length];
        for(int i = 0; i < length; i++)
            f[i] = i;
        for(int i = 0; i < length; i++){
            for(int j = i + 1; j < length; j++){
                int a = find(f, i), b = find(f, j);
                if(a == b) continue;
                if(contains(list.get(a), list.get(b)))
                    f[b] = a;
                else if(contains(list.get(b), list.get(a)))
                    f[a] = b;
            }
        }
        
        Set<Integer> r = new HashSet<>();
        for(int i : f)
            r.add(find(f, i));
        res.addAll(r);
        Collections.sort(res);
        return res;
        
    }
}