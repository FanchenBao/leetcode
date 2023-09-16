class DSU {
    int[] par;
    int[] nodeCount;

    DSU(int N) {
        par = new int[N];
        for (int i = 0; i < N; i++) {
            par[i] = i;
        }
        nodeCount = new int[N];
    }

    int find(int x) {
        if (par[x] != x) {
            par[x] = find(par[x]);
        }
        return par[x];
    }

    boolean union(int x, int y) {
        int px = find(x); int py = find(y);
        if (px == py){
            return false;
        }
        if (nodeCount[px] >= nodeCount[py]) {
            nodeCount[px] += nodeCount[py];
            par[py] = px;
        } else {
            nodeCount[py] += nodeCount[px];
            par[px] = py;
        }
        return true;
    }
}

class Solution {
    public int minCostConnectPoints(int[][] points) {
        /*
        LeetCode 1584 (Hint)

        Fail to solve this one again. Last time I failed, it was in April, 2023. I learned about Kruskal's algo, but
        unsurprisingly, I completely forgot about it. It also took me more than one hour to sort-of understand the
        proof of Kruskal.

        602 ms, faster than 17.84%
         */
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < points.length; i++) {
            for (int j = i + 1; j < points.length; j++) {
                int dist = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                edges.add(new int[]{dist, i, j});
            }
        }
        edges.sort(Comparator.comparing(tup -> tup[0]));
        DSU dsu = new DSU(points.length);
        int res = 0; int numEdges = 0;
        for (int[] edge : edges) {
            if (dsu.union(edge[1], edge[2])) {
                res += edge[0];
                numEdges++;
                if (numEdges == points.length - 1) {
                    break;
                }
            }
        }
        return res;
    }
}
