/*
Medium
*/

class Solution {
    public int minNumberOfFrogs(String frog) {
        if(frog.length() < 5)
            return -1;
        int max = 0;
        int c = 0, r = 0, o = 0, a = 0, k = 0;
        int use = 0;
        for(char ch : frog.toCharArray()){
            switch(ch){
                case 'c':
                    c++;
                    use++;
                    break;
                case 'r':
                    r++;
                    break;
                case 'o':
                    o++;
                    break;
                case 'a':
                    a++;
                    break;
                case 'k':
                    k++;
                    use--;
                    break;
            }
            max = Math.max(max, use);
            if ((c < r) || (r < o) || (o < a) || (a < k)) 
                return -1;
        }
        if (use == 0 && c == r && c == o && c == a && c == k)
            return max;
        return -1;
    }
}