/*
Medium*/

class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> list = new ArrayList();
        int p1 = 0, p2 = 0;
        int len1 = firstList.length, len2 = secondList.length;
        while(p1 < len1 && p2 < len2){
            int[] arr1 = firstList[p1];
            int[] arr2 = secondList[p2];
            int[] comm = new int[]{Math.max(arr1[0], arr2[0]), Math.min(arr1[1], arr2[1])};
            if(comm[0] <= comm[1])
                list.add(comm);
            
            if(arr1[1] < arr2[1])
                p1++;
            else
                p2++;
        }
        int[] res = new int[list.size()];
        return list.toArray(new int[][]{});
        //return list.toArray(list.size());
    }
}