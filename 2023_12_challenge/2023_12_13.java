class Solution {
    public int numSpecial(int[][] mat) {
        /*
        LeetCode 1582
        
        Brute force. O(M(M + N)), 1 ms, faster than 99.75%
         */
        int M = mat.length; int N = mat[0].length;
        int res = 0;
        for (int[] row : mat) {
            int k = -1;
            int c = 0;
            for (int j = 0; j < N; j++) {
                if (row[j] == 1) {
                    k = j;
                    c++;
                    if (c > 1)
                        break;
                }
            }
            if (c == 1) {
                int cc = 0;
                for (int[] ints : mat) {
                    if (ints[k] == 1)
                        cc++;
                }
                if (cc == 1)
                    res++;
            }
        }
        return res;
    }
}


class Solution {
    public int numSpecial(int[][] mat) {
        /*
        Use 2D prefix sum to compute the number of 1s in each
        row and col in O(1)
        
        The total runtime is O(MN),  3 ms, faster than 23.23%
        */
        int M = mat.length; int N = mat[0].length;
        int[][] presum = new int[M][N];
        for (int i = 0; i < M; i++) {
            int pre = 0;
            for (int j = 0; j < N; j++) {
                pre += mat[i][j];
                presum[i][j] = pre + (i > 0 ? presum[i - 1][j] : 0);
            }
        }
        int res = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (mat[i][j] == 1) {
                    int cRow = i > 0 ? presum[i][N - 1] - presum[i - 1][N - 1] : presum[i][N - 1];
                    int cCol = j > 0 ? presum[M - 1][j] - presum[M - 1][j - 1] : presum[M - 1][j];
                    if (cRow == 1 && cCol == 1)
                        res++;
                }
            }
        }
        return res;
    }
}


class Solution {
    public int numSpecial(int[][] mat) {
        /*
        No need for 2D array. Just use a rowCount and colCount
        array to find the total number of 1s in each row and col.
        
        Inspired by the official solution.
        
        O(MN) 2 ms, faster than 88.89%
        */
        int M = mat.length; int N = mat[0].length;
        int[] rowCount = new int[M];
        int[] colCount = new int[N];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                rowCount[i] += mat[i][j];
                colCount[j] += mat[i][j];
            }
        }
        int res = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1) 
                    res++;
            }
        }
        return res;
    }
}
