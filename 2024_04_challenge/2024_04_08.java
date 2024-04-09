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
    public int countStudents(int[] students, int[] sandwiches) {
        /*
         * LeetCode 1700
         *
         * The API for deque is addLast to append a value, not push. Push adds
         * the value at the front.
         *
         * 1 ms, faster than 71.05% Time complexity could be O(N^2) in worst
         * case.
         */
        Deque<Integer> q = new ArrayDeque<>();
        for (int s : students)
            q.addLast(s);
        int i = 0;
        while (i < sandwiches.length) {
            int initLen = q.size();
            for (int j = 0; j < initLen; j++) {
                int s = q.pollFirst();
                if (s == sandwiches[i]) {
                    i++;
                    break;
                } else {
                    q.addLast(s);
                }
            }
            if (initLen == q.size())
                break;
        }
        return q.size();
    }
}


class Solution2 {
    public int countStudents(int[] students, int[] sandwiches) {
        /*
         * This is the counter methof from the official solution. We count the
         * number of 1s and 0s in students. Each time a value in sandwiches
         * is encountered, we chekc whether there is a student that can match.
         * Once a sandwich cannot be matched by any student, the remaining
         * students count is the answer.
         *
         * 0 ms, faster than 100.00%
         */
        int c0 = 0;
        int c1 = 0;
        for (int s : students) {
            if (s == 0)
                c0++;
            else
                c1++;
        }
        for (int s : sandwiches) {
            if (s == 0 && c0 > 0)
                c0--;
            else if (s == 1 && c1 > 0)
                c1--;
            else
                break;
        }
        return c0 + c1;
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
