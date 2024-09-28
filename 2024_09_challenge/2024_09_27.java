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


class BSTNode {
    int lo;
    int hi;
    BSTNode left;
    BSTNode right;
    int repeats;
    int oriLo;
    int oriHi;
    BSTNode oriLeft;
    BSTNode oriRight;
    int oriRepeats;

    BSTNode(int start, int end) {
        this.lo = start;
        this.hi = end;
        this.repeats = 1;
    }

    void backup() {
        this.oriLo = this.lo;
        this.oriHi = this.hi;
        this.oriLeft = this.left;
        this.oriRight = this.right;
        this.oriRepeats = this.repeats;
    }

    void restore() {
        this.lo = this.oriLo;
        this.hi = this.oriHi;
        this.left = this.oriLeft;
        this.right = this.oriRight;
        this.repeats = this.oriRepeats;
    }

    boolean add(int start, int end) {
        if (end <= this.lo) {
            if (this.left == null) {
                this.left = new BSTNode(start, end);
                return true;
            }
            return this.left.add(start, end);
        }
        if (this.hi <= start) {
            if (this.right == null) {
                this.right = new BSTNode(start, end);
                return true;
            }
            return this.right.add(start, end);
        }
        if (this.repeats == 2)
            return false;
        boolean res = true;
        this.backup();
        if (this.lo < start) {
            if (this.left == null)
                this.left = new BSTNode(this.lo, start);
            else
                res &= this.left.add(this.lo, start);
            this.lo = start;
        } else if (this.lo > start) {
            if (this.left == null)
                this.left = new BSTNode(start, this.lo);
            else
                res &= this.left.add(start, this.lo);
        }
        if (end < this.hi) {
            if (this.right == null)
                this.right = new BSTNode(end, this.hi);
            else
                res &= this.right.add(end, this.hi);
            this.hi = end;
        } else if (end > this.hi) {
            if (this.right == null)
                this.right = new BSTNode(this.hi, end);
            else
                res &= this.right.add(this.hi, end);
        }
        if (res) {
            this.repeats++;
        } else {
            // backtracking
            this.restore();
            if (this.left != null)
                this.left.restore();
            if (this.right != null)
                this.right.restore();
        }
        return res;
    }
}

class MyCalendarTwo {
    BSTNode root;

    public MyCalendarTwo() {
        this.root = null;
    }
    
    public boolean book(int start, int end) {
        /*
         * LeetCode 731
         *
         * The same idea as MyCalendar One, in which we use Binary Search Tree.
         * The difference is that in the current case, we need to keep track
         * of how many times a BSTNode has been covered already. Also, when
         * a double-booking overlap happens, we need to split the node or the
         * incoming range into the smallest possible overlapping ranges and
         * new un-overlapping ranges.
         */
        if (this.root == null) {
            this.root = new BSTNode(start, end);
            return true;
        }
        return this.root.add(start, end);
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(start,end);
 */


class Main{
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
