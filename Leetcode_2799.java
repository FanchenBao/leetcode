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
    public int countCompleteSubarrays(int[] nums) {
        /*
        Use sliding window. And for each window that contains the same
        number of unique values as the total array, we count the number
        of subarrays starting from the current start of the sliding window.
        
        O(N), 6 ms, faster than 95.47%
        */
        Map<Integer, Integer> counter = new HashMap<>();
        Set<Integer> uniqs = new HashSet<>();
        for (int n : nums)
            uniqs.add(n);
        int i = 0;
        int res = 0;
        for (int j = 0; j < nums.length; j++) {
            counter.put(nums[j], counter.getOrDefault(nums[j], 0) + 1);
            while (i <= j && counter.size() == uniqs.size()) {
                res += nums.length - j;
                counter.put(nums[i], counter.get(nums[i]) - 1);
                if (counter.get(nums[i]) == 0)
                    counter.remove(nums[i]);
                i++;
            }
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
