/*
Medium
*/

class Solution {
    public int dfs(int[][] grid, int i, int j, boolean[][] visited){
        if(i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] == 0 || visited[i][j])
            return 0;
        visited[i][j] = true;
        return 1 + dfs(grid, i + 1, j, visited) + dfs(grid, i - 1, j, visited) + dfs(grid, i, j + 1, visited) + dfs(grid, i, j - 1, visited);
    }
    public int maxAreaOfIsland(int[][] grid) {
        if(grid == null || grid.length == 0 || grid[0].length == 0)
            return 0;
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        int max = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 1)
                    max = Math.max(max, dfs(grid, i, j, visited));
            }
        }
        
        return max;
    }
}