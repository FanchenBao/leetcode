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
    public long countFairPairs(int[] nums, int lower, int upper) {
        /*
         * LeetCode 2563
         *
         * After sorting nums, we can solve this problem by using binary search
         * on each number in nums. This will run O(NlogN + NlogN) time.
         *
         * However, we can also use a sliding window technique, where we keep
         * track of the range of numbers that satisfy fair pairs. When a new
         * number is encountered (it is bigger than the previous), we shift
         * the window to the left. This will end once the right index touches
         * the index of the current number. This will run O(NlogN + N) time.
         *
         * 25 ms, faster than 62.32%
         */
        Arrays.sort(nums);
        long res = 0;
        int i = 1;
        while (i < nums.length) {
            if (nums[i] >= lower - nums[0])
                break;
            i++;
        }
        int j = 1;
        while (j < nums.length) {
            if (nums[j] > upper - nums[0])
                break;
            j++;
        }
        res += j - i;
        int k = 1;
        while (j > k && k < nums.length) {
            while (i > 0 && nums[i - 1] >= lower - nums[k])
                i--;
            while (j > 0 && nums[j - 1] > upper - nums[k])
                j--;
            if (j <= k)
                break;
            res += (long)(j - Math.max(i, k + 1));
            k++;
        }
        return res;
    }
}


class Solution2 {
    private long countLower(int[] nums, int thresh) {
        long res = 0;
        int i = 0;
        int j = nums.length - 1;
        while (i < j) {
            if (nums[i] + nums[j] < thresh) {
                res += (long)(j - i);
                i++;
            } else {
                j--;
            }
        }
        return res;
    }

    public long countFairPairs(int[] nums, int lower, int upper) {
        /*
         * This is from the official solution. We just need to find the total
         * number of pairs whose sum is smaller or equal to upper (or in other
         * words, smaller than upper + 1), and the total number of pairs whose
         * sum is smaller than lower. The difference between these two counts
         * is our answer.
         *
         * O(NlogN + N), 23 ms, faster than 100.00%
         */
        Arrays.sort(nums);
        return countLower(nums, upper + 1) - countLower(nums, lower);
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
