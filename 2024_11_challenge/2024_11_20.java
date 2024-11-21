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
    public int takeCharacters(String s, int k) {
        /*
         * LeetCode 2516
         *
         *
         */
        int N = s.length();
        if (3 * k > N)
            return -1;
        // left to right to satisfy k
        int[] counter = new int[3];
        int ltrMin = -1;
        for (int i = 0; i < N; i++) {
            counter[s.charAt(i) - 'a']++;
            boolean flag = true;
            for (int c : counter) {
                if (c < k)
                    flag = false;
            }
            if (flag) {
                ltrMin = i + 1;
                break;
            }
        }
        // right to left to satisfy k
        Arrays.fill(counter, 0);
        int rtlMin = -1;
        for (int i = 0; i < N; i++) {
            counter[s.charAt(N - i - 1) - 'a']++;
            boolean flag = true;
            for (int c : counter) {
                if (c < k)
                    flag = false;
            }
            if (flag) {
                rtlMin = i + 1;
                break;
            }
        }
        // priority queue element = [step, letter, ltr or rtl]
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        // Left to right and right to left, put in the priority queue
        for (int i = 0; i < N; i++) {
            pq.add(new int[]{i + 1, s.charAt(i) - 'a', 0});
            pq.add(new int[]{i + 1, s.charAt(N - i - 1) - 'a', 1});
        }
        int[] steps = new int[2];
        while (!pq.isEmpty()) {
            int[] ele = pq.poll();
            if (counter[ele[1]] >= k)
                continue;
            counter[ele[1]]++;
            steps[ele[2]] = ele[0];
        }
        for (int c : counter) {
            if (c < k)
                return Math.min(ltrMin, rtlMin);
        }
        if (steps[0] + steps[1] > N)
            return Math.min(ltrMin, rtlMin);
        return Math.min(Math.min(steps[0] + steps[1], ltrMin), rtlMin);
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
