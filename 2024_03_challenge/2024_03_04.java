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
    public int bagOfTokensScore(int[] tokens, int power) {
        /*
        LeetCode 948
        
        Each round, we always remove the smallest token and add the biggest
        token. This opeartion does not change the score, but it accumulates the
        max power at the moment. Then we check how many remaining tokens can
        fit in the current power. We use a sliding window to check the tokens.
        
        O(NlogN), 3 ms, faster than 37.26%
        */
        if (tokens.length == 0)
            return 0;
        Arrays.sort(tokens);
        int i = 0;
        int j = tokens.length - 1;
        int score = 0;
        int windowSum = 0;
        int p = 0;
        int q = -1;
        while (i < j && j > q) {
            while (q + 1 <= j && windowSum + tokens[q + 1] <= power) {
                windowSum += tokens[++q];
            }
            score = Math.max(score, q - p + 1);
            if (tokens[i] > power)
                break;
            power += tokens[j] - tokens[i];
            windowSum -= tokens[i];
            p++;
            i++;
            j--;
        }
        if (i == j && tokens[i] <= power)
            score = Math.max(score, 1);
        return score;
    }
}


class Solution1 {
    private void faceUp(int[] tokens, int[] ele) {
        while (ele[0] <= ele[1] && ele[2] >= tokens[ele[0]]) {
            ele[3]++;
            ele[2] -= tokens[ele[0]++];
        }
    }

    public int bagOfTokensScore(int[] tokens, int power) {
        /*
         * This is from my previous solution, which is exactly the same idea
         * as today, but with better implementation.
         
         4 ms, faster than 9.55%
        */
        if (tokens.length == 0)
            return 0;
        Arrays.sort(tokens);
        int[] ele = new int[]{0, tokens.length - 1, power, 0}; // index i, j, power, and score
        faceUp(tokens, ele);

        if (ele[3] == 0)
            return 0;
        while (ele[0] < ele[1] && ele[2] + tokens[ele[1]] >= tokens[ele[0]]) {
            ele[2] += tokens[ele[1]]; // get more power
            ele[1]--; // use jth token
            ele[3]--; // the cost to score by using the jth token
            faceUp(tokens, ele);
        }
        return ele[3];
    }
}


class Solution2 {
    public int bagOfTokensScore(int[] tokens, int power) {
        /*
         * This is from the official solution.
         
         O(NlogN) 2 ms, faster than 97.13% 
         */
        if (tokens.length == 0)
            return 0;
        Arrays.sort(tokens);
        int i = 0;
        int j = tokens.length - 1;
        int score = 0;
        while (i <= j) {
            if (power >= tokens[i]) {
                // face up
                score++;
                power -= tokens[i++];
            } else if (i < j && score > 0) {
                // face down
                power += tokens[j--];
                score--;
            } else {
                break;
            }
        }
        return score;
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
