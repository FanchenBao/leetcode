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
    public long countSubarrays(int[] nums, int minK, int maxK) {
        /*
         * LeetCode 2444
         *
         * Make sure that nums[i:j + 1] points to the minimum possible subarray
         * that contains at least one minK or one maxK (in other words, any
         * subarray within nums[i:j + 1] that does not also include nums[i]
         * or nums[j] would not satisfy the requirement)
         *
         * We also have a pre pointing to the most recent position where the
         * value is outside the range.
         *
         * Then we can accumulate the count as i - pre. Each time j moves
         * forward, it accumulates the count of minK and maxK. As long as
         * i points to the minK or maxK that still has count of 1, we do not
         * move i. However, it the count because larger than 1, we move i until
         * the next position where it lands on either minK or maxK and its
         * count is one again. Also, each time j moves forward, we add new
         * count to the result.
         *
         * O(N) 9 ms, faster than 12.27%
         */
        int cntMin = 0;
        int cntMax = 0;
        int i = 0;
        int pre = -1;
        long res = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] < minK || nums[j] > maxK) {
                pre = j;
                i = j + 1;
                cntMin = 0;
                cntMax = 0;
                continue;
            }
            cntMin += nums[j] == minK ? 1 : 0;
            cntMax += nums[j] == maxK ? 1 : 0;
            if (cntMin > 0 && cntMax > 0) {
                while (i < j) {
                    if (nums[i] == minK) {
                        if (cntMin == 1)
                            break;
                        cntMin--;
                    }
                    if (nums[i] == maxK) {
                        if (cntMax == 1)
                            break;
                        cntMax--;
                    }
                    i++;
                }
                res += (long)(i - pre);
            }
        }
        return res;
    }
}


class Solution2 {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        /*
         * This is inspired by the official solution. It has the same concept
         * as Solution1. However, it directly looks for the most recent minK
         * index and the most recent maxK index. In solution1, we use i and j
         * and the count to search for the most recent positions of minK and
         * maxK.
         *
         * O(N), 7 ms, faster than 89.53%
         */
        int mostRecentMinK = -1;
        int mostRecentMaxK = -1;
        int mostRecentOutOfBound = -1;
        long res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < minK || nums[i] > maxK) {
                // reset
                mostRecentMaxK = -1;
                mostRecentMinK = -1;
                mostRecentOutOfBound = i;
            } else {
                if (nums[i] == minK)
                    mostRecentMinK = i;
                if (nums[i] == maxK)
                    mostRecentMaxK = i;
                if (mostRecentMinK >= 0 && mostRecentMaxK >= 0)
                    res += (long)Math.min(mostRecentMinK, mostRecentMaxK) - mostRecentOutOfBound;
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
