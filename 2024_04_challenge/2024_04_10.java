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
    public int[] deckRevealedIncreasing(int[] deck) {
        /*
         * LeetCode 950
         *
         * Simulate the whole deck revealing process using a queue. The only
         * modification is that we keep track of the pseudo indices of the
         * cards and use them to decide whether a card is ready to be revealed
         *
         * O(N^2), 5 ms, faster than 13.35%
         */
        Arrays.sort(deck);
        int idx = 0;
        int[] res = new int[deck.length];
        Deque<int[]> queue = new ArrayDeque<>();
        for (int i = 0; i < deck.length; i++)
            queue.addLast(new int[]{i, i});
        while (!queue.isEmpty()) {
            int[] ele = queue.removeFirst();
            if (ele[0] % 2 == 0 || queue.isEmpty())
                res[ele[1]] = deck[idx++];
            else
                queue.addLast(new int[]{queue.peekLast()[0] + 1, ele[1]});
        }
        return res;
    }
}


class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        /*
         * Simulated approach from the official solution
         
         O(N), 4 ms, faster than 86.41% 
         */
        Arrays.sort(deck);
        int[] res = new int[deck.length];
        Deque<Integer> indices = new ArrayDeque<>();
        for (int i = 0; i < deck.length; i++)
            indices.addLast(i);
        for (int d : deck) {
            res[indices.removeFirst()] = d;
            if (!indices.isEmpty())
                indices.addLast(indices.removeFirst());
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
