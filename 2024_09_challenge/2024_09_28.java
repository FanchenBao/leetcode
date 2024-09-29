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

class MyCircularDeque1 {
    int[] deque;
    int f = -1;
    int e = -1;
    int k;

    public MyCircularDeque1(int k) {
        /*
         * LeetCode 641
         *
         * Use a single array and some manipulation of two pointers.
         *
         * 4 ms, faster than 100.00%
         */
        this.deque = new int[k];
        this.k = k;
    }
    
    public boolean insertFront(int value) {
        if (isEmpty()) {
            this.f = 0;
            this.e = 0;
            this.deque[this.f] = value;
            return true;
        }
        if (isFull())
            return false;
        this.f = (this.f - 1 + this.k) % this.k;
        this.deque[this.f] = value;
        return true;
    }
    
    public boolean insertLast(int value) {
        if (isEmpty()) {
            this.f = 0;
            this.e = 0;
            this.deque[this.e] = value;
            return true;
        }
        if (isFull())
            return false;
        this.e = (this.e + 1) % this.k;
        this.deque[this.e] = value;
        return true;
    }
    
    public boolean deleteFront() {
        if (isEmpty())
            return false;
        if (this.f == this.e) {
            this.f = -1;
            this.e = -1;
        } else {
            f = (f + 1) % this.k;
        }
        return true;
    }
    
    public boolean deleteLast() {
        if (isEmpty())
            return false;
        if (this.f == this.e) {
            this.f = -1;
            this.e = -1;
        } else {
            this.e = (this.e - 1 + this.k) % this.k;
        }
        return true;
    }
    
    public int getFront() {
        if (isEmpty())    
            return -1;
        return this.deque[this.f];
    }
    
    public int getRear() {
        if (isEmpty())
            return -1;
        return this.deque[this.e];
    }
    
    public boolean isEmpty() {
        return this.f == -1 && this.e == -1;
    }
    
    public boolean isFull() {
        return (this.f - this.e + this.k) % this.k == 1;
    }
}


class MyCircularDeque {
    int[] deque;
    // f and e points to the next available front and end position
    int f = 0;
    int e = 1;
    int k;

    public MyCircularDeque(int k) {
        /*
         * Better implementation
         
         * Note the requirement of setting the deque size to k + 1,
         * because we f and e pointing to the next available front
         * end, which means when f and e meet other, the deque is full.
         * In this case, we have len(deque) - 1 available spots. Thus
         * the deque itself must be of size k + 1.
         */
        this.deque = new int[k + 1];
        this.k = k + 1;
    }
    
    public boolean insertFront(int value) {
        if (isFull())
            return false;
        this.deque[this.f] = value;
        this.f = (this.f - 1 + this.k) % this.k;
        return true;
    }
    
    public boolean insertLast(int value) {
        if (isFull())
            return false;
        this.deque[this.e] = value;
        this.e = (this.e + 1) % this.k;
        return true;
    }
    
    public boolean deleteFront() {
        if (isEmpty())
            return false;
        this.f = (this.f + 1) % this.k;
        return true;
    }
    
    public boolean deleteLast() {
        if (isEmpty())
            return false;
        this.e = (this.e - 1 + this.k) % this.k;
        return true;
    }
    
    public int getFront() {
        if (isEmpty())    
            return -1;
        return this.deque[(this.f + 1) % this.k];
    }
    
    public int getRear() {
        if (isEmpty())
            return -1;
        return this.deque[(this.e - 1 + this.k) % this.k];
    }
    
    public boolean isEmpty() {
        return (this.f + 1) % this.k == this.e;
    }
    
    public boolean isFull() {
        return this.f == this.e;
    }
}






/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 *//**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */

class Main{
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
