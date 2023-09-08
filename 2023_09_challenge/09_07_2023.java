/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        /*
        LeetCode 92
        
        Use a dummy node at the start. Find the node before the first of the
        reversed stretch, perform the reversal, and reconnect.
        
        O(N), 0 ms, faster than 100.00% 
        */
        ListNode dummy = new ListNode(0, head);
        ListNode start = dummy;
        for (int i = 1; i < left; i++) {
            start = start.next;
        }
        ListNode pre = start;
        ListNode cur = start.next;
        for (int i = left; i <= right; i++) {
            ListNode tmp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = tmp;
        }
        start.next.next = cur;
        start.next = pre;
        return dummy.next;
    }
}
