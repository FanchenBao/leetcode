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
    public int countTriplets(int[] arr) {
        /*
         * LeetCode 1442
         *
         * Prefix XOR, record the indices of all the repeated xor values. If
         * we can find a subarray whose cumulative xor is zero, we can divide
         * it into the desired triplets.
         *
         * O(N^2), 5 ms, faster than 33.85%
         */
        int xor = arr[0];
        Map<Integer, List<Integer>> indices = new HashMap<>();
        indices.put(xor, new ArrayList<>());
        indices.get(xor).add(0);
        for (int i = 1; i < arr.length; i++) {
            xor = xor ^ arr[i];
            indices.putIfAbsent(xor, new ArrayList<>());
            indices.get(xor).add(i);
        }
        int res = 0;
        for (int k : indices.keySet()) {
            List<Integer> vals = indices.get(k);
            if (k == 0) {
                for (int i : vals)
                    res += i;
            }
            for (int j = 0; j < vals.size() - 1; j++) {
                for (int m = j + 1; m < vals.size(); m++)
                    res += vals.get(m) - vals.get(j) - 1;
            }
        }
        return res;
   }
}


class Solution2 {
    public int countTriplets(int[] arr) {
        /*
         * The computation can be further simplified to reduce the run time to
         * O(N), 2 ms, faster than 77.44%
         */
        int xor = arr[0];
        Map<Integer, List<Integer>> indices = new HashMap<>();
        indices.put(xor, new ArrayList<>());
        indices.get(xor).add(0);
        for (int i = 1; i < arr.length; i++) {
            xor = xor ^ arr[i];
            indices.putIfAbsent(xor, new ArrayList<>());
            indices.get(xor).add(i);
        }
        int res = 0;
        for (int k : indices.keySet()) {
            List<Integer> vals = indices.get(k);
            if (k == 0) {
                for (int i : vals)
                    res += i;
            }
            int cnt = 1;
            int total = vals.get(0);
            for (int j = 1; j < vals.size(); j++) {
                res += vals.get(j) * cnt - total - cnt;
                cnt++;
                total += vals.get(j);
            }
        }
        return res;
   }
}


class Solution3 {
    public int countTriplets(int[] arr) {
        /*
         * Further simplification, built on Solution2
         *
         * O(N), 2 ms, faster than 77.44%
         */
        int xor = arr[0];
        Map<Integer, Integer> cnt = new HashMap<>();
        Map<Integer, Integer> total = new HashMap<>();
        cnt.put(xor, 1);
        total.put(xor, 0);
        int res = 0;
        for (int i = 1; i < arr.length; i++) {
            xor = xor ^ arr[i];
            if (xor == 0)
                res += i;
            res += (i - 1) * cnt.getOrDefault(xor, 0) - total.getOrDefault(xor, 0);
            cnt.put(xor, cnt.getOrDefault(xor, 0) + 1);
            total.put(xor, total.getOrDefault(xor, 0) + i);
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
