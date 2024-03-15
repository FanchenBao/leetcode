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
    private int solveZero(int[] nums) {
        // Find consecutive stretches of zeros.
        int curCnt = 0;
        int res = 0;
        for (int n : nums) {
            if (n == 0) {
                curCnt++;
            } else {
                res += (curCnt + 1) * curCnt / 2;
                curCnt = 0;
            }
        }
        return res + (curCnt + 1) * curCnt / 2;
    }

    public int numSubarraysWithSum(int[] nums, int goal) {
        /*
        LeetCode 930
        
        I think the method for when goal is zero is different from
        when goal is non zero. When it is zero, we simply look for
        stretches of zeros. When non zero, we tally all the ones
        together and form a window whose size is goal. Then we look
        towards the left and right to include extra zeros.
        
        O(N), 4 ms, faster than 54.72%
        */
        if (goal == 0)
            return solveZero(nums);
        List<Integer> onePos = new ArrayList<>();
        onePos.add(-1);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1)
                onePos.add(i);
        }
        onePos.add(nums.length);
        int res = 0;
        for (int i = 1; i + goal - 1 < onePos.size() - 1; i++) {
            int j = i + goal - 1;
            res += (onePos.get(i) - onePos.get(i - 1)) * (onePos.get(j + 1) - onePos.get(j));
        }
        return res;
    }
}


class Solution2 {
    public int numSubarraysWithSum(int[] nums, int goal) {
        /*
         * This is the prefix sum + frequency method from the official solution.
         *
         * It is essentially finding the number of subarrays ending at each
         * position. If we have kept the prefix sum for each position, to
         * get to the goal, we only need to know how many previous prefix sums
         * when deducted from the current one ends up with goal.
         *
         * O(N) 20 ms, faster than 49.97%
         */
        Map<Integer, Integer> counter = new HashMap<>();
        counter.put(0, 1);
        int presum = 0;
        int res = 0;
        for (int n : nums) {
            presum += n;
            res += counter.getOrDefault(presum - goal, 0);
            counter.put(presum, counter.getOrDefault(presum, 0) + 1);
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
