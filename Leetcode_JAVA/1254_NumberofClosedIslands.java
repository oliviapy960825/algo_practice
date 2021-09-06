/*
Medium
*/
class Solution {
    boolean[][] visited;
    public void dfs(int[][] grid, int row, int col){
        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || visited[row][col] || grid[row][col] != 0) return ;
        visited[row][col] = true;
        dfs(grid, row - 1, col);
        dfs(grid, row + 1, col);
        dfs(grid, row, col - 1);
        dfs(grid, row, col + 1);
    }
    public int closedIsland(int[][] grid) {
        if(grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        int row = grid.length;
        int col = grid[0].length;
        visited = new boolean[row][col];
        for(int i = 0; i < row; i++){
            if(grid[i][0] == 0) dfs(grid, i, 0);
            if(grid[i][col - 1] == 0) dfs(grid, i, col - 1);
        }
        for(int i = 0; i < col; i++){
            if(grid[0][i] == 0) dfs(grid, 0, i);
            if(grid[row - 1][i] == 0) dfs(grid, row - 1, i);
        }
        
        int count = 0;
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(!visited[i][j] && grid[i][j] == 0){
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        
        return count;
    }
}