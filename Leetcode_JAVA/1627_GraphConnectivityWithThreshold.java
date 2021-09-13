/*
Hard
*/

class UnionFind{
    int[] parent, size;
    public UnionFind(int n){
        this.parent = new int[n];
        this.size = new int[n];
        for(int i = 0; i < n; i++){
            this.parent[i] = i;
            this.size[i] = 1;
        }
    }
    public int find(int n){
        if(this.parent[n] == n)
            return n;
        return this.parent[n] = find(this.parent[n]);
    }
    public boolean union(int u, int v){
        int pu = find(u), pv = find(v);
        if (pu == pv) return false;
        if (size[pu] > size[pv]) { // Union by larger size
            size[pu] += size[pv];
            parent[pv] = pu;
        } else {
            size[pv] += size[pu];
            parent[pu] = pv;
        }
        return true;
    }
}

class Solution {
    public List<Boolean> areConnected(int n, int threshold, int[][] queries) {
        UnionFind uf = new UnionFind(n+1);
        for (int i = 1; i <= n; i++)
            for (int j = i * 2; j <= n; j += i)
                if (i > threshold)
                    uf.union(i, j);
        List<Boolean> ans = new ArrayList<>();
        for (int[] q : queries) {
            int pa = uf.find(q[0]);
            int pb = uf.find(q[1]);
            ans.add(pa == pb);
        }
        return ans;
    }
}