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
    public int minKBitFlips(int[] nums, int k) {
        /*
         * LeetCode 995
         *
         * There is a bit greedy here. We will always flip the first 0 encountered.
         * I believe this will always result in the least number of flips,
         * because if we don't do so, we will double our efforts in flipping
         * some bits.
         *
         * Then we need a mechanism to keep track of the number of flips a
         * bit down the array has been subjected to. For this, we use a queue
         * (this comes from the hint) in which we save the right limit of
         * each flip. Before we consider each bit, we remove from the left all
         * the right limits that are smaller than the current position, since
         * those flips do not overlap the current position. Then we can use
         * the size of the queue to indicate the number of flips the current
         * position has been subjected to. This will help determine what
         * the current bit should be after those flips.
         *
         * O(N)
         *
         * Update: use flieEnds.size() % 2 == nums[i] to decide whether
         the current but is zero after all the previous flips. Also, since
         we are checking for unflippable zeros, we don't have to do the
         extra check at the beginning.
         */
        Deque<Integer> flipEnds = new ArrayDeque<>();
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            while (!flipEnds.isEmpty() && flipEnds.peekFirst() < i)
                flipEnds.removeFirst();
            if (flipEnds.size() % 2 == nums[i]) { // current bit is zero
                if (i + k <= nums.length) {
                    res++;
                    flipEnds.add(i + k - 1);
                } else {
                    return -1; // we have a zero in a non-flippable position
                }
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
