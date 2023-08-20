class DSU {
    int[] par;
    int[] cnt; // cnt[i] is the number of connected nodes with i as their parent

    DSU(int n) {
        this.par = new int[n];
        this.cnt = new int[n];
        for (int i = 0; i < n; i++) {
            this.par[i] = i;
            this.cnt[i] = 1;
        }
    }

    public int find(int x) {
        if (par[x] != x) {
            par[x] = find(par[x]);
        }
        return par[x];
    }

    public boolean union(int x, int y) {
        int px = find(x); int py = find(y);
        if (px == py) {
            return false;
        }
        if (cnt[px] >= cnt[py]) {
            par[py] = px;
            cnt[px] += cnt[py];
        } else {
            par[px] = py;
            cnt[py] += cnt[px];
        }
        return true;
    }
}

class Solution {
    int n;
    int[][] edges;
    int[][] sortedEdges; // must be sorted based on edge weights, element -> [a, b, weight, idx]

    private int findMSTWeight(int initWeight, Set<Integer> initEdges, Set<Integer> removedEdges) {
        int totalWeights = initWeight;
        DSU dsu = new DSU(n);
        ArrayList<Integer> edgesList = new ArrayList<>(initEdges);
        for (int ei : edgesList) {
            dsu.union(edges[ei][0], edges[ei][1]);
        }
        for (int i = 0; i < sortedEdges.length && edgesList.size() < n - 1; i++) {
            int a = sortedEdges[i][0]; int b = sortedEdges[i][1];
            int w = sortedEdges[i][2]; int idx = sortedEdges[i][3];
            if (!initEdges.contains(idx) && !removedEdges.contains(idx) && dsu.union(a, b)) {
                totalWeights += w;
                edgesList.add(idx);
            }
        }
        // check if the MST is connected
        return dsu.cnt[dsu.find(0)] == n ? totalWeights : Integer.MAX_VALUE;
    }

    public List<List<Integer>> findCriticalAndPseudoCriticalEdges(int n, int[][] edges) {
        /*
        LeetCode 1489 (Hint)

        What a problem! Love it! Learned a lot. The Kruskal algorithm (I think I have encountered it before, but
        definitely not at the same level as today); all the Java shenenigans; the good practice of debugger; all in all
        this was a very good experience.

        The hints are very helpful. Basically, we use Kruskal to find the MST weights. Then we remove each edge and
        recompute MST. If the weight increases, the edge is critical.

        After that, we pre-include each edge (not including the critical ones) and compute MST. If the resulting weight
        is equal to the actual min weight, the edge is pseudo-critical.

        O(EV), 46 ms, faster than 40.26% 
         */
        this.n = n;
        this.edges = edges;
        this.sortedEdges = new int[edges.length][4];
        for (int i = 0; i < edges.length; i++) {
            sortedEdges[i] = new int[]{edges[i][0], edges[i][1], edges[i][2], i};
        }
        Arrays.sort(sortedEdges, Comparator.comparingInt(tup -> tup[2]));
        int minWeight = findMSTWeight(0, Collections.emptySet(), Collections.emptySet());
        // remove each edge and see if the min weight increases. If it does, the removed edge is critical
        Set<Integer> criticalSet = new HashSet<>();
        for (int[] ele : sortedEdges) {
            int idx = ele[3];
            if (findMSTWeight(0, Collections.emptySet(), new HashSet<>(List.of(idx))) > minWeight) {
                criticalSet.add(idx);
            }
        }
        // add each edge to the potential MST, and check if the actual MST has the same weight as minWeight.
        // If it does, then the added edge is a pseudo-critical edge
        List<Integer> pseudoCritical = new ArrayList<>();
        int initWeight = 0;
        for (int idx : criticalSet) {
            initWeight += edges[idx][2];
        }
        for (int[] ele : sortedEdges) {
            int idx = ele[3];
            if (!criticalSet.contains(idx)) {
                criticalSet.add(idx);
                if (findMSTWeight(initWeight + edges[idx][2], criticalSet, Collections.emptySet()) == minWeight) {
                    pseudoCritical.add(idx);
                }
                criticalSet.remove(idx);
            }

        }
        return Arrays.asList(new ArrayList<>(criticalSet), pseudoCritical);
    }
}
