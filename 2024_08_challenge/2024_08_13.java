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
    private void backtrack(List<Integer> uniques, int target, int[] counter, int idx, List<Integer> cur, int curSum, List<List<Integer>> res) {
        if (curSum == target) {
            res.add(new ArrayList<>(cur));
            return;
        }
        if (idx == uniques.size()) {
            return;
        }
        int curVal = uniques.get(idx);
        for (int n = 0; n <= counter[curVal]; n++) {
            int newSum = curSum + curVal * n;
            if (newSum <= target) {
                for (int i = 0; i < n; i++)
                    cur.add(curVal);
                backtrack(uniques, target, counter, idx + 1, cur, newSum, res);
                for (int i = 0; i < n; i++)
                    cur.remove(cur.size() - 1);
            } else {
                break;
            }
        } 
    }
    
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        /*
         * LeetCode 40
         *
         * Use backtracking on the unique values in candidates. For each unique
         * value, we can choose to select 0, 1, 2, ... n number of it. And then
         * moving on to the next.
         *
         * 2 ms, faster than 99.70%
         */
        int[] counter = new int[51];
        List<Integer> uniques = new ArrayList<>();
        for (int c : candidates) {
            counter[c]++;
            if (counter[c] == 1)
                uniques.add(c);
        }
        List<List<Integer>> res = new ArrayList<>();
        backtrack(uniques, target, counter, 0, new ArrayList<>(), 0, res);
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
