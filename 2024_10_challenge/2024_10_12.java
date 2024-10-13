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
    public int minGroups(int[][] intervals) {
        /*
         * LeetCode 2406
         *
         * First sort intervals by its start. Then we use a priority queue
         * to keep track of the end of the last interval in each group, as well
         * as the index of the group.
         *
         * For each new interval encountered, we compare the start with the
         * smallest end in the priority queue. If the priority queue is empty
         * or the smallest end is not smaller than the new start, we can
         * guarantee that the new interval has overlap with all the intervals
         * in the groups. Thus, we create a new group.
         *
         * Otherwise, we put the new interval in the group with the smallest
         * end. In fact, this does not matter, i.e., the new interval can
         * join any group as long as its end is smaller than the new start.
         * However, we are using priority queue, and it is very easy to get
         * the smallest end among all the groups.
         *
         * One more thing to note is that we don't have to materialize the
         * groups. All we need is the end of the interval and its group's
         * index.
         *
         * O(NlogN), 100 ms, faster than 29.89% 
         */
        Arrays.sort(intervals, (a, b) -> a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]));
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0])); // [end of last interval in a group, group index]
        int res = 0;
        for (int[] interval : intervals) {
            int s = interval[0];
            int e = interval[1];
            if (pq.isEmpty() || pq.peek()[0] >= s) {
                pq.add(new int[]{e, res++});
            } else {
                pq.add(new int[]{e, pq.poll()[1]});
            }
        }
        return res;
    }
}


class Solution2 {
    public int minGroups(int[][] intervals) {
        /*
         * Update. I think we don't need to keep track of the index of the
         * group. The number of groups is the size of the priority queue. Thus
         * all we need is to keep track of the end interval.
         *
         * O(NlogN) 97 ms, faster than 38.59%
         */
        Arrays.sort(intervals, (a, b) -> a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]));
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> Integer.compare(a, b));
        for (int[] itv : intervals) {
            if (!pq.isEmpty() && pq.peek() < itv[0])
                pq.poll();
            pq.add(itv[1]);
        }
        return pq.size();
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
