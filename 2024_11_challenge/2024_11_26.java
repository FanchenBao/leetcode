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
class Solution1 {
    public int findChampion(int n, int[][] edges) {
        /*
         * LeetCode 2924
         *
         * Go through the edges. Each edge reveals one strong and one weak. We
         * use two sets to keep track of the strong and weak teams. For a weak
         * team in the current edge, we add it to the weak set. Also, if it
         * already exists in the strong set, we remove it.
         * For a strong team in the current edge, if it already exists in the
         * weak set, we do nothing. Otherwise, we add it to the strong set.
         *
         * At the end, we have a champion if there is only one team in the
         * strong set and the total number of elements in both the strong and
         * weak sets equal to n.
         *
         * O(M) where M = len(edges), 11 ms, faster than 12.09%
         */
        if (edges.length == 0) // edge case of having no edges
            return n == 1 ? 0 : -1;
        Set<Integer> strong = new HashSet<>();
        Set<Integer> weak = new HashSet<>();
        for (int[] ele : edges) {
            int st = ele[0];
            int we = ele[1];
            weak.add(we);
            if (strong.contains(we))
                strong.remove(we);
            if (!weak.contains(st))
                strong.add(st);
        }
        if (strong.size() == 1 && strong.size() + weak.size() == n)
            return new ArrayList<>(strong).get(0);
        return -1;
    }
}

class Solution2 {
    public int findChampion(int n, int[][] edges) {
        /*
         * The same solution as above but we try to make things faster by not
         * using hashset.
         * O(M + N), 2 ms, faster than 34.07%
         */
        if (edges.length == 0) // edge case of having no edges
            return n == 1 ? 0 : -1;
        boolean[] strong = new boolean[n];
        boolean[] weak = new boolean[n];
        for (int[] ele : edges) {
            int st = ele[0];
            int we = ele[1];
            weak[we] = true;
            if (strong[we])
                strong[we] = false;
            if (!weak[st]) {
                strong[st] = true;
            }
        }
        int res = 0;
        int stCnt = 0;
        int weCnt = 0;
        for (int i = 0; i < n; i++) {
            if (strong[i]) {
                res = i;
                stCnt++;
            }
            if (weak[i])
                weCnt++;
        }
        if (stCnt == 1 && stCnt + weCnt == n)
            return res;
        return -1;
    }
}


class Solution {
    public int findChampion(int n, int[][] edges) {
        /*
         * This one is from the official solution using indegree counts. I
         * cannot believe it that I forgot about indegree count.
         *
         * O(M + N), 1 ms, faster than 100.00%
         */
        int[] indegrees = new int[n];
        for (int i = 0; i < edges.length; i++)
            indegrees[edges[i][1]]++;
        int res = 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (indegrees[i] == 0) {
                res = i;
                cnt++;
            }
        }
        return cnt == 1 ? res : -1;
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
