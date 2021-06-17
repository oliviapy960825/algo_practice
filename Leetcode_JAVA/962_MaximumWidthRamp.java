class Solution {
    public int maxWidthRamp(int[] nums) {
        List<Integer> list = new ArrayList<>();
        int max = 0;
        for(int i = 0; i < nums.length; i++){
            if(list.size() == 0 || nums[i] < nums[list.get(list.size() - 1)])
                list.add(i);
            else{
                int left = 0, right = list.size() - 1, mid;
                while(left + 1 < right){
                    mid = left + (right - left) / 2;
                    int ind = list.get(mid);
                    if(nums[ind] <= nums[i])
                        right = mid;
                    else
                        left = mid;
                }
                
                if(nums[list.get(left)] <= nums[i])
                    max = Math.max(max, i - list.get(left));
                else
                    max = Math.max(max, i - list.get(right));
            }
        }
        
        return max;
    }
}