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

// class PQEle {
//     String key;
//     int cnt;
//
//     PQEle(String key, int cnt) {
//         this.key = key;
//         this.cnt = cnt;
//     }
// }
//
// class AllOne {
//     Map<String, Integer> counter = new HashMap<>();
//     PriorityQueue<PQEle> maxQ = new PriorityQueue<>((a, b) -> Integer.compare(b.cnt, a.cnt));
//     PriorityQueue<PQEle> minQ = new PriorityQueue<>((a, b) -> Integer.compare(a.cnt, b.cnt));
//
//     public AllOne() {
//         /*
//          * LeetCode 432
//          *
//          * Naive solution using priority queue to find the key with max or min
//          * counts. The complexity of getMaxKey() and getMinKey() can be O(NlogN)
//          * where N is the number of inc or dec calls made on the same key
//          *
//          * 56 ms, faster than 38.79%
//          */
//         
//     }
//     
//     public void inc(String key) {
//         this.counter.put(key, this.counter.getOrDefault(key, 0) + 1);
//         this.maxQ.add(new PQEle(key, this.counter.get(key)));
//         this.minQ.add(new PQEle(key, this.counter.get(key)));
//     }
//     
//     public void dec(String key) {
//         this.counter.put(key, this.counter.get(key) - 1);
//         if (this.counter.get(key) > 0) {
//             this.maxQ.add(new PQEle(key, this.counter.get(key)));
//             this.minQ.add(new PQEle(key, this.counter.get(key)));
//         }
//     }
//     
//     public String getMaxKey() {
//         while (!this.maxQ.isEmpty()) {
//             PQEle top = this.maxQ.peek();
//             if (top.cnt != this.counter.get(top.key))
//                 this.maxQ.poll();
//             else
//                 return top.key;
//         }
//         return "";
//     }
//     
//     public String getMinKey() {
//         while (!this.minQ.isEmpty()) {
//             PQEle top = this.minQ.peek();
//             if (top.cnt != this.counter.get(top.key))
//                 this.minQ.poll();
//             else
//                 return top.key;
//         }
//         return "";
//     }
// }
//
class Node {
    int cnt;
    Set<String> keys = new HashSet<>();
    Node prev;
    Node next;

    Node(int cnt) {
        this.cnt = cnt;
    }
}

class AllOne {
    Node head;
    Node tail;
    Map<String, Node> keyToNode;

    public AllOne() {
        /*
         * This solution uses the official solution's doubly-linked list. The
         * genious part is that we use the doubly-linked list to keep the
         * counts of all keys in sorted order. This works because each time
         * a count changes, it only changes by one unit. In the doubly-linked
         * list, this means moving the key either to its current node's parent
         * or descendant. The min and max count value can be easily obtained
         * by accessing the first and last node.
         *
         * This works for this problem because the change to the count is
         * restricted to only one unit. If the change can be an arbitrary value
         * the doubly-linked list method will not work.
         *
         * 50 ms, faster than 85.57%
         */
        this.head = new Node(0);
        this.tail = new Node(0);
        this.head.next = this.tail;
        this.tail.prev = this.head;
        this.keyToNode = new HashMap<>();
    }

    private void delete(Node node) {
        Node prevNode = node.prev;
        Node nextNode = node.next;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
        node.prev = null;
        node.next = null;
    }
    
    private Node add(Node cur, int cnt) {
        Node newNode = new Node(cnt);
        if (cnt > cur.cnt) {
            Node nextNode = cur.next;
            cur.next = newNode;
            newNode.prev = cur;
            newNode.next = nextNode;
            nextNode.prev = newNode;
        } else {
            Node prevNode = cur.prev;
            prevNode.next = newNode;
            newNode.prev = prevNode;
            cur.prev = newNode;
            newNode.next = cur;
        }
        return newNode;
    }
    
    public void inc(String key) {
        if (this.keyToNode.containsKey(key)) {
            Node node = this.keyToNode.get(key);
            Node nextNode = node.next.cnt == node.cnt + 1 ? node.next : add(node, node.cnt + 1);
            nextNode.keys.add(key);
            this.keyToNode.put(key, nextNode);
            node.keys.remove(key);
            if (node.keys.isEmpty())
                delete(node);
        } else {
            Node node = this.head.next.cnt != 1 ? add(this.head, 1) : this.head.next;
            node.keys.add(key);
            this.keyToNode.put(key, node);
        }
    }
    
    public void dec(String key) {
        Node node = this.keyToNode.get(key);
        Node prevNode = node.prev.cnt == node.cnt - 1 ? node.prev : add(node, node.cnt - 1);
        if (prevNode == this.head) {
            this.keyToNode.remove(key);
        } else {
            prevNode.keys.add(key);
            this.keyToNode.put(key, prevNode);
        }
        node.keys.remove(key);
        if (node.keys.isEmpty())
            delete(node);
    }
    
    public String getMaxKey() {
        if (this.tail.prev == this.head)
            return "";
        return this.tail.prev.keys.iterator().next();  // use iterator to get any element from a set in O(1) time
    }
    
    public String getMinKey() {
        if (this.head.next == this.tail)
            return "";
        return this.head.next.keys.iterator().next();  // use iterator to get any element from a set in O(1) time

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
