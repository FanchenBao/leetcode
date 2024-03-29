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
    public long countSubarrays(int[] nums, int k) {
        /*
         * LeetCode 2962
         *
         * Two pointers. First find the max value. Then we find the first
         * window where there are exactly k max values. We compute the total
         * number of subarrays ending at j that satisfy the requirements. We
         * do this by moving i forward until it hits a max. Then the number
         * of steps i moves is the number of good subarrays ending at j. 
         *
         * Then we move j forward. Each time the new nums[j] is not max, we
         * accumulate the same number of subarrays as its left neighbor. Until
         * nums[j] hits another max, then we move i forward again and repeat
         * the same process.
         *
         * O(N), 5 ms, faster than 84.18%
         */
        int max = 0;
        for (int i = 0; i < nums.length; i++) 
            max = Math.max(max, nums[i]);
        int maxCnt = 0;
        long res = 0;
        int pre = -1;
        int i = 0;
        int j = 0;
        int preCnt = 0;
        while (j < nums.length && maxCnt < k) {
            if (nums[j++] == max)
                maxCnt++;
        }
        if (maxCnt != k)
            return 0;
        j--;
        while (j < nums.length) {
            if (nums[j] == max) {
                while (i < j && nums[i] != max)
                    i++;
                preCnt += i - pre;
                pre = i;
                i++;
            }
            res += (long)preCnt;
            j++;
        }
        return res;
    }
}


class Solution2 {
    public long countSubarrays(int[] nums, int k) {
        /*
         * This is the official solution with a much simpler implementation
         * of sliding window.
         *
         * All we need to find is the window that contains exactly k max
         * elements. Then the number of good subarrays ending at j is the
         * number of elements from start to i, inclusive.
         *
         * O(N), 5 ms, faster than 84.18%
         */
        int max = 0;
        for (int i = 0; i < nums.length; i++) 
            max = Math.max(max, nums[i]);
        int i = 0;
        int maxCount = 0;
        long res = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] == max) {
                maxCount += 1;
                while (maxCount == k) {
                    if (nums[i] == max)
                        maxCount--;
                    i++;
                }
            }
            res += (long)i;
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
