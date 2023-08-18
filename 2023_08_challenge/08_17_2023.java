class Solution {
    public int[][] updateMatrix(int[][] mat) {
        /*
        LeetCode 542
        
        BFS starting from all the zeros. Each time a new cell is reached, we increment the distance count.
        
        O(MN), 12 ms, faster than 85.51%
         */
        int M = mat.length; int N = mat[0].length;
        int[][] res = new int[M][N];
        // initialize res and find the zeros in mat
        Deque<int[]> queue = new ArrayDeque<>();
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (mat[i][j] == 0) {
                    queue.addLast(new int[]{i, j});
                    res[i][j] = 0;
                } else {
                    res[i][j] = -1;
                }
            }
        }
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!queue.isEmpty()) {
            int[] coord = queue.removeFirst();
            for (int[] d : dirs) {
                int ni = coord[0] + d[0]; int nj = coord[1] + d[1];
                if (ni >= 0 && ni < M && nj >= 0 && nj < N && res[ni][nj] < 0) {
                    res[ni][nj] = res[coord[0]][coord[1]] + 1;
                    queue.addLast(new int[]{ni, nj});
                }
            }
        }
        return res;
    }
}
