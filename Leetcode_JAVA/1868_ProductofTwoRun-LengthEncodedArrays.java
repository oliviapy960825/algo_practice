/*
Medium
*/

class Solution {
    public List<List<Integer>> findRLEArray(int[][] encoded1, int[][] encoded2) {
        List<List<Integer>> res = new ArrayList<>();
        int len1 = encoded1.length, len2 = encoded2.length;
        int p1 = 0, p2 = 0;
        
        while(p1 < len1 && p2 < len2){
            int prod = encoded1[p1][0] * encoded2[p2][0];
            int num = Math.min(encoded1[p1][1], encoded2[p2][1]);
            //int num = 0;
            if(encoded1[p1][1] < encoded2[p2][1]){
                
                encoded2[p2][1] -= encoded1[p1][1];
                p1++;
            }
            else if(encoded1[p1][1] > encoded2[p2][1]){
                
                encoded1[p1][1] -= encoded2[p2][1];
                p2++;
            }
            
            else{
                p1++;
                p2++;
            }
            
            if(res.isEmpty() || prod != res.get(res.size() - 1).get(0)){
                List<Integer> list = new ArrayList<>();
                list.add(prod);
                list.add(num);
                res.add(list);
            }
            else{
                int newN = res.get(res.size() - 1).get(1) + num;
                res.get(res.size() - 1).set(1, newN);
            }
        }
        
        while(p1 < len1){
            if(encoded1[p1][1] > 0){
                List<Integer> list = new ArrayList<>();
                list.add(encoded1[p1][0]);
                list.add(encoded1[p1][1]);
                res.add(list);
            }
            p1++;
        }
        
        while(p2 < len2){
            if(encoded1[p2][1] > 0){
                List<Integer> list = new ArrayList<>();
                list.add(encoded2[p2][0]);
                list.add(encoded2[p2][1]);
                res.add(list);
            }
            p2++;
        }
        
        return res;
    }
}