/*
Medium
*/

/**
 * // This is the GridMaster's API interface.
 * // You should not implement it, or speculate about its implementation
 * class GridMaster {
 *     boolean canMove(char direction);
 *     void move(char direction);
 *     boolean isTarget();
 * }
 */

class Solution {
    private static final int BLOCKED = -1;
    private static final int UNEXPLORED = 0;
    private static final int PATH = 1;
    private static final int TARGET = 2;
    private static final int START = 3;
    
    public int[] dfs(GridMaster master, int[][] board, int r, int c){
        if(master.isTarget()){
            board[r][c] = TARGET;
            return new int[]{r, c};
        }
        int[] res = null;
        for(Direction d : Direction.values()){
            int x = r + d.x[0];
            int y = c + d.x[1];
            if(master.canMove(d.c)){
                if(board[x][y] == UNEXPLORED){
                    master.move(d.c);
                    board[x][y] = PATH;
                    int[] target = dfs(master, board, x, y);
                    if (target != null)
                        res = target;
                    master.move(d.o);
                } 
            }
            else{  
                board[x][y] = BLOCKED;
                }
        }
        return res;
    }
    enum Direction{
        UP('U', 'D', new int[]{0,1}),
        DOWN('D', 'U', new int[]{0,-1}),
        LEFT('L', 'R', new int[]{-1,0}),
        RIGHT('R', 'L', new int[]{1,0});
        char c;
        char o;
        int[] x;
        Direction(char c, char o, int[] x){
            this.c = c;
            this.o = o;
            this.x = x;
        }
    }
    public int bfs(int[][] board, int[] target, int[] start){
        Queue<int[]> q = new LinkedList<>();
        int res = 1;
        q.offer(start);
        while(!q.isEmpty()){
            int size = q.size();
            for(int i = 0; i < size; i++){
                int[] next = q.poll();
                for(Direction d : Direction.values()){
                    int x = next[0] + d.x[0];
                    int y = next[1] + d.x[1];
                    if(board[x][y] == TARGET)
                        return res;
                    else if(board[x][y] == PATH){
                        board[x][y] = BLOCKED;
                        q.offer(new int[]{x, y});
                    }
                }
            }
            res++;
        }
        
        return res;
    }
    
    
    
    public int findShortestPath(GridMaster master) {
        //int min = Integer.MAX_VALUE;
        int m = 500;
        int[][] board = new int[m*2][m*2];
        int[] start = new int[] {m, m};
        board[m][m] = START;
        int[] target = dfs(master, board, m, m);
        return target == null ? -1 : bfs(board, target, start);
    }
}