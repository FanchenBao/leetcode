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
    public String longestDiverseString(int a, int b, int c) {
        /*
         * LeetCode 1405 (Hint)
         *
         * We will use priority queue to always try the letter with the max
         * frequency. If it is possible, we use it. If not, we use the letter
         * with the second max frequency.
         *
         * I thought of this before, but didn't think it would work. 
         *
         * O(a + b + c), 2 ms, faster than 52.46%. The priority queue takes
         * O(3) time, which can be ignored.
         *
         * Also, since there are only three counters to compare, we can use
         * three separate counters and avoid using priority queue.
         */
        // [freq, letter]
        PriorityQueue<int[]> pq = new PriorityQueue<>((x, y) -> Integer.compare(y[0], x[0]));
        if (a > 0)
            pq.add(new int[]{a, 'a'});
        if (b > 0)
            pq.add(new int[]{b, 'b'});
        if (c > 0)
            pq.add(new int[]{c, 'c'});
        StringBuilder res = new StringBuilder();
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            if (res.length() < 2 || (res.charAt(res.length() - 1) == cur[1] && res.charAt(res.length() - 2) != cur[1]) || res.charAt(res.length() - 1) != cur[1]) {
                res.append((char)cur[1]);
                cur[0]--;
            } else if (!pq.isEmpty()) {
                int[] nex = pq.poll();
                res.append((char)nex[1]);
                nex[0]--;
                if (nex[0] > 0)
                    pq.add(nex);
            } else {
                break;
            }
            if (cur[0] > 0)
                pq.add(cur);
        }
        return res.toString();
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
