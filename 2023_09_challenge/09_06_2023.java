class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    private ListNode take(ListNode head, int cnt) {
        ListNode node = head;
        while (--cnt > 0) {
            node = node.next;
        }
        if (node == null) {
            return null;
        }
        ListNode nextHead = node.next;
        node.next = null;
        return nextHead;
    }

    private int length(ListNode head) {
        int len = 0;
        ListNode node = head;
        while (node != null){
            len++;
            node = node.next;
        }
        return len;
    }

    public ListNode[] splitListToParts(ListNode head, int k) {
        /*
        LeetCode 725
        
        First count the length of the linked list. Then we can find the size of the bigger length and the smaller length.
        Suppose the length is l, we have q = l / k and r = l % k. The bigger length is q + 1, and the smaller length is
        q. There are r number of bigger length and k - r number of smaller length.
        
        The rest is just implementation.
        
        O(N) 0 ms, faster than 100.00%
         */
        int len = length(head);
        int small = len / k; int r = len % k;
        ListNode[] res = new ListNode[k];
        ListNode node = head;
        for (int i = 0; i < k; i++) {
            res[i] = node;
            node = take(node, i < r ? small + 1 : small);
        }
        return res;
    }
}
