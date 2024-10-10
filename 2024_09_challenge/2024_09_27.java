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

class MyCalendarTwo1 {
    List<int[]> booked = new ArrayList<>(); // interval with single or double booking
    List<int[]> doubleBooked = new ArrayList<>(); // range with double booking

    public MyCalendarTwo1() {
       /*
        * This solution is from the official solution of using two lists to
        * keep track of all the intervals that are booked and doubly booked.
        *
        * When a new range comes, we first check the double booked list. If
        * any interval has overlap with the new range, it is a triple booking
        * and we return false.
        *
        * Otherwise, we go through the booked list and make any overlap
        * into the double booking list.
        *
        * There is no need to make any modifications to the intervals already
        * in the list, because any duplicate overlap in the booked
        * list would have been identified in the double booking list already.
        */
    }

    private boolean hasOverlap(int[] r1, int[] r2) {
        return r1[1] > r2[0] && r1[0] < r2[1];
    }

    private int[] getOverlap(int[] r1, int[] r2) {
        return new int[]{Math.max(r1[0], r2[0]), Math.min(r1[1], r2[1])};
    }
    
    public boolean book(int start, int end) {
        int[] cur = new int[]{start, end};
        // check triple booking
        for (int[] db : this.doubleBooked) {
            if (hasOverlap(db, cur))
                return false;
        }
        // update the bookings list
        for (int[] sb : this.booked) {
            if (hasOverlap(sb, cur))
                this.doubleBooked.add(getOverlap(sb, cur));
        }
        booked.add(cur);
        return true;
    }
}

class MyCalendarTwo {
    TreeMap<Integer, Integer> linesweep = new TreeMap<>();

    public MyCalendarTwo() {
        /*
         * This is the line sweep method. I was thinking about line sweep but
         * ended up not implementing it because it was too complicated to
         * maintain the TreeMap clean. I was essentially maintaining the
         * prefix sum as new intervals are coming in. The official solution,
         * however, does not maintain the prefix sum in the TreeMap. Instead,
         * it just records the line sweep signal and computes the the prefix
         * sum each time the book function is called.
         */
    }
    
    public boolean book(int start, int end) {
        this.linesweep.put(start, this.linesweep.getOrDefault(start, 0) + 1);
        this.linesweep.put(end, this.linesweep.getOrDefault(end, 0) - 1);
        // compute prefix sum
        int psum = 0;
        for (int k : this.linesweep.keySet()) {
            psum += this.linesweep.get(k);
            if (psum == 3) {
                // backtrack
                this.linesweep.put(start, this.linesweep.get(start) - 1);
                this.linesweep.put(end, this.linesweep.get(end) + 1);
                if (this.linesweep.get(start) == 0)
                    this.linesweep.remove(start);
                return false;
            }
        }
        return true;
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
