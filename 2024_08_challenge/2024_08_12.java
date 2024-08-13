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

class KthLargest {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    int k;

    public KthLargest(int k, int[] nums) {
        /*
         * LeetCode 703
         *
         * Use priority queue
         *
         * 13 ms, faster than 82.29%
         */
        this.k = k;
        for (int n : nums)
            this.add(n);
    }
    
    public int add(int val) {
        if (minHeap.size() < this.k) {
            minHeap.add(val);
        } else if (minHeap.peek() < val) {
            minHeap.poll();
            minHeap.add(val);
        }
        return minHeap.peek();
    }
}



/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */

class Main{
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
