class Solution {
    public int[][] onesMinusZeros(int[][] grid) {
        /*
        LeetCode 2482
        
        Find the counts of 1s for each row and col, then compute diff directly.
        The count of zeros can be computed as M - count col or N - count row.
        
        O(MN), 9 ms, faster than 66.67%
         */
        int M = grid.length; int N = grid[0].length;
        int[] onesRow = new int[M]; // count of 1s for each row
        int[] onesCol = new int[N]; // count of 1s for each col
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                onesRow[i] += grid[i][j];
                onesCol[j] += grid[i][j];
            }
        }
        int[][] diff = new int[M][N];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                diff[i][j] = onesRow[i] + onesCol[j] - (N - onesRow[i]) - (M - onesCol[j]);
            }
        }
        return diff;
    }
}
