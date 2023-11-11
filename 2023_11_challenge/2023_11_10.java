class Solution {
     Map<Integer, List<Integer>> graph = new HashMap<>();

     public int[] restoreArray(int[][] adjacentPairs) {
         /*
         LeetCode 1743
         
         Adjacent numbers essentially form an edge. We can identify the
         number on either ends by finding the numbers with only one degree.
         Then starting from them, we can populate the rest from both ends
         in.
         
         O(N), 65 ms, faster than 94.67%
         */
        for (int[] tup : adjacentPairs) {
            graph.putIfAbsent(tup[0], new ArrayList<>());
            graph.putIfAbsent(tup[1], new ArrayList<>());
            graph.get(tup[0]).add(tup[1]);
            graph.get(tup[1]).add(tup[0]);
        }
        int[] res = new int[adjacentPairs.length + 1];
        int i = 0; int j = res.length - 1;;
        for (Integer k : graph.keySet()) {
            if (graph.get(k).size() == 1) {
                if (i == 0) {
                    res[i++] = k;
                    res[i++] = graph.get(k).get(0);
                }
                else {
                    res[j--] = k;
                    res[j--] = graph.get(k).get(0);
                    break;
                }
            }
        }
        List<Integer> children;
        while (j >= i) {
            children = graph.get(res[i - 1]);
            if (children.get(0) != res[i - 2])
                res[i++] = children.get(0);
            else
                res[i++] = children.get(1);
            children = graph.get(res[j + 1]);
            if (children.get(0) != res[j + 2])
                res[j--] = children.get(0);
            else
                res[j--] = children.get(1);
        }
        return res;
    }
}
