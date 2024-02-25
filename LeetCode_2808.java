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
    public int minimumSeconds(List<Integer> nums) {
        /*
        Find the max gap (including wrap-around gap) between each pair of
        identical numbers. For those numbers that occurr only once, its gap
        is the length of nums minus one.
        
        The answer needs to use the number that has the min of these max gap.
        
        O(N), 48 ms, faster than 96.00%
        */
        Map<Integer, int[]> map = new HashMap<>(); // the array is [first occurrence idx, previous occurrence idx, max gap between any consecutive two occurrences]
        for (int i = 0; i < nums.size(); i++) {
            if (map.containsKey(nums.get(i))) {
                int[] g = map.get(nums.get(i));
                g[2] = Math.max(g[2], i - g[1] - 1);
                g[1] = i;
            } else {
                map.put(nums.get(i), new int[]{i, i, -1});
            }
        }
        int minGap = nums.size();
        for (int[] g : map.values()) {
            // when g[2] == -1, that means the number only occurrs once in nums
            // we also need to use g[0] and g[1] to compute the wrap-around gap
            minGap = Math.min(minGap, g[2] == -1 ? nums.size() - 1 : Math.max(g[2], nums.size() - g[1] - 1 + g[0]));
        }
        return (minGap + 1) / 2;
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
