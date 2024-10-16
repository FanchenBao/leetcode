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
    public long maxKelements(int[] nums, int k) {
        /*
         * LeetCode 2530
         *
         * Use max heap
         *
         * O(NlogN + KlogN) 122 ms, faster than 76.78% 
         */
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        long res = 0;
        for (int n : nums)
            pq.add(n);
        for (int i = 0; i < k; i++) {
            int tmp = pq.poll();
            res += (long)tmp;
            pq.add((int)Math.ceil(tmp / 3.0));
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
