class Solution1 {
    private void compute(int diff, ArrayList<int[]> diag, int[][] res) {
        HashMap<Integer, Integer> uniqsFront = new HashMap<>();
        HashMap<Integer, Integer> uniqsBack = new HashMap<>();
        for (int i = 0; i < diag.size() - 1; i++) {
            int v = diag.get(i)[1];
            uniqsFront.put(v, uniqsFront.getOrDefault(v, 0) + 1);
        }
        for (int i = diag.size() - 1; i >= 0; i--) {
            int r = diag.get(i)[0];
            int v = diag.get(i)[1];
            res[r][r - diff] = Math.abs(uniqsFront.size() - uniqsBack.size());
            uniqsBack.put(v, uniqsBack.getOrDefault(v, 0) + 1);
            if (i > 0) {
                int pre = diag.get(i - 1)[1];
                int preCount = uniqsFront.get(pre) - 1;
                if (preCount == 0) {
                    uniqsFront.remove(pre);
                } else {
                    uniqsFront.put(pre, preCount);
                }
            }
        }
    }
    public int[][] differenceOfDistinctValues(int[][] grid) {
        /*
        First obtain all the diags as arrays in a HashMap, with the keys being the diff of i and j. We
        can do this, because all the cells on the same diagonal has the same diff between i and j.

        Then for each diag array, we can compute prefix and suffix counters of values to obtain the
        number of uniques in O(N) time.

        The total runtime is O(MN), 11 ms, faster than 82.26%
         */
        HashMap<Integer, ArrayList<int[]>> diags = new HashMap<>();
        int M = grid.length;
        int N = grid[0].length;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                diags.putIfAbsent(i - j, new ArrayList<>());
                diags.get(i - j).add(new int[]{i, grid[i][j]});
            }
        }
        int[][] res = new int[M][N];
        for (Map.Entry<Integer, ArrayList<int[]>> entry: diags.entrySet()) {
            compute(entry.getKey(), entry.getValue(), res);
        }
        return res;
    }
}


class Solution2 {
    private void compute(int i, int j, ArrayList<Integer> diag, int[][] res) {
        Set<Integer> uniqsTl = new HashSet<>();
        Set<Integer> uniqsBr = new HashSet<>();
        int k = 0;
        while (i < res.length && j < res[0].length) {
            res[i][j] = uniqsTl.size();
            uniqsTl.add(diag.get(k));
            k++; i++; j++;
        }
        while (--i >= 0 && --j >= 0) {
            --k;
            res[i][j] = Math.abs(res[i][j] - uniqsBr.size());
            uniqsBr.add(diag.get(k));
        }
    }
    public int[][] differenceOfDistinctValues(int[][] grid) {
        /*
        Inspired by https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/discuss/3571235/O(m-*-n)

        Two improvements.

        1. We don't need to use a HashMap to record all the diags. We can simply traverse the first row and the first
        column to get all the diags.
        2. Instead of a sliding-window-ish way to find the answer given a diag, we can simply go through the diag two
        times. The first time from top left to bottom right, using a set to count the uniques. The second time going
        bottom right to top left and also using a set to count the uniques. The result for each cell is the absolute
        diff between the two passes.

        O(MN), 7 ms, faster than 91.94%
         */
        int M = grid.length;
        int N = grid[0].length;
        int[][] res = new int[M][N];
        // Go through the top row
        for (int j = 0; j < N; j++) {
            ArrayList<Integer> diag = new ArrayList<>();
            int i = 0; int jj = j;
            while (i < M && jj < N) {
                diag.add(grid[i][jj]);
                i++; jj++;
            }
            compute(0, j, diag, res);
        }
        // Go through the left most col
        for (int i = 1; i < M; i++) {
            ArrayList<Integer> diag = new ArrayList<>();
            int ii = i; int j = 0;
            while (ii < M && j < N) {
                diag.add(grid[ii][j]);
                ii++; j++;
            }
            compute(i, 0, diag, res);
        }

        return res;
    }
}
