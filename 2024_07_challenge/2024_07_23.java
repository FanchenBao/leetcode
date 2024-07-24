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
    public int[] frequencySort(int[] nums) {
        /*
         * LeetCode 1636
         *
         * This is more of a Java skill practice on custom sort.
         * 7 ms, faster than 55.67%
         */
        Map<Integer, Integer> counter = new HashMap<>();
        for (int n : nums)
            counter.put(n, counter.getOrDefault(n, 0) + 1);
        int[][] numsWithFreq = new int[nums.length][2];
        for (int i = 0; i < nums.length; i++)
            numsWithFreq[i] = new int[]{nums[i], counter.get(nums[i])};
        Arrays.sort(numsWithFreq, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                if (a[1] == b[1])
                    return b[0] - a[0];
                return a[1] - b[1];
            }
        });
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++)
            res[i] = numsWithFreq[i][0];
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
