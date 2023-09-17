class Solution1 {
    int[][] heights;
    int M;
    int N;
    int[][] dirs = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    private int dfs(int i, int j, int maxEff, Set<Integer> visited, int thresh) {
        if (i == M - 1 && j == N - 1) {
            return maxEff;
        }
        visited.add(i * N + j);
        for (int[] ds : dirs) {
            int ni = i + ds[0]; int nj = j + ds[1];
            if (ni < M && ni >= 0 && nj < N && nj >= 0 && !visited.contains(ni * N + nj)) {
                int diff = Math.abs(heights[i][j] - heights[ni][nj]);
                if (diff <= thresh) {
                    int res = dfs(ni, nj, Math.max(maxEff, diff), visited, thresh);
                    if (res >= 0) {
                        return res;
                    }
                }
            }
        }
        return -1; // failed to find a path that is within threshold
    }

    public int minimumEffortPath(int[][] heights) {
        /*
        LeetCode 1631

        This is the binary search solution, where we set a effort threshold and see if a path can be found that
        satisfies the threshold. If a path exists, we shrink the threshold, otherwise increase it.

        O(M * N * logK), 144 ms, faster than 10.02%
         */
        M = heights.length; N = heights[0].length;
        this.heights = heights;
        int lo = 0; int hi = 0;
        for (int[] row : heights) {
            for (int h : row) {
                hi = Math.max(hi, h);
            }
        }
        hi++;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            int maxEff = dfs(0, 0, 0, new HashSet<>(), mid);
            if (maxEff < 0) {
                lo = mid + 1;
            } else {
                hi = Math.min(mid, maxEff);
            }
        }
        return lo;
    }
}


class Solution2 {
    int[][] dirs = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    public int minimumEffortPath(int[][] heights) {
        /*
        This is Dijkstra. Pretty bad that I had this idea initially but then abondoned it. The only trick is to keep
        track of the max effort so far, instead of the total weight as in the regular Dijkstra.

        There are (N - 1) * M + (M - 1) * N = 2MN - M - N edges.
        There are M * N nodes.
        Dijkstra runs on O(VlogE) = O((2MN - M - N) log(MN)) = O(MNlogMN), 44 ms, faster than 64.59%
         */
        int M = heights.length; int N = heights[0].length;
        int[] minEffs = new int[M * N];
        Arrays.fill(minEffs, Integer.MAX_VALUE);
        minEffs[0] = 0;
        PriorityQueue<int[]> queue = new PriorityQueue<>(Comparator.comparingInt(tup -> tup[0]));
        queue.add(new int[]{0, 0, 0});
        int eff = 0;
        while (!queue.isEmpty()) {
            int[] tup = queue.poll();
            eff = tup[0]; int i = tup[1]; int j = tup[2];
            if (eff != minEffs[i * N + j]) {
                continue;
            }
            if (i == M - 1 && j == N - 1) {
                break;
            }
            for (int[] ds : dirs) {
                int ni = i + ds[0]; int nj = j + ds[1];
                if (0 <= ni && ni < M && 0 <= nj && nj < N) {
                    int curEff = Math.max(eff, Math.abs(heights[i][j] - heights[ni][nj]));
                    if (curEff < minEffs[ni * N + nj]) {
                        minEffs[ni * N + nj] = curEff;
                        queue.add(new int[]{curEff, ni, nj});
                    }
                }
            }
        }
        return eff;
    }
}
