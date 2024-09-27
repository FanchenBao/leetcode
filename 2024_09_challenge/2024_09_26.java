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

class MyCalendar {
    Map<Integer, Integer> calendar;

    public MyCalendar() {
         this.calendar = new TreeMap<>();
    }
    
    public boolean book(int start, int end) {
        /*
         * LeetCode 729
         *
         * With the help of TreeMap that can maintain the sorted order of
         * newly added time range, the problem becomes much easier. For each
         * new range, we binary search the current start times. Then we compare
         * the new range with the closest current ranges and check whether an
         * overlap exists. If not, we can add the new range.
         *
         * O(N + logN) 163 ms, faster than 12.16% 
         */
        if (this.calendar.isEmpty()) {
            this.calendar.put(start, end);
            return true;
        }
        List<Integer> keys = new ArrayList<>(this.calendar.keySet());
        int idx = Collections.binarySearch(keys, start);
        if (idx >= 0) // the start matches, must be overbooking
            return false;
        idx = -(idx + 1);
        // check whether the previous range's end is larger than the start
        if (idx > 0 && this.calendar.get(keys.get(idx - 1)) > start)
            return false;
        // check whether the next range's start is smaller than the end
        if (idx < keys.size() && keys.get(idx) < end)
            return false;
        this.calendar.put(start, end);
        return true;
    }
}


class MyCalendar2 {
    TreeMap<Integer, Integer> calendar;

    public MyCalendar2() {
         this.calendar = new TreeMap<>();
    }
    
    public boolean book(int start, int end) {
        /*
         * Same idea, but we use the built-in function to find the closest
         * neighbors of the new start-end range.
         *
         * O(logN), 22 ms, faster than 62.47%
         */
        if (this.calendar.isEmpty()) {
            this.calendar.put(start, end);
            return true;
        }
        Integer pre = this.calendar.floorKey(start);
        Integer nex = this.calendar.ceilingKey(start);
        if ((pre == null || this.calendar.get(pre) <= start) && (nex == null || nex >= end)) {
            this.calendar.put(start, end);
            return true;
        }
        return false;
    }
}

class BSTNode {
    int lo;
    int hi;
    BSTNode left;
    BSTNode right;
    BSTNode (int start, int end) {
        this.lo = start;
        this.hi = end;
    }

    boolean insert (int start, int end) {
        if (end <= this.lo) {
            if (this.left == null) {
                this.left = new BSTNode(start, end);
                return true;
            }
            return this.left.insert(start, end);
        }
        if (start >= this.hi) {
            if (this.right == null) {
                this.right = new BSTNode(start, end);
                return true;
            }
            return this.right.insert(start, end);
        }
        return false;
    }
}

class MyCalendar3 {
    BSTNode root = null;

    public MyCalendar3() {}
    
    public boolean book(int start, int end) {
        /*
         * Use binary search tree
         *
         * 11 ms, faster than 100.00%
         */
        if (this.root == null) {
            this.root = new BSTNode(start, end);
            return true;
        }
        return this.root.insert(start, end);
    }
}



/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
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
