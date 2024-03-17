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
    public int[][] insert(int[][] intervals, int[] newInterval) {
        /*
         * LeetCode 57
         *
         * Not a difficult one but quite complex. Each time we handle interval
         * merging, it is always complex. This time, we use binary search to
         * find the starting and ending point of overlap within intervals with
         * regards to newInterval. Then we iterate through intervals to push
         * all the non-affected elements in the array and ignore the range of
         * intervals being merged with newInterval.
         *
         * When we compute the range of overlap, we also update newInterval
         * according to how it overlaps with the elements in intervals.
         *
         * O(N + logN) 2 ms, faster than 44.45%
         */
        // loIdx is the starting point where newInterval is inserted
        int loIdx = Arrays.binarySearch(intervals, new int[]{0, newInterval[0]}, Comparator.comparingInt(arr -> arr[1]));
        if (loIdx >= 0) {
            newInterval[0] = intervals[loIdx][0];
        } else {
            loIdx = -(loIdx + 1);
            if (loIdx < intervals.length && intervals[loIdx][0] < newInterval[0])
                newInterval[0] = intervals[loIdx][0];
        }
        // hiIdx - 1 is the last point on the original intervals array where the
        // newInterval overlaps
        int hiIdx = Arrays.binarySearch(intervals, new int[]{newInterval[1], 0}, Comparator.comparingInt(arr -> arr[0]));
        if (hiIdx >= 0) {
            newInterval[1] = intervals[hiIdx++][1];
        } else {
            hiIdx = -(hiIdx + 1);
            if (hiIdx > 0 && intervals[hiIdx - 1][1] > newInterval[1])
                newInterval[1] = intervals[hiIdx - 1][1];
        }
        int[][] res = new int[intervals.length - (hiIdx - loIdx) + 1][2];
        int i;
        for (i = 0; i < loIdx; i++)
            res[i] = intervals[i];
        res[loIdx] = newInterval;
        int j = loIdx + 1;
        for (i = hiIdx; i < intervals.length; i++)
            res[j++] = intervals[i];
        return res;
    }
}


class Solution2 {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        /*
         * This is an even cleaner binary search solution inspired by the
         * submitted solution from last year.
         */
        // loIdx is the start of overlap
        int loIdx = Arrays.binarySearch(intervals, newInterval, Comparator.comparingInt(arr -> arr[0]));
        if (loIdx < 0) {
            loIdx = -(loIdx + 1);
            if (loIdx > 0 && intervals[loIdx - 1][1] >= newInterval[0])
                loIdx--;
        }
        // hiIdx is the start of the non-overlapping section after newInterval
        // is inserted
        int hiIdx = Arrays.binarySearch(intervals, new int[]{newInterval[1], 0}, Comparator.comparingInt(arr -> arr[0]));
        if (hiIdx >= 0)
            hiIdx++;
        else
            hiIdx = -(hiIdx + 1);
        // Update the newInterval
        if (loIdx != hiIdx) {
            newInterval[0] = Math.min(newInterval[0], intervals[loIdx][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[hiIdx - 1][1]);
        }
        int[][] res = new int[intervals.length - (hiIdx - loIdx) + 1][2];
        for (int i = 0; i < loIdx; i++)
            res[i] = intervals[i];
        res[loIdx] = newInterval;
        int j = loIdx + 1;
        for (int i = hiIdx; i < intervals.length; i++)
            res[j++] = intervals[i];
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
