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
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        /*
        LeetCode 1642
        
        Binary search with a touch of greedy.
        
        We find the positive diffs between adjacent heights. Sort them. Then
        run binary search to see for a given index, can we reach the index
        using the bricks and ladders. We always use ladders first on the
        biggest diffs.
        
        O(NlogN), 50 ms, faster than 5.70%
        */
        List<int[]> posDiffs = new ArrayList<>();
        for (int i = 1; i < heights.length; i++) {
            int diff = heights[i] - heights[i - 1];
            if (diff > 0)
                posDiffs.add(new int[]{diff, i});
        }
        Collections.sort(posDiffs, (a, b) -> Integer.compare(a[0], b[0]));
        // Binary search
        int lo = 0;
        int hi = heights.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            int remBricks = bricks;
            int remLadders = ladders;
            for (int i = posDiffs.size() - 1; i >= 0; i--) {
                if (posDiffs.get(i)[1] <= mid) {
                    if (remLadders > 0)
                        remLadders--;
                    else
                        remBricks -= posDiffs.get(i)[0];
                }
            }
            if (remBricks >= 0)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo - 1;
    }
}


class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        /*
         * This is the solution from my previous attempt. It uses priority
         * queue
         * 
         * O(NlogN), 19 ms, faster than 69.61%
         */
        PriorityQueue<Integer> pq = new PriorityQueue<>();
       for (int i = 1; i < heights.length; i++) {
           int diff = heights[i] - heights[i - 1];
           if (diff > 0) {
               pq.add(diff);
               if (pq.size() > ladders) {
                   bricks -= pq.poll();
                   if (bricks < 0)
                       return i - 1;
               }
           }
       } 
       return heights.length - 1;
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
