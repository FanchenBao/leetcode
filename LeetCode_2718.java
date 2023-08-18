class Solution1 {
    public long matrixSumQueries(int n, int[][] queries) {
        /*
        Since once a row or col gets overwritten, the previous values do not count. Therefore, we only need
        to concern the last time a row or col appears in queries.
        
        Then we go through these queries in order. Each time a row or col shows up, we add the value multiplied
        by n. Also, for each added row, all previous cols at the some row need to be deducted from the result.
        The same for added col. Thus, we keep track of a prefix sum of rows and cols to facilitate this removal.
        
        O(N + MlogM), where M = len(queries). 
         */
        // Initialize rows and cols
        long[][] rows = new long[n][2];
        long[][] cols = new long[n][2];
        for (int i = 0; i < n; i++) {
            rows[i][0] = Integer.MAX_VALUE;
            cols[i][0] = Integer.MAX_VALUE;
        }
        for (int i = 0; i < queries.length; i++) {
            if (queries[i][0] == 0) {
                rows[queries[i][1]][0] = i; rows[queries[i][1]][1] = queries[i][2];
            } else {
                cols[queries[i][1]][0] = i; cols[queries[i][1]][1] = queries[i][2];
            }
        }
        Arrays.sort(rows, Comparator.comparingLong(tup -> tup[0]));
        Arrays.sort(cols, Comparator.comparingLong(tup -> tup[0]));
        long res = 0; long psumRow = 0; long psumCol = 0;
        int i = 0; int j = 0;
        while (i < n && rows[i][0] < Integer.MAX_VALUE && j < n && cols[j][0] < Integer.MAX_VALUE) {
            if (rows[i][0] < cols[j][0]) {
                res += (rows[i][1] * n - psumCol);
                psumRow += rows[i][1];
                i++;
            } else {
                res += (cols[j][1] * n - psumRow);
                psumCol += cols[j][1];
                j++;
            }
        }
        while (i < n && rows[i][0] < Integer.MAX_VALUE) {
            res += (rows[i][1] * n - psumCol);
            i++;
        }
        while (j < n && cols[j][0] < Integer.MAX_VALUE) {
            res += (cols[j][1] * n - psumRow);
            j++;
        }
        return res;
    }
}

class Solution2 {
    public long matrixSumQueries(int n, int[][] queries) {
        /*
        Inspired by the titles of the forum. We already know that only the last occurrence of query matters.
        Thus, instead of going from left to right to find the last occurrence, we can easily go from right to
        left and consider only the first occurrence of any query to a certain row or col. Then we can use a
        seen array to check whether a row or col has been handled already. Also, when we go right to left,
        each time a row or col is considered, we must NOT count the values that have already been assigned
        on the opposite direction. Thus, we have to keep track of the number of rows or cols that have been
        handled.

        O(N), 3 ms, faster than 100.00%
         */
        long res = 0;
        int[][] seen = new int[2][n];
        int[] count = new int[2]; // count the number of unique rows and cols encountered in queries
        for (int i = queries.length - 1; i >= 0; i--) {
            int type = queries[i][0]; int idx = queries[i][1]; int v = queries[i][2];
            if (seen[type][idx] == 0) {
                // not encountered yet
                res += (long) v * (n - count[type ^ 1]);
                count[type] += 1;
                seen[type][idx] = 1;
            }
        }
        return res;
    }
}
