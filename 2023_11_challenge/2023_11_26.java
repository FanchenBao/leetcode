class Solution {
    public int largestSubmatrix(int[][] matrix) {
        /*
        LeetCode 1727 (Fail)
        
        Unable to solve this one. The solution is smart. We compute
        the height of ones at each cell. Then sort each row. Then we
        know for that row what is the max possible height of a submatrix
        of a given width.
        
        O(MNlogN)
        */
        int M = matrix.length; int N = matrix[0].length;
        for (int j = 0; j < N; j++) {
            for (int i = 0; i < M; i++) {
                if (i > 0 && matrix[i][j] == 1 && matrix[i - 1][j] >= 1)
                    matrix[i][j] = matrix[i - 1][j] + 1;
            }
        }
        int res = 0;
        for (int[] ints : matrix) {
            Arrays.sort(ints);
            // ints[j] is the max height of ones at position j
            // N - j is the max width to accomodate the height ints[j]
            for (int j = N - 1; j >= 0 && ints[j] > 0; j--)
                res = Math.max(res, ints[j] * (N - j));
        }
        return res;
    }
}
