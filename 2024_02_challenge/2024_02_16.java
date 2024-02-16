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
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        /*
        LeetCode 1481
        
        Greedy. Use a counter to get the counts of all elements in arr.
        Sort by the count from small to large. Remove the elements from
        the lowest count up.
        
        O(NlogN), 48 ms, faster than 69.11%
        */
        Map<Integer, Integer> counter = new HashMap<>();
        for (int a : arr) {
            counter.put(a, counter.getOrDefault(a, 0) + 1);
        }
        List<Integer> sortedCounts = new ArrayList<>(counter.values());
        Collections.sort(sortedCounts);
        int i = 0;
        while (k > 0 && i < sortedCounts.size()) {
            if (k >= sortedCounts.get(i)) {
                k -= sortedCounts.get(i);
                i++;
            } else {
                break;
            }
        }
        return sortedCounts.size() - i;
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
