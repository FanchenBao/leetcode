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
    public List<Integer> findDuplicates(int[] nums) {
        /*
         * LeetCode 442
         *
         * This is O(N) time and O(N) extra space. It is not following the
         * requirement of the problem, but to hell with it.
         *
         * 3 ms, faster than 99.83%
         */
        boolean[] seen = new boolean[nums.length + 1];
        List<Integer> res = new ArrayList<>();
        for (int n : nums) {
            if (seen[n])
                res.add(n);
            seen[n] = true;
        }
        return res;
    }
}


class Solution2 {
    public List<Integer> findDuplicates(int[] nums) {
        /*
         * This is the swap method which will run in O(N)
         * time and O(1) space.
         
          6 ms, faster than 74.33%
         */
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (i + 1 == nums[i])
                continue;
            int cur = nums[i];
            int nex = 0;
            nums[i] = 0;
            while (cur != 0) {
                if (nums[cur - 1] == cur) {
                    res.add(cur);
                    break;
                }
                nex = nums[cur - 1];
                nums[cur - 1] = cur;
                cur = nex;
            }
            
        }
        return res;
    }
}


class Solution3 {
    public List<Integer> findDuplicates(int[] nums) {
        /*
         * This is from the previous solution. We still doing the swapping,but
         * without actually making the swap. For each number that can swap to
         * its correct position, we set the value at the correct position to
         * negative. A number cannot swap if its corresponding position
         * already contains a negative value (this means the same number must
         * have been swapped there before, which means the current value is
         * a duplicate)
         *
         * O(N) time and O(1) extra space. 7 ms, faster than 47.90% 
         */
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[Math.abs(nums[i]) - 1] < 0)
                res.add(Math.abs(nums[i]));
            else
                nums[Math.abs(nums[i]) - 1] *= -1;
            
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
