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
    public char[][] rotateTheBox(char[][] box) {
        /*
         * LeetCode 1861
         *
         * The formula for rotation is ni = j; nj = M - 1 - i.
         * Then for each stone, we rotate it and check if there is any space
         * beneath it that can allow it to fall.
         *
         * O(MN^2), 18 ms, faster than 30.08%
         */
        int M = box.length;
        int N = box[0].length;
        char[][] res = new char[N][M];
        for (char[] row : res)
            Arrays.fill(row, '.');
        for (int i = M - 1; i >= 0; i--) {
            for (int j = N - 1; j >= 0; j--) {
                int ni = j;
                int nj = M - 1 - i;
                if (box[i][j] == '*') {
                    res[ni][nj] = '*';
                } else if (box[i][j] == '#') {
                    while (ni + 1 < N && res[ni + 1][nj] == '.')
                        ni++;
                    res[ni][nj] = '#';
                }
            }
        }
        return res;
    }
}


class Solution2 {
    public char[][] rotateTheBox(char[][] box) {
        /*
         * The first solution is O(MN^2). This one originates from the official
         * solution and is O(MN). The key is that we keep track of the position
         * of the lowest empty cell. Then each time a stone is encountered,
         * we can place it there directly without having to go through yet
         * another loop.
         *
         * This is the real O(MN), 7 ms, faster than 79.67%
         */
        int M = box.length;
        int N = box[0].length;
        char[][] res = new char[N][M];
        for (char[] row : res)
            Arrays.fill(row, '.');
        for (int i = M - 1; i >= 0; i--) {
            int lastRowWithEmptyCell = N - 1;
            for (int j = N - 1; j >= 0; j--) {
                int nj = M - 1 - i;
                if (box[i][j] == '*') {
                    res[j][nj] = '*';
                    lastRowWithEmptyCell = j - 1;
                } else if (box[i][j] == '#') {
                    res[lastRowWithEmptyCell--][nj] = '#';
                }
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
