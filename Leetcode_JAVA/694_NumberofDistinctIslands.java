
class Solution {
    private int[][] grid;
    private boolean[][] visited;
    private List<int[]> curr = new ArrayList();
    private List<List<int[]>> unique = new ArrayList();
    public void dfs(int row, int col){
        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length) return ;
        if(visited[row][col] || grid[row][col] == 0) return ;
        
        visited[row][col] = true;
        curr.add(new int[]{row, col});
        dfs(row + 1, col);
        dfs(row - 1, col);
        dfs(row, col + 1);
        dfs(row, col - 1);
    }
    
    public boolean currentIslandUnique(){
        for(List<int[]> otherIsland : unique){
            if(curr.size() != otherIsland.size()) continue;
            if(equal(curr, otherIsland)) return false;
        }
        
        return true;
    }
    
    public boolean equal(List<int[]> island1, List<int[]> island2){
        for(int i = 0; i < island1.size(); i++){
            if(island1.get(i)[0] != island2.get(i)[0] || island1.get(i)[1] != island2.get(i)[1]) return false;
        }
        
        return true;
    }
    
    
    public int numDistinctIslands(int[][] grid) {
        this.grid = grid;
        int row = grid.length;
        int col = grid[0].length;
        this.visited = new boolean[row][col];
        for(int r = 0; r < row; r++){
            for(int c = 0; c < col; c++){
                dfs(r, c);
                if(curr.isEmpty()) continue;
                
                int minCol = col - 1;
                for(int i = 0; i < curr.size(); i++){
                    minCol = Math.min(minCol, curr.get(i)[1]);
                }
                
                for(int[] cell : curr){
                    cell[0] -= r;
                    cell[1] -= minCol;
                }
                
                if(currentIslandUnique()){
                    unique.add(curr);
                }
                curr = new ArrayList();
            }
        }
        
        return unique.size();
    }
}