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
    private long count(long d, long n) {
        /*
         * Count the number of lexicographically sorted numbers with the first
         * digit being d and smaller than n
         
         * O(logN)
         */
        long c = 1;
        long res = 0;
        while (d + c - 1 <= n) {
            res += c;
            d *= 10;
            c *= 10;
        }
        if (d <= n)
            res += n - d + 1;
        return res;
    }
    
    private long kthNumberHelper(long st, long k, long n) {
        /*
         * Find the kth lexicographically sorted number given the first number
         * start with st. All of the numbers must be smaller than n.
         */
        long res = 0;
        while (k > 0) {
            res = st;
            k--;
            if (st * 10 <= n) {
                st *= 10;
            } else {
                // remove the extra digits at the right end of st
                while (st >= n || st % 10 == 9)
                    st /= 10;
                st++;
            }
        }
        return res;
    }

    public int findKthNumber(int n, int k) {
        /*
         * LeetCode 440
         *
         * We first find all the lexicographically sorted numbers starting
         * with 1 and <= n. If this count is smaller than k, that means we
         * can ignore all the lexicographically sorted numbers starting with 1.
         * We can continue with numbers starting with 2.
         *
         * We keep doing this, until we find the starting digit st of the kth
         * number.
         *
         * Then we run the algorithm to find the k'th lexicographically sorted
         * number with the starting digit being st, where k' = k - all the
         * previous number with starting number 1, 2, 3,...st - 1
         *
         * Yesterday's problem 386 helps this problem tremendously because
         * the helper function kthNumberHelper is a direct copy of the solution
         * to 386.
         *
         * One more thing to note is that there will be overflow issue. So
         * make sure to use long generously.
         *
         * Dude! TLE!!! What the heck!
         */
        long st = 1;
        long cnt = 0;
        while (true) {
            long tmp = count(st, (long)n); // count of numbers starting with st
            if (cnt + tmp < (long)k) {
                cnt += tmp;
                st++;
            } else {
                k -= (int)cnt;
                break;
            }
        }
        // now we need to find the current kth lexicographical number starting
        // with the current st
        return (int)kthNumberHelper(st, (long)k, (long)n);
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
