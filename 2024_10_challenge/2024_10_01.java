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
    public boolean canArrange(int[] arr, int k) {
        /*
         * LeetCode 1497
         *
         * A first round naive check is to see if the sum of all arr can be
         * divisible by k. If not, there is no way to arrange the pairs.
         *
         * Get the count of each remainder when a value in arr MOD k.
         * To have a pair whose sum is divisible by k, the sum of their
         * remainders must be either k, -k or 0.
         *
         * For a positive remainder r, its matching remainder can be -r or
         * k - r. For -r and k - r, their other matching remainder is r - k.
         *
         * Thus for all of them to match, we need to count of r and r - k to
         * equal the count of -r and k - r. Because otherwise, there will be
         * some remainders that do not have a match.
         *
         * We use this to examine if a remainder can find all its matches in
         * the array.
         *
         * O(N), 34 ms, faster than 51.44%
         */
        // First round of naive check.
        long total = 0;
        for (long a : arr)
            total += a;
        if (total % k != 0)
            return false;
        Map<Integer, Integer> remCounter = new HashMap<>();
        for (int a : arr)
            remCounter.put(a % k, remCounter.getOrDefault(a % k, 0) + 1);
        for (int r : new ArrayList<>(remCounter.keySet())) {
            if (!remCounter.containsKey(r))
                continue;
            int rr = Math.abs(r);
            int[] rems = new int[]{rr, rr - k, k - rr, -rr};
            // Compare the count of rr + rr - k and k - rr + (-rr)
            if (remCounter.getOrDefault(rems[0], 0) + remCounter.getOrDefault(rems[1], 0) == remCounter.getOrDefault(rems[2], 0) + remCounter.getOrDefault(rems[3], 0)) {
                // we have good pairing, remove all of them
                for (int rrr : rems) {
                    if (remCounter.containsKey(rrr))
                        remCounter.remove(rrr);
                }
            }
        }
        return remCounter.isEmpty();
    }
}



class Solution2 {
    public boolean canArrange(int[] arr, int k) {
        /*
         * Make all the remainders positive, then we only need to check two
         * matching remainders. Also, we probably don't need to use the naive
         * first round check.
         *
         * Pay attention that values from the Map cannot compare directly without
         * first converting to primitive types. If you want to compare the values
         * directly, you must use Objects.equals
         * 24 ms, faster than 53.09%
         */
        // First round of naive check. Can speed up the algo
        long total = 0;
        for (long a : arr)
            total += a;
        if (total % k != 0)
            return false;
        Map<Integer, Integer> remCounter = new HashMap<>();
        for (int a : arr) {
            int r = (a % k + k) % k;
            remCounter.put(r, remCounter.getOrDefault(r, 0) + 1);
        }
        for (int r : remCounter.keySet()) {
            if (r == 0) {
                if (remCounter.get(0) % 2 != 0)
                    return false;
            } else if (!Objects.equals(remCounter.get(r), remCounter.get(k - r))) {
                return false;
            }
        }
        return true;
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
