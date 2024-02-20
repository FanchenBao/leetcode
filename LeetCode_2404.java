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
    public int mostFrequentEven(int[] nums) {
        /*
        Use a counter, and then sort its key-value pair in desc for
        value and asc for key.
        
        O(NlogN)
        */
        Map<Integer, Integer> counter = new HashMap<>();
        for (int n : nums) {
            if (n % 2 == 0)
                counter.put(n, counter.getOrDefault(n, 0) + 1);
        }
        if (counter.isEmpty())
            return -1;
        List<Map.Entry<Integer, Integer>> keyVals = new ArrayList<>(counter.entrySet());
        Collections.sort(keyVals, (kv1, kv2) -> {
            int c = Integer.compare(kv1.getValue(), kv2.getValue());
            if (c == 0)
                return Integer.compare(kv1.getKey(), kv2.getKey());
            return -c;
        });
        return keyVals.get(0).getKey();
    }
}


class Solution {
    public int mostFrequentEven(int[] nums) {
        /*
         * No need to sort. One pass O(N)
         *
         * 21 ms, faster than 41.98%
         */
        Map<Integer, Integer> counter = new HashMap<>();
        int freq = 0;
        int res = 100001;
        for (int n : nums) {
            if (n % 2 == 0) {
                counter.put(n, counter.getOrDefault(n, 0) + 1);
                if (freq < counter.get(n)) {
                    freq = counter.get(n);
                    res = n;
                } else if (freq == counter.get(n)) {
                    res = Math.min(res, n);
                }
            }
        }
        return freq == 0 ? -1 : res;
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
