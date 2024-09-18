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
    public String[] uncommonFromSentences(String s1, String s2) {
        /*
         * LeetCode 884
         *
         * O(M + N), 2 ms, faster than 100.00%
         */
        Map<String, Integer> map1 = new HashMap<>();
        for (String s : s1.split(" "))
            map1.put(s, map1.getOrDefault(s, 0) + 1);
        Map<String, Integer> map2 = new HashMap<>();
        for (String s : s2.split(" "))
            map2.put(s, map2.getOrDefault(s, 0) + 1);
        List<String> resList = new ArrayList<>();
        for (String s : map1.keySet()) {
            if (!map2.containsKey(s) && map1.get(s) == 1)
                resList.add(s);
        }
        for (String s : map2.keySet()) {
            if (!map1.containsKey(s) && map2.get(s) == 1)
                resList.add(s);
        }
        String[] res = new String[resList.size()];
        for (int i = 0; i < resList.size(); i++)
            res[i] = resList.get(i);
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
