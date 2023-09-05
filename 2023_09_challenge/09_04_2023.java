public class Solution {
    public boolean hasCycle(ListNode head) {
        /*
        LeetCode 141

        Hare and tortoise.

        0 ms, faster than 100.00% 
        */
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
}