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
    int res = 0;
    int[] counter = new int[1001];

    private void backtrack(int idx, int subsetSize, int[] nums, int k) {
        if (idx == nums.length) {
            res += subsetSize > 0 ? 1 : 0;
        } else {
            backtrack(idx + 1, subsetSize, nums, k); // skip the current number
            if (nums[idx] - k < 0 || counter[nums[idx] - k] == 0) {
                // use the current number
                counter[nums[idx]]++;
                backtrack(idx + 1, subsetSize + 1, nums, k);
                counter[nums[idx]]--;
            }
        }
    }

    public int beautifulSubsets(int[] nums, int k) {
        /*
         * LeetCode 2597
         *
         * Backtrack with a counter to keep record of what
         * numbers have been included in the current subset
         *
         * 69 ms, faster than 62.07%
         */
        Arrays.sort(nums);
        backtrack(0, 0, nums, k);
        return res;
    }
}


class Solution2 {
    public int beautifulSubsets(int[] nums, int k) {
        /*
         * This is the solution from a previous attempt at the problem. We
         * group all the numbers that MOD k resulting in the same remainder.
         * Then any subset of one such group can always be paired with another
         * group without having any members between the groups having difference
         * equal to k.
         *
         * The problem now becomes finding the beautiful subsets within each
         * subgroup. We go from small to large in each subgroup and make sure
         * when computing the number of subsets that end in the current number,
         * we do not include any of the subsets that end in the previous
         * number.
         *
         * 7 ms, faster than 82.11%
         */
        int[] counter = new int[1001];
        Arrays.fill(counter, -1);
        for (int n : nums) {
            if (counter[n] < 0)
                counter[n] = 1;
            else
                counter[n]++;
        }
        int res = 1;
        for (int i = 1; i <= 1000; i++) {
            if (counter[i] > 0 && (i - k <= 0 || counter[i - k] < 0)) {
                // ensure that i is the smallest number in the subgroup under
                // consideration
                int cur = i;
                int dp0 = 1; // the number of subsets within the subgroup that does not include the previous number (it is one because of empty set)
                int dp1 = 0; // the number of subsets within the subgroup that includes the previous number;
                while (cur <= 1000) {
                    if (counter[cur] < 0)
                        counter[cur] = 0;
                    int tmp = dp0;
                    dp0 = dp0 + dp1;
                    dp1 = tmp * ((1 << counter[cur]) - 1);
                    cur += k;
                }
                res *= (dp0 + dp1);
            }
        }
        return res - 1; // do not include the empty subset
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
