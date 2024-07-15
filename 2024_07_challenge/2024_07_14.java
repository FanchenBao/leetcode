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
    private int strToNumber(String numStr) {
        int res = 0;
        for (char n : numStr.toCharArray())
            res = res * 10 + n - '0';
        return res;
    }
    
    private List<String> getComonents(String formula) {
        List<String> comps = new ArrayList<>();
        StringBuilder cur = new StringBuilder();
        for (char f : formula.toCharArray()) {
            if (f >= 'a' && f <= 'z') {
                cur.append(f);
            } else if (f >= 'A' && f <= 'Z') {
                if (!cur.isEmpty()) {
                    comps.add(cur.toString());
                    cur.setLength(0);
                }
                cur.append(f);
            } else if (f >= '0' && f <= '9') {
                if (!cur.isEmpty() && cur.charAt(0) > '9') {
                    comps.add(cur.toString());
                    cur.setLength(0);
                }
                cur.append(f);
            } else {
                if (!cur.isEmpty()) {
                    comps.add(cur.toString());
                    cur.setLength(0);
                }
                comps.add(String.valueOf(f));
            }
        }
        if (!cur.isEmpty())
            comps.add(cur.toString());
        return comps;
    }

    public String countOfAtoms(String formula) {
        /*
         * LeetCode 726
         *
         * Not a hard problem, but very commplex to implement.
         *
         * 8 ms, faster than 15.84%
         */
        // Break down the formula to components
        List<String> comps = getComonents(formula);

        Stack<Map<String, Integer>> stack = new Stack<>();
        for (String c : comps) {
            if (c.equals("(")) {
                stack.add(new HashMap<>(Map.of("(", 1)));
            } else if (c.charAt(0) > '9') {
                // an atom
                stack.add(new HashMap<>(Map.of(c, 1)));
            } else if (c.charAt(0) >= '0' && c.charAt(0) <= '9') {
                // a number
                Map<String, Integer> cnt = stack.pop();
                int num = strToNumber(c);
                cnt.replaceAll((a, v) -> cnt.get(a) * num);
                stack.add(cnt);
            } else {
                // right parenthesis
                Map<String, Integer> cnt = new HashMap<>();
                while (!stack.peek().containsKey("(")) {
                    for (Map.Entry<String, Integer> entry : stack.pop().entrySet())
                        cnt.put(entry.getKey(), cnt.getOrDefault(entry.getKey(), 0) + entry.getValue());
                }
                stack.pop(); // pop left parenthesis
                stack.add(cnt);
            }
        }
        Map<String, Integer> cnt = new HashMap<>();
        while (!stack.isEmpty()) {
            for (Map.Entry<String, Integer> entry : stack.pop().entrySet())
                cnt.put(entry.getKey(), cnt.getOrDefault(entry.getKey(), 0) + entry.getValue());
        }
        StringBuilder res = new StringBuilder();
        for (Map.Entry<String, Integer> entry: new TreeMap<>(cnt).entrySet()) {
            res.append(entry.getKey());
            if (entry.getValue() > 1)
                res.append(entry.getValue());
        }
        return res.toString();
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
