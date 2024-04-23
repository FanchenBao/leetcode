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
    int[] divs = new int[]{1000, 100, 10, 1};

    private int stringToInt(String s) {
        int dnum = 0;
        for (char c : s.toCharArray())
            dnum = 10 * dnum + (c - '0');
        return dnum;
    }

    private int arrToInt(int[] arr) {
        int dnum = 0;
        for (int d : arr)
            dnum = 10 * dnum + d;
        return dnum;
    }

    private int[] findNext(int cur) {
        int[] digits = new int[4];
        for (int i = 0; i < 4; i++) {
            digits[i] = cur / divs[i];
            cur = cur % divs[i];
        }
        int[] res = new int[8];
        for (int i = 0; i < 4; i++) {
            int original = digits[i];
            digits[i] = (original + 1) % 10;
            res[i * 2] = arrToInt(digits);
            digits[i] = (original - 1 + 10) % 10;
            res[i * 2 + 1] = arrToInt(digits);
            digits[i] = original;
        }
        return res;
    }

    public int openLock(String[] deadends, String target) {
        /*
        * LeetCode 752 (fail)
        *
        * BFS. At each state of the lock, move each wheel forward or backward by 1.
        *
        * O(10^4), 16 ms, faster than 96.35% 
        */
        int[] seen = new int[10000];
        for (String d : deadends) {
            seen[stringToInt(d)] = -2; // -2 => deadend
        }
        int targetNum = stringToInt(target);
        Deque<int[]> queue = new ArrayDeque<>();
        queue.addFirst(new int[]{0, 0});
        if (seen[0] != 0) // "0000" is a deadend
            return -1;
        seen[0] = 1;
        while (!queue.isEmpty()) {
            int[] ele = queue.removeFirst();
            if (ele[0] == targetNum)
                return ele[1];
            for (int nex : findNext(ele[0])) {
                if (seen[nex] == 0) {
                    seen[nex] = 1;
                    queue.addLast(new int[]{nex, ele[1] + 1});
                }
            }
        }
        return -1;
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
