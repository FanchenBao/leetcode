import java.util.*;
import java.util.stream.Stream;
import java.math.*;

// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};


class Solution {
    private void postorder(Node node, List<Integer> res) {
        if (node == null)
            return;
        for (Node c : node.children)
            postorder(c, res);
        res.add(node.val);
    }

    public List<Integer> postorder(Node root) {
        /*
         * LeetCode 590
         */
        List<Integer> res = new ArrayList<>();
        postorder(root, res);
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
