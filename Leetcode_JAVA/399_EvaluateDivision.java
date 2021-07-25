/*
Medium
*/

class Solution {
    public double dfs(Map<String, Map<String, Double>> map, Set<String> visited, String end, String curr, double res){
        if(!map.containsKey(curr) || visited.contains(curr))
            return -1;
        visited.add(curr);
        Map<String, Double> next = map.get(curr);
        double max = -1.0;
        for(String s : next.keySet()){
            if(s.equals(end))
                return res * next.get(s);
            max = Math.max(max, dfs(map, visited, end, s, res * next.get(s)));
        }
        visited.remove(curr);
        return max;
    }
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        double[] res = new double[queries.size()];
        Map<String, Map<String, Double>> map = new HashMap<>();
        for(int i = 0; i < equations.size(); i++){
            List<String> list = equations.get(i);
            String a = list.get(0);
            String b = list.get(1);
            if(!map.containsKey(a))
                map.put(a, new HashMap<>());
            if(!map.containsKey(b))
                map.put(b, new HashMap<>());
            map.get(a).put(b, values[i]);
            map.get(b).put(a, 1/values[i]);
        }
        
        for(int i = 0; i < queries.size(); i++){
            List<String> query = queries.get(i);
            if(!map.containsKey(query.get(0)) || !map.containsKey(query.get(1))){
                res[i] = -1;
                //continue;
            }
            else if(query.get(0).equals(query.get(1)))
                res[i] = 1;
            else{
                Set<String> visited = new HashSet<>();
                res[i] = dfs(map, visited, query.get(1), query.get(0), 1);
            }
        }
        
        return res;
    }
}