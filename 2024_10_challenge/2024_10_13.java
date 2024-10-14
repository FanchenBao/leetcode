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
    private boolean isSmallerRange(int x1, int y1, int x2, int y2) {
        // is [x1, y1] a smaller range than [x2, y2]
        if (y1 - x1 == y2 - x2)
            return x1 <= x2;
        return y1 - x1 < y2 - x2;
    }

    public int[] smallestRange(List<List<Integer>> nums) {
        /*
         * LeetCode 632
         *
         * The basic idea is that the smallest value among all the lists can
         * only have one way of becoming a range, which is to be grouped with
         * the smallest of the other lists. Since this is deterministic, we
         * don't have to branch out.
         *
         * Once the smallest value has been considered, we can elimiate and
         * move to consider the second smallest value and form the best range
         * for it. The second smallest value's range is also deterministic
         * as long as the smallest is not considered. We can compare the two
         * ranges and keep the smaller one.
         *
         * We can do this for all the numbers in order, such that each one has
         * the chance of being the smallest under the current consideration
         * and obtain the smallest possible range under that condition.
         *
         * If the true smallest range does start with the current number being
         * the smallest under the current situation, we will have found the
         * answer. If not, then it must belong to some range that has been
         * considered before. Thus, we will never miss the true smallest range.
         *
         * O(KlogK + NlogK), K = len(nums), N is the total number of values in
         * nums, 65 ms, faster than 9.18%
         */
        // [idx of list, idx within list]
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(nums.get(a[0]).get(a[1]), nums.get(b[0]).get(b[1])));
        int curMax = Integer.MIN_VALUE;
        for (int i = 0; i < nums.size(); i++) {
            pq.add(new int[]{i, 0});
            curMax = Math.max(curMax, nums.get(i).get(0));
        }
        int lo = -1000000;
        int hi = 1000000;
        while (true) {
            int[] ele = pq.poll();
            int curMin = nums.get(ele[0]).get(ele[1]);
            if (isSmallerRange(curMin, curMax, lo, hi)) {
                lo = curMin;
                hi = curMax;
                // when lo is equal to hi for the first time, it is guaranteed
                // to be the smallest range
                if (lo == hi)
                    break;
            }
            if (ele[1] + 1 == nums.get(ele[0]).size())
                break;
            pq.add(new int[]{ele[0], ele[1] + 1});
            curMax = Math.max(curMax, nums.get(ele[0]).get(ele[1] + 1));
        }
        return new int[]{lo, hi};
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
