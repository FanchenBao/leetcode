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

class Solution {
    public int largestSubmatrix(int[][] matrix) {
        /*
        This is from the official solution where each row in the matrix after
        computing the cumulative height of each cell is NOT sorted.
        
        The idea is that we always have a previous row that is sorted in descend.
        We place both the height and the col index in the sorted previous row.
        preRow[j] = (height, col)
        Then we iterate from left to right on the previous sorted row. If
        row[preRow[j][1]] > 0, then its value must be bigger than preRow[j][0],
        which means in the current sorted row, it maintains the same position
        as the previous row.
        
        If row[preRow[j][i]] == 0, then this value is gone in the current sorted
        row.
        
        After we go through all the cols in the previous row, we have made the
        decision whether these cols will continue to be in the current sorted
        row or not. Then we have to go through the current row again to find any
        values that are 1. These cells do not exist in the previous sorted row,
        yet they must be included towards the end of the current sorted row.
        
        After we get the current sorted row, we can compute all possible set up
        of rectangles.
        
        O(MN), 21 ms, faster than 17.76% 
        */
        int M = matrix.length; int N = matrix[0].length;
        for (int j = 0; j < N; j++) {
            for (int i = 0; i < M; i++) {
                if (i > 0 && matrix[i][j] == 1 && matrix[i - 1][j] >= 1)
                    matrix[i][j] = matrix[i - 1][j] + 1;
            }
        }
        int res = 0;
        List<int[]> preRow = new ArrayList<>();
        for (int[] row : matrix) {
            List<int[]> curRow = new ArrayList<>();
            for (int[] tup : preRow) {
                int v = tup[0]; int col = tup[1];
                if (row[col] > 0)
                    curRow.add(new int[]{row[col], col});
            }
            for (int j = 0; j < N; j++) {
                if (row[j] == 1)
                    curRow.add(new int[]{1, j});
            }
            for (int k = 0; k < curRow.size(); k++) {
                res = Math.max(res, curRow.get(k)[0] * (k + 1));
            }
            preRow = curRow;
        }
        return res;
    }
}

