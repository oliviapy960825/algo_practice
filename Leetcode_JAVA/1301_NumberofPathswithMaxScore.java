class Solution {
    private static final int[][] DIRS = new int[][]{{0, -1}, {-1, 0}, {-1, -1}};
    public int[] pathsWithMaxScore(List<String> board) {
        int m = board.size(), n = board.get(0).length();
        int[][] sum = new int[m][n], cnt = new int[m][n];
        cnt[m - 1][n - 1] = 1;
        for(int i = m - 1; i >= 0; i--){
            for(int j = n - 1; j >=0; j--){
                if(cnt[i][j] == 0)
                    continue;
                for(int[] dir : DIRS){
                    int x = i + dir[0];
                    int y = j + dir[1];
                    if(x >= 0 && y >= 0 && board.get(x).charAt(y) != 'X'){
                        int newSum = sum[i][j];
                        if(board.get(x).charAt(y) != 'E')
                            newSum += board.get(x).charAt(y) - '0';
                        if(newSum == sum[x][y])
                            cnt[x][y] = (cnt[x][y] + cnt[i][j]) % 1000000007;
                        else if(newSum > sum[x][y]){
                            sum[x][y] = newSum;
                            cnt[x][y] = cnt[i][j];
                        }
                    }
                }
            }
        }
        
        return new int[]{sum[0][0], cnt[0][0]};
    }
}