class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        /*
        LeetCode 799
        
        Compute the total amount of champagn that will eventually accumulate
        at each cup, and then decide how much will be given to its two
        children.
        
        Use BFS to traverse the rows.
        
        O(N), where N is the total number of cups.
        8 ms, faster than 20.49%
        */
        double[][] champ = new double[101][101];
        champ[0][0] = poured;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});
        int i = 0; int j = 0;
        boolean[][] visited = new boolean[101][101];
        visited[0][0] = true;
        while (!queue.isEmpty()) {
            int[] coord = queue.poll();
            i = coord[0]; j = coord[1];
            if (champ[i][j] > 1) {
                champ[i + 1][j] += (champ[i][j] - 1) / 2.0; // left child
                champ[i + 1][j + 1] += (champ[i][j] - 1) / 2.0; // right child
                champ[i][j] = 1.0;
                if (!visited[i + 1][j] && i + 1 <= query_row) {
                    queue.add(new int[]{i + 1, j});
                    visited[i + 1][j] = true;
                }
                if (!visited[i + 1][j + 1] && i + 1 <= query_row) {
                    queue.add(new int[]{i + 1, j + 1});
                    visited[i + 1][j + 1] = true;
                }
            }
            if (i == query_row && j == query_glass) {
                break;
            }
        }
        return champ[query_row][query_glass];
    }
}


class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        /*
        This is the fancier and better solution, where we use 1D DP to compute the current champagn situation at
        each row.

        For cup[i][j], it depends on cup[i - 1][j] and cup[i - 1][j - 1]. Therefore, we can do 1D DP going from right
        to left to update the DP array in place for each row.
        
        O(N), where N is the total number of glasses. 3 ms, faster than 84.41%
         */
        double[] dp = new double[query_row + 1];
        dp[0] = poured;
        for (int i = 1; i <= query_row; i++) {
            for (int j = i; j >= 0; j--) {
                dp[j] = Math.max((dp[j] - 1) / 2.0, 0);
                if (j > 0) {
                    dp[j] += Math.max((dp[j - 1] - 1) / 2.0, 0);
                }
            }
        }
        return Math.min(dp[query_glass], 1.0);
    }
}
