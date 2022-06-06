/*
52. N-Queens II
Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:

Input: n = 1
Output: 1

 

Constraints:

    1 <= n <= 9


*/
class Solution {
    private int backtrack(int size, int row, Set<Integer> diagnoals, Set<Integer> anti_diagonals, Set<Integer> cols){
        if(row == size){
            return 1;
        }
        int solutions = 0;
        for(int col = 0; col < size; col++){
            int curr_dia = row - col;
            int curr_anti = row + col;
            if(cols.contains(col) || diagnoals.contains(curr_dia) || anti_diagonals.contains(curr_anti))
                continue;
            cols.add(col);
            diagnoals.add(curr_dia);
            anti_diagonals.add(curr_anti);
            solutions += backtrack(size, row + 1, diagnoals, anti_diagonals, cols);
            cols.remove(col);
            diagnoals.remove(curr_dia);
            anti_diagonals.remove(curr_anti);
        }
        return solutions;
    }
    public int totalNQueens(int n) {
        return backtrack(n, 0, new HashSet<>(), new HashSet<>(), new HashSet<>());
    }
}