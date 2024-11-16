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
    public int findLengthOfShortestSubarray(int[] arr) {
        /*
         * LeetCode 1574
         *
         * Binary search. We use an aux array to record whether arr[i:] is
         * non-decreasing. Then we specify a subarray length and then sliding
         * window it to check whether removing it can make the remainder array
         * into non-decreasing. The checks include
         * 1. Whether the subarray to the right is non-decreasing (we use the
         * aux array for this)
         * 2. Whether the subarray to the left is non-decreasing (we will keep
         * track of each adjacent pair of numbers to the left and check whether
         * they follow the non-decreasing order)
         * 3. Whether the numbers surrounding the removed subarray follow the
         * non-decreasing order.
         *
         * O(NlogN), 1 ms, faster than 100.00% 
         */
        boolean[] aux = new boolean[arr.length];
        aux[arr.length - 1] = true;
        for (int i = arr.length - 2; i >= 0 && arr[i] <= arr[i + 1]; i--) 
            aux[i] = true;
        int lo = 0;
        int hi = arr.length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            boolean works = false;
            for (int i = 0, j = mid - 1; j < arr.length; j++, i++) {
                if (i > 1 && arr[i - 1] < arr[i - 2])
                    break;  // no way to recover from this
                if (j < arr.length - 2 && !aux[j + 1])
                    continue;
                if (i > 0 && j < arr.length - 1 && arr[i - 1] > arr[j + 1])
                    continue;
                
                works = true;
                break;
            }
            if (works)
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }
}


class Solution2 {
    public int findLengthOfShortestSubarray(int[] arr) {
        /*
         * This is the two-pointer solucion from the official solution.
         * The right index j starts at the left most index such that arr[j:] is
         * non-decreasing.
         * The left index i starts at 0, and for each arr[i], we move j to the
         * right until the first arr[j] >= arr[i]. Then it is guaranteed that
         * arr[i+1:j] is the shortest subarray given the current i and j to
         * be removed such that the remaining is non-decreasing.
         *
         * We must also ensure that arr[:i + 1] is non-dreasing as well.
         *
         * O(N), 3 ms, faster than 32.14%
         */
        int j = arr.length - 1;
        while (j > 0 && arr[j - 1] <= arr[j])
            j--;
        int res = j; // since arr[j:] are non-decreasing, we can remove arr[:j]
        for (int i = 0; i < j && (i == 0 || arr[i] >= arr[i - 1]); i++) {
            while (j < arr.length && arr[j] < arr[i])
                j++;
            res = Math.min(res, j - i - 1);
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
