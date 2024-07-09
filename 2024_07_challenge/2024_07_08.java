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

class Node {
    int val;
    Node pre;
    Node next;
    Node (int val) {
        this.val = val;
    }
}

class Solution {
    public int findTheWinner(int n, int k) {
        /*
        LeetCode 1823
        
        Simulation, using doubly linked list. However it is
        O(N^2) with extra space.

        3 ms, faster than 49.98%
        */
        Node st = new Node(1);
        Node preNode = st;
        for (int i = 2; i <= n; i++) {
            Node cur = new Node(i);
            preNode.next = cur;
            cur.pre = preNode;
            preNode = cur;
        }
        preNode.next = st;
        st.pre = preNode;
        // simulate
        Node node = st;
        int cnt = n;
        while (cnt > 2) {
            int moves = k % cnt == 0 ? cnt : k % cnt;
            for (int i = 1; i < moves; i++)
                node = node.next;
            node.pre.next = node.next;
            node.next.pre = node.pre;
            cnt--;
            node = node.next;
        }
        return k % 2 == 0 ? node.val : node.next.val;
    }
}


class Solution2 {
    public int findTheWinner(int n, int k) {
        /*
         * This is the recursive solution from the official solution.
         * It is very very neat. By observation, we know that once we complete
         * the first step of f(n, k), the problem is converted to f(n - 1, k)
         * with shifted indices. Interestingly, the shifted index value is k.
         * Thus, we can leverage this property to solve the problem using
         * recursion.
         *
         * Although this is not constant space, but we are getting very close
         * to the requirement. This is O(N) in time.
         *
         * 0 ms, faster than 100.00%
         */
        if (n == 1)
            return 1;
        int res = (findTheWinner(n - 1, k) + k) % n;
        return res == 0 ? n : res;
    }
}


class Solution3 {
    public int findTheWinner(int n, int k) {
        /*
         * Iterative approach of Solution2, which makes the solution O(N) in
         * time and O(1) in space.
         */
        int pre = 1;
        for (int i = 2; i <= n; i++) {
            int cur = (pre + k) % i;
            if (cur == 0)
                cur = i;
            pre = cur;
        }
        return pre;
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
