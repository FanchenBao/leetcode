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
    public boolean isNStraightHand(int[] hand, int groupSize) {
        /*
         * LeetCode 846
         *
         * Counter and then sort the keys. Go through the keys from small to
         * large and check whether it is possible to form consecutive groups
         * of size groupSize.
         *
         * O(NlogN), 38 ms, faster than 48.77%
         */
        if (hand.length % groupSize != 0) // cannot form integer number of groups
            return false;
        Map<Integer, Integer> counter = new HashMap<>();
        for (int h : hand)
            counter.put(h, counter.getOrDefault(h, 0) + 1);
        if (counter.size() < groupSize) // cannot form integer number of groups
            return false;
        List<Integer> keys = new ArrayList<Integer>(counter.keySet());
        Collections.sort(keys);
        for (int i = 0; i <= keys.size() - groupSize; i++) {
            if (counter.get(keys.get(i)) == 0)
                continue;
            if (i + groupSize - 1 > keys.size() || keys.get(i) + groupSize - 1 != keys.get(i + groupSize - 1))
                // cannot form consecutive numbers within a group
                return false;
            int c = counter.get(keys.get(i));
            for (int j = 0; j < groupSize; j++) {
                int cur = keys.get(i + j);
                counter.put(cur, counter.get(cur) - c);
                if (counter.get(cur) < 0)
                    return false;
            }
        }
        for (int i = keys.size() - groupSize + 1; i < keys.size(); i++) {
            if (counter.get(keys.get(i)) != 0)
                return false;
        }
        return true;
    }
}


class Solution2 {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        /*
         * Simpler logic. We directly go through the cards
         * O(NlogN), 35 ms, faster than 54.10%
         */
        if (hand.length % groupSize != 0) // cannot form integer number of groups
            return false;
        Map<Integer, Integer> counter = new HashMap<>();
        for (int h : hand)
            counter.put(h, counter.getOrDefault(h, 0) + 1);
        if (counter.size() < groupSize) // cannot form integer number of groups
            return false;
        List<Integer> keys = new ArrayList<Integer>(counter.keySet());
        Collections.sort(keys);
        for (int i = 0; i < keys.size(); i++) {
            int cur = keys.get(i);
            while (counter.get(cur) > 0) {
                for (int j = cur; j < cur + groupSize; j++) {
                    counter.put(j, counter.getOrDefault(j, 0) - 1);
                    if (counter.get(j) < 0)
                        return false;
                }
            }
        }
        return true;
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
