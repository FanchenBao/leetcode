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
    public int maxDistance(List<List<Integer>> arrays) {
        /*
         * LeetCode 624
         *
         * We can prove that the answer must involve at least the min of all
         * arrays or the max of all arrays.
         *
         * Suppose we can find a pair that include neither the min nor the max
         * and yield the max distance. Then we can always use the actual max
         * to replace the current bigger value to produce a bigger distance.
         *
         * If the actual max is in the same array as the current smaller value
         * then we can use the actual min. If the actual min is in the same
         * array as the actual max and current smaller value, then it can pair
         * with the current bigger value to yield a larger distance. If the
         * acutal min is not in the same array as the actual max, then we
         * have the actual min and actual max forming the biggest distance.
         *
         * Either way, we can show that at least one of the actual min or
         * actual max must be in the max distance pair.
         *
         * O(NlogN), 65 ms, faster than 5.06%
         */
        int N = arrays.size();
        int[][] maxs = new int[N][2];
        int[][] mins = new int[N][2];
        for (int i = 0; i < arrays.size(); i++) {
            List<Integer> arr = arrays.get(i);
            maxs[i] = new int[]{arr.get(arr.size() - 1), i};
            mins[i] = new int[]{arr.get(0), i};
        }
        Arrays.sort(maxs, (a, b) -> Integer.compare(-a[0], -b[0]));
        Arrays.sort(mins, (a, b) -> Integer.compare(a[0], b[0]));
        int res = 0;
        // fix min, go through max
        int i = 0;
        while (i < N && maxs[i][1] == mins[0][1])
            i++;
        res = Math.max(res, maxs[i][0] - mins[0][0]);
        // fix max, go through min
        i = 0;
        while (i < N && mins[i][1] == maxs[0][1])
            i++;
        return Math.max(res, maxs[0][0] - mins[i][0]);
    }
}


class Solution2 {
    public int maxDistance(List<List<Integer>> arrays) {
        /*
         * This solution is from the top post. It does not sort. It simply
         * goes through all the arrays and keeps track of the overall min and
         * max so far. Then we use the overalls and the current min and max to
         * produce the potential max distance.
         *
         * The proof for this solution is that the max distance will be generated
         * by some min value among the arrays. If the corresponding max value
         * occurrs before the min is encountered, we can find such max as we
         * iterate through arrays. If the corresponding max value occurs AFTER
         * the min is encountered, then since the min will be captured by the
         * overall min, we can still apply the min to the corresponding max.
         *
         * O(N), 7 ms, faster than 82.70%
         */
        int res = 0;
        int min = arrays.get(0).get(0);
        int max = arrays.get(0).get(arrays.get(0).size() - 1);
        for (int i = 1; i < arrays.size(); i++) {
            int curMin = arrays.get(i).get(0);
            int curMax = arrays.get(i).get(arrays.get(i).size() - 1);
            res = Math.max(res, Math.abs(max - curMin));
            res = Math.max(res, Math.abs(min - curMax));
            min = Math.min(min, curMin);
            max = Math.max(max, curMax);
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
