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

class CustomStack1 {
    Stack<Integer> stack = new Stack<>();
    int maxSize;
    PriorityQueue<int[]> incMarkers = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0])); // element = [marker, freq]

    public CustomStack1(int maxSize) {
        /*
         * LeetCode 1381
         *
         * Use a regular stack to keep track of the actual values in the stack.
         * Use a max heap to record which bottom k values need to be incremented
         * by what amount.
         *
         * Push and increment are both straightforward with no fancy algorithm.
         * Except the increment need to clip k such that it is not bigger than
         * the current size of the stack.
         *
         * The trick happens in the pop function. When we pop, we need to know
         * how much increment the popped value has been subjected. We look into
         * the max heap and accumulate all the increment whose k is the same
         * as the current size of the stack. We pop these increments and pop
         * the current stack.
         *
         * But then we must add the popped increment values back to the max
         * heap and create or merge with the element with the same k as the
         * current reduced size of the stack.
         *
         * 7 ms, faster than 35.59%
         */
        this.maxSize = maxSize;
    }
    
    public void push(int x) {
        if (this.stack.size() == this.maxSize)
            return;
        stack.add(x);
    }
    
    public int pop() {
        if (this.stack.isEmpty())
            return -1;
        int incAmount = 0;
        while (!this.incMarkers.isEmpty() && this.incMarkers.peek()[0] == this.stack.size())
            incAmount += this.incMarkers.poll()[1];
        int res = this.stack.pop() + incAmount;
        if (!this.stack.isEmpty()) {
            if (!this.incMarkers.isEmpty() && this.incMarkers.peek()[0] == this.stack.size())
                this.incMarkers.peek()[1] += incAmount;
            else
                this.incMarkers.add(new int[]{this.stack.size(), incAmount});
        }
        return res;
    }
    
    public void increment(int k, int val) {
       k = Math.min(k, this.stack.size());
       this.incMarkers.add(new int[]{k, val});
    }
}


class CustomStack {
    int[] stack;
    int[] incMarkers;
    int topIdx = -1;

    public CustomStack(int maxSize) {
        /*
         * This solution is the official solution and it has the same idea as
         * mine. HOWEVER, it has a much much smarter implementation of keeping
         * track of how much increment each popped value needs to be added.
         *
         * It propagates the incremented amount just like I did, but it only
         * does it ONCE without ever having to loop. Also, since we use an
         * array instead of PriorityQueue to keep track of the incMarkers, the
         * operation of maintaining and using incMarkers is O(1) instead of
         * O(logk)
         *
         * 4 ms, faster than 100.00%
         */
        this.stack = new int[maxSize];
        this.incMarkers = new int[maxSize];
    }
    
    public void push(int x) {
        if (this.topIdx + 1 < this.stack.length)
            this.stack[++this.topIdx] = x;
    }
    
    public int pop() {
        if (this.topIdx < 0)
            return -1;
        int incAmount = this.incMarkers[this.topIdx];
        this.incMarkers[this.topIdx] = 0;
        // propagate
        if (topIdx - 1 >= 0)
            this.incMarkers[this.topIdx - 1] += incAmount;
        return this.stack[this.topIdx--] + incAmount;
    }
    
    public void increment(int k, int val) {
        if (this.topIdx >= 0)
            this.incMarkers[Math.min(k - 1, this.topIdx)] += val;
    }
}


/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */

class Main{
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
