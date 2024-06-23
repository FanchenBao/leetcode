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
    public int numberOfSubarrays(int[] nums, int k) {
        /*
         * LeetCode 1248
         *
         * Count the number of evens between each pair of odds. From that we
         * can know the number of different ways to form subarrays using the
         * odds flanking the evens.
         *
         * Then it is a sliding window to sum all the different ways to form
         * subarrays about each window of odds.
         *
         * O(N), 9 ms, faster than 83.51%
         */
        List<Integer> cntEven = new ArrayList<>();
        int preIdx = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 1) {
                cntEven.add(i - preIdx);
                preIdx = i;
            }
        }
        cntEven.add(nums.length - preIdx);
        int res = 0;
        for (int i = 0; i + k < cntEven.size(); i++)
            res += cntEven.get(i) * cntEven.get(i + k);
        return res;
    }
}


class Solution2 {
    public int numberOfSubarrays(int[] nums, int k) {
        /*
         * This solution is from the official solution. It converts the numbers
         * into 0 and 1 for even and odd. Then what we need to find is the
         * number of subarrays whose sum is equal to k. We can use a prefix
         * sum with counter to solve this problem (it is equivalent to the
         * question of subarray sum equal to k)
         *
         * O(N),4 ms, faster than 99.09%
         */
        int[] counter = new int[50001];
        counter[0] = 1;
        int res = 0;
        int cur = 0; // current prefix sum
        for (int n : nums) {
            cur += n % 2;
            if (cur >= k)
                res += counter[cur - k];
            counter[cur]++;
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
