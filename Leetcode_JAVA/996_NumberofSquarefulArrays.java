/*
Hard
*/

class Solution {
    int count = 0;
    public boolean isSquare(int a, int b){
        double sqr = Math.sqrt(a+b);
        boolean res = (sqr - Math.floor(sqr)) == 0;
        return res;
    }
    
    private void helper(List<Integer> temp, int[] A, boolean[] used, int lastNumber){
        if (temp.size()==A.length){
            count++;
        } else {
            for (int i = 0; i<A.length;i++){
                if (used[i] || (i>0 && A[i]==A[i-1] && !used[i-1]))continue;
                if (lastNumber!=-1){
				// if we cant form a square we can not proceed to form a squareful array
                    if (isSquare(A[i],lastNumber)==false)
                        continue;
                }
                used[i] = true;
                temp.add(A[i]);
                helper(temp,A,used,A[i]);
                temp.remove(temp.size()-1);
                used[i] = false;
            }
        }
        
    }
    
    public int numSquarefulPerms(int[] nums) {
        //int count = 0;
        Arrays.sort(nums);
        //Set<List<Integer>> seen = new HashSet<>();
        List<Integer> list = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        helper(list, nums, used, -1);
        return count;
    }
}