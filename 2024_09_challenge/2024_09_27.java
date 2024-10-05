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

class MyCalendarTwo {
    TreeMap<Integer, Integer> linesweep = new TreeMap<>();

    public MyCalendarTwo() {
        
    }
    
    public boolean book(int start, int end) {
       // first dry run
        System.out.println(String.format("start=%d, end=%d", start, end));
        for (int k : this.linesweep.keySet()) {
            System.out.println(String.format("k=%d, line=%d", k, this.linesweep.get(k)));
        }
        
       for (int k : this.linesweep.keySet()) {
           if (k >= start && k < end && this.linesweep.get(k) == 2)
               return false;
       }
       // update
       for (int k : this.linesweep.keySet()) {
           if (k >= start && k < end)
               this.linesweep.put(k, this.linesweep.get(k) + 1);
           else if (k >= end)
               break;
       }
       if (start < this.linesweep.firstKey() || start > this.linesweep.lastKey()) {
            this.linesweep.put(start, 1);
       } else if (!this.linesweep.containsKey(start)) {
            int before = this.linesweep.floorKey(start);
            this.linesweep.put(start)
       }
       // if (!this.linesweep.containsKey(start))
       //     this.linesweep.put(start, 1);
       // if (!this.linesweep.containsKey(end))
       //     this.linesweep.put(end, this.linesweep.get(beforeEnd) - 1);
       //  else if (this.linesweep.get(beforeEnd) == this.linesweep.get(end))
       //      this.linesweep.remove(end);
       return true;
    }
}


/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(start,end);
 */
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
