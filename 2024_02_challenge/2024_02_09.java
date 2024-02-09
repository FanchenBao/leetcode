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
    Map<Integer, List<Integer>> graph = new HashMap<>();
    Map<Integer, List<Integer>> memo = new HashMap<>();

    private List<Integer> dfs(int node) {
        if (memo.containsKey(node))
            return memo.get(node);
        List<Integer> res = new ArrayList<>();
        for (int child : graph.getOrDefault(node, Collections.emptyList())) {
            List<Integer> path = dfs(child);
            if (path.size() > res.size())
                res = path;
        }
        memo.put(node, new ArrayList<>(res));
        return memo.get(node);
    }

    public List<Integer> largestDivisibleSubset(int[] nums) {
        /*
        LeetCode 368
        
        Create a directed graph where each smaller number points to
        a bigger number that divides it. Then we DFS the graph to find
        the longest path.
        
        O(N^2)
        */
        Arrays.sort(nums);        
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] % nums[i] == 0) {
                    graph.putIfAbsent(nums[i], new ArrayList<>());
                    graph.get(nums[i]).add(nums[j]);
                }
            }
        }
        List<Integer> res = new ArrayList<>();
        for (int node : nums) {
            List<Integer> path = dfs(node);
            if (path.size() > res.size())
                res = path;
        }
        return res;
    }
}


class Solution {
    // count[i] records the size of the largest divisible subset starting
    // from nums[i]
    int[] count;
    // post[i] records the next value in the path for the largest divisible
    // subset after nums[i]
    int[] post;

    private void dfs(int idx, int[] nums) {
        if (count[idx] == 0) {
            for (int i = idx + 1; i < nums.length; i++) {
                if (nums[i] % nums[idx] == 0) {
                    dfs(i, nums);
                    if (count[i] > count[idx]) {
                        count[idx] = count[i];
                        post[idx] = i;
                    }
                }
            }
            count[idx]++; // to add the current node
        }
    }

    public List<Integer> largestDivisibleSubset(int[] nums) {
        /*
         * This is the solution from 2021-11-15. It has basically the same idea
         * but the implementation is different, and most likely faster.
         *
         * O(N^2) 14 ms, faster than 75.44% 
         */
        Arrays.sort(nums);
        count = new int[nums.length];
        post = new int[nums.length];
        int maxCount = 0;
        int idx = 0;
        for (int i = 0; i < nums.length; i++) {
            dfs(i, nums);
            if (count[i] > maxCount) {
                maxCount = count[i];
                idx = i;
            }
        }
        List<Integer> res = new ArrayList<>();
        do {
            res.add(nums[idx]);
            idx = post[idx];
        } while (idx > 0);
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
