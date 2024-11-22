import java.util.*;
import java.util.stream.Stream;
import java.math.*;

/**
 * Definition for a binary tree node.
 */
//class TreeNode {
//    int val;
//    TreeNode left;
//    TreeNode right;
//    TreeNode() {}
//    TreeNode(int val) { this.val = val; }
//    TreeNode(int val, TreeNode left, TreeNode right) {
//        this.val = val;
//        this.left = left;
//        this.right = right;
//    }
//}

class Solution {
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        /*
         * LeetCode 2257
         *
         * Put guards and walls positions in rows and cols, sort them, and then
         * check each cell and binary search to find whether the cell has an
         * adjacent guards on the row or on the col
         *
         * O(MNlog(MN)), 390 ms, faster than 5.26%
         */
        Map<Integer, List<int[]>> rows = new HashMap<>();        
        Map<Integer, List<int[]>> cols = new HashMap<>();        
        for (int[] g : guards) {
            rows.putIfAbsent(g[0], new ArrayList<>());
            rows.get(g[0]).add(new int[]{g[1], 0});
            cols.putIfAbsent(g[1], new ArrayList<>());
            cols.get(g[1]).add(new int[]{g[0], 0});
        }
        for (int[] w : walls) {
            rows.putIfAbsent(w[0], new ArrayList<>());
            rows.get(w[0]).add(new int[]{w[1], 1});
            cols.putIfAbsent(w[1], new ArrayList<>());
            cols.get(w[1]).add(new int[]{w[0], 1});
        }
        for (int k : rows.keySet())
            rows.get(k).sort((a, b) -> Integer.compare(a[0], b[0]));
        for (int k : cols.keySet())
            cols.get(k).sort((a, b) -> Integer.compare(a[0], b[0]));
        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rows.containsKey(i)) {
                    int idx = Collections.binarySearch(rows.get(i), new int[]{j, j}, (a, b) -> Integer.compare(a[0], b[0]));
                    if (idx >= 0) // cell is occupied
                        continue;
                    idx = -(idx + 1);
                    if ((idx < rows.get(i).size() && rows.get(i).get(idx)[1] == 0) || (idx > 0 && rows.get(i).get(idx - 1)[1] == 0))
                        // visible to at least one guard 
                        continue;
                }
                if (cols.containsKey(j)) {
                    int idx = Collections.binarySearch(cols.get(j), new int[]{i, i}, (a, b) -> Integer.compare(a[0], b[0]));
                    if (idx >= 0) // cell is occupied
                        continue;
                    idx = -(idx + 1);
                    if ((idx < cols.get(j).size() && cols.get(j).get(idx)[1] == 0) || (idx > 0 && cols.get(j).get(idx - 1)[1] == 0))
                        // visible to at least one guard 
                        continue;
                }
                res++;
            }
        }
        return res;
    }
}


class Main{
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
