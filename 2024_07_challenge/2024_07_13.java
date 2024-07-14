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
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        /*
         * LeetCode 2751
         *
         * This is definitely not as difficult as yesterday, where the proof
         * of a greedy solution really floored me. This one is pretty much
         * straightforward solving, with a little bit twist and turn here and
         * there.
         *
         * O(NlogN), 67 ms, faster than 26.25%
         */
        int N = positions.length;
        int[][] phd = new int[N][4];
        for (int i = 0; i < N; i++)
            phd[i] = new int[]{positions[i], healths[i], directions.charAt(i) == 'R' ? 1 : -1, i};
        Arrays.sort(phd, (a, b) -> Integer.compare(a[0], b[0]));
        Stack<int[]> stack = new Stack<>();
        for (int[] robot : phd) {
            while (!stack.isEmpty() && robot[2] == -1 && stack.peek()[2] == 1 && robot[1] > 0) {
                if (stack.peek()[1] < robot[1]) {
                    stack.pop();
                    robot[1]--;
                } else if (stack.peek()[1] == robot[1]) {
                    stack.pop();
                    robot[1] = 0;
                } else {
                    robot[1] = 0;
                    stack.peek()[1]--;
                }
            }
            if (robot[1] > 0)
                stack.add(robot);
        }
        int[] resArr = new int[N];
        for (int[] robot : stack)
            resArr[robot[3]] = robot[1];
        List<Integer> res = new ArrayList<>();
        for (int r : resArr) {
            if (r > 0)
                res.add(r);
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
