/*
Medium
*/

class Solution {
    int[][] DIRECTIONS = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
    public void bfs(char[][] grid, boolean[][] seen, int i, int j){
        if(i >= grid.length || i < 0 || j < 0 || j >= grid[0].length || seen[i][j] || grid[i][j] != '1')
            return ;
        seen[i][j] = true;
        for(int[] d : DIRECTIONS){
            int x = i + d[0];
            int y = j + d[1];
            bfs(grid, seen, x, y);
        }
    }
    public int numIslands(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        if(m == 1 && n == 1){
            if(grid[0][0] == '1')
                return 1;
            else
                return 0;
        }
        
        int count = 0;
        boolean[][] seen = new boolean[m][n];
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == '1' && !seen[i][j]){
                    count++;
                    //seen[i][j] = true;
                    bfs(grid, seen, i, j);
                }
            }
        }
        
        return count;
    }
}