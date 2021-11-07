class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        if(row == 1 && col == 1)
            return matrix[0][0];
        int min = Integer.MAX_VALUE;
        int[] dir = {1, 0, -1};
        int[][] memo = new int[row][col];
        for(int i = 0; i < col; i++){
            memo[0][i] = matrix[0][i];
        }
        for(int i = 1; i < row; i++){
            Arrays.fill(memo[i], Integer.MAX_VALUE);
        }
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                for(int k : dir){
                    int x = i + 1;
                    int y = j + k;
                    if(x >= row || y < 0 || y >= col)
                        continue;
                    int next = memo[i][j] + matrix[x][y];
                    if(next < memo[x][y]){
                        memo[x][y] = next;
                    }
                }
            }
        }
        
        for(int i = 0; i < col; i++){
            min = Math.min(min, memo[row - 1][i]);
        }
        
        return min;
    }
}