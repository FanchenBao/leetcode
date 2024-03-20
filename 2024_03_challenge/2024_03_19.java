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
    public int leastInterval(char[] tasks, int n) {
        /*
        LeetCode 621
        
        Use priority queue. Each element in the queue is [nextAvailableTime, count]
        We always pop the task with the earlieset next available time. If several
        tasks have the same next available time, we pick the one with the highest
        count. This is because if we exhaust the low count task first, then we
        increase the chance of idling with only the high count tasks left.
        
        22 ms, faster than 48.07%
        */
        int[] counter = new int[26];
        for (char c : tasks)
            counter[c - 65]++;
        PriorityQueue<int[]> pq = new PriorityQueue<>(26, (x, y) -> {
            // x = [nextAvailableTime, count]
            if (x[0] == y[0])
                return Integer.compare(y[1], x[1]); // larger count goes first
            return Integer.compare(x[0], y[0]); // smaller position goes first
        });
        for (int i = 0; i < 26; i++) {
            if (counter[i] > 0)
                pq.add(new int[]{0, counter[i]});
        }
        int res = 0;
        while (!pq.isEmpty()) {
            while (pq.peek()[0] > res)
                res++;
            int[] ele = pq.poll();
            ele[1]--;
            res++;
            if (ele[1] > 0) {
                ele[0] += n + 1;
                pq.add(ele);
            }
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
