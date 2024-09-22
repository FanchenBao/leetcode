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
    public List<Integer> lexicalOrder(int n) {
        /*
         * LeetCode 386
         *
         * This is not following the requirement. It is the dirty method.
         *
         * O(NlogN) time with O(N) space. 21 ms, faster than 11.50% 
         */
        List<String> tmp = new ArrayList<>();
        for (int i = 1; i <= n; i++)
            tmp.add(String.valueOf(i));
        Collections.sort(tmp);
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; i++)
            res.add(Integer.parseInt(tmp.get(i)));
        return res;
    }
}


class Solution2 {
    public List<Integer> lexicalOrder(int n) {
        /*
         * LeetCode 386
         *
         * This is the solution with O(N) time and O(1) space. We try a number.
         * If it is good, we add it, and then multiple it by 10.
         *
         * If i is not good, we reverse the multiplication and start to add
         * 1 until we hit n or the next multiple of 10. Then we remove any
         * trailing zeros and start the next round.
         *
         * 5 ms, faster than 42.61%
         */
        List<Integer> res = new ArrayList<>();
        int cur = 1;
        while (res.size() < n) {
            if (cur <= n) {
                res.add(cur);
                cur *= 10;
            } else {
                cur = cur / 10 + 1;
                while (cur <= n && cur % 10 != 0)
                    res.add(cur++);
                if (cur % 10 != 0)
                    cur = cur / 10 + 1;
                while (cur % 10 == 0) // remove trailing zeros
                    cur /= 10;
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
