class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution1 {
    public ListNode partition(ListNode head, int x) {
        /*
        LeetCode 86

        Use two pointers, one on left and the other on right. Whenever a node whose value is larger or equal
        to x is encountered, move that node to right.next. Otherwise, progress left forward.

        The terminal condition is a bit tricky. We use a separate term node to mark the first node that gets
        placed after the original tail. Once the traversal hits that node, we know all the nodes have been
        handled.

        O(N), 0 ms.
         */
        ListNode dummy = new ListNode(0, head);
        ListNode left = dummy;
        ListNode right = head;
        ListNode term = null; // the first node that gets placed after the original tail
        while (right != null && right.next != null) {
            right = right.next;
        }
        ListNode node = head;
        while (node != term && node != right) {
            if (node.val < x) {
                node = node.next;
                left = left.next;
            } else {
                right.next = node;
                left.next = node.next;
                node.next = null;
                node = left.next;
                right = right.next;
                if (term == null) {
                    term = right;
                }
            }
        }
        return dummy.next;
    }
}


class Solution2 {
    public ListNode partition(ListNode head, int x) {
        /*
        Use two dummy heads
         */
        ListNode dummySmall = new ListNode(0, head);
        ListNode preSmall = dummySmall;
        ListNode dummyBig = new ListNode();
        ListNode preBig = dummyBig;
        ListNode node = head;
        while (node != null) {
            if (node.val < x) {
                node = node.next;
                preSmall = preSmall.next;
            } else {
                preBig.next = node;
                preSmall.next = node.next;
                node.next = null;
                node = preSmall.next;
                preBig = preBig.next;
            }
        }
        preSmall.next = dummyBig.next;
        return dummySmall.next;
    }
}
