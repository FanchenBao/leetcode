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
    private int[] getCounter(String s) {
        int[] counter = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counter[s.charAt(i) - 'a']++;
        }
        return counter;
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        /*
        LeetCode 49
        
        Use a counter for each string and turn the counter into
        something that can serve as key for a map. Here, we simply
        concatenate each value in the counter, separated by a dash.
        
        O(N * (M + 26)), where N = len(strs) and M is the average
        length of each string.
        
        20 ms, faster than 15.98%
        */
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            int[] counter = getCounter(s);
            String key = Arrays.toString(counter);
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(s);
        }
        return new ArrayList<List<String>>(map.values());
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
