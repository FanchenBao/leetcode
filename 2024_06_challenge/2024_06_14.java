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
    public int minIncrementForUnique(int[] nums) {
        /*
         * LeetCode 945
         *
         * Greedy. We do not touch the numbers that are already unique in nums.
         * For the rest, we simply go from 1 to infinity. If the current is
         * not one of the uniques and if it is bigger than the duplicates, we
         * move the smallest duplicate towards the current value.
         *
         * O(NlogN); 78 ms, faster than 15.41%
         *
         * This is way too slow
         */
        Set<Integer> seen = new HashSet<>();
        List<Integer> extras = new ArrayList<>();
        for (int n : nums) {
            if (!seen.contains(n))
                seen.add(n);
            else
                extras.add(n);
        }
        Collections.sort(extras);
        int i = 0;
        int cur = 1;
        int res = 0;
        while (i < extras.size()) {
            if (!seen.contains(cur) && cur > extras.get(i))
                res += cur - extras.get(i++);
            cur++;
        }
        return res;
    }
}


class Solution2 {
    public int minIncrementForUnique(int[] nums) {
        /*
         * Same idea as above, but let's try speeding things up.
         *
         * We will go through the gaps within uniques, and compare the values
         * in the gap with the current extra
         *
         * O(NlogN), 50 ms, faster than 20.33%
         */
        List<Integer> uniques = new ArrayList<>();
        uniques.add(-1);
        List<Integer> extras = new ArrayList<>();
        Arrays.sort(nums);
        for (int n : nums) {
            if (uniques.get(uniques.size() - 1) != n)
                uniques.add(n);
            else
                extras.add(n);
        }
        uniques.add(Integer.MAX_VALUE);
        int j = 0;
        int res = 0;
        for (int i = 1; i < uniques.size() && j < extras.size(); i++) {
            // examine each gap between adjacent uniques
            int lo = Math.max(uniques.get(i - 1) + 1, extras.get(j) + 1);
            int hi = uniques.get(i) - 1;
            while (lo <= hi && j < extras.size()) {
                res += lo - extras.get(j++);
                if (j < extras.size())
                    lo = Math.max(extras.get(j) + 1, lo + 1);
            }
        }
        return res;
    }
}


class Solution3 {
    public int minIncrementForUnique(int[] nums) {
        /*
         * None of my solutions are fast. The solution in the official solution
         * is very good. Sort nums, and modify it in place to create a
         * sort of monotonic increasing array. For nums[i], nums[i - 1] is
         * the max value allowed so far. Then nums[i] need to be converted
         * to nums[i - 1] + 1, unless nums[i] itself is bigger than nums[i - 1]
         *
         * O(NlogN), 37 ms, faster than 72.13%
         */
        Arrays.sort(nums);
        int res = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] <= nums[i - 1]) {
                res += nums[i - 1] + 1 - nums[i];
                nums[i] = nums[i - 1] + 1;
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
