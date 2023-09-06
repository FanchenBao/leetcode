// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

class Solution1 {
    public Node copyRandomList(Node head) {
        /*
        LeetCode 138

        Create a hashmap between the original node and its copy. Two passes.
        O(N), 0 ms, faster than 100.00%
         */
        if (head == null) {
            return null;
        }
        HashMap<Integer, Node> oriCopyMap = new HashMap<>();
        Node ori = head;
        Node copy = new Node(head.val);
        // Copy the list
        while (ori != null) {
            oriCopyMap.put(System.identityHashCode(ori), copy);
            if (ori.next != null) {
                copy.next = new Node(ori.next.val);
            }
            ori = ori.next;
            copy = copy.next;
        }
        // Fill out the random pointers
        ori = head;
        while (ori != null) {
            copy = oriCopyMap.get(System.identityHashCode(ori));
            if (ori.random != null) {
                copy.random = oriCopyMap.get(System.identityHashCode(ori.random));
            }
            ori = ori.next;
        }
        return oriCopyMap.get(System.identityHashCode((head)));
    }
}


class Solution2 {
    public Node copyRandomList(Node head) {
        /*
        This is the O(1) extra space method. We put each copy node right next to the original one. This way, we can
        easily map the nodes during the establishment of random pointers

        0 ms, faster than 100.00%
         */
        if (head == null) {
            return null;
        }
        Node ori = head;
        Node tmp;
        // insert the copy nodes
        while (ori != null) {
            tmp = ori.next;
            ori.next = new Node(ori.val);
            ori.next.next = tmp;
            ori = tmp;
        }
        // Fill out the random pointers
        ori = head;
        while (ori != null) {
            if (ori.random != null) {
                ori.next.random = ori.random.next;
            }
            ori = ori.next.next;
        }
        // Split out the copy nodes
        Node copyHead = head.next;
        Node cur = copyHead;
        Node pre = head;
        while (cur.next != null) {
            pre.next = cur.next;
            cur.next = cur.next.next;
            pre = pre.next;
            cur = cur.next;
        }
        pre.next = null;
        return copyHead;
    }
}

