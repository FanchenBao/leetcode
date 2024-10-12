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

class Solution1 {
    public int smallestChair(int[][] times, int targetFriend) {
        /*
         * LeetCode 1942
         *
         * First sort times based on start, then use two priority queues. One
         * of them tracks the available seats. The other tracks the leaving
         * time and seat of someone who's currently occupying a seat. When a
         * new arrival happens, we check the leavings priority queue to pop
         * any people who's leaving time is not bigger than the current start.
         * Their seats will be recycled in the seats priority queue. And the
         * current person will take the smallest available seat in the seats
         * priority queue.
         *
         * O(NlogN), 55 ms, faster than 42.10%
         *
         * Update: since arrival time is unique, we don't have to create a new
         * array to keep track of the friend index. We can use the arrival
         * time of the targetFriend as the signal.
         *
         * 51 ms, faster than 51.46%
         */
        int N = times.length;
        int targetArrival = times[targetFriend][0];
        Arrays.sort(times, (a, b) -> Integer.compare(a[0], b[0]));
        PriorityQueue<int[]> leavings = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0])); // [time to leave, seat index]
        PriorityQueue<Integer> seats = new PriorityQueue<>((a, b) -> Integer.compare(a, b));
        for (int i = 0; i < N; i++)
            seats.add(i);
        for (int[] ele : times) {
            while (!leavings.isEmpty() && leavings.peek()[0] <= ele[0])
                seats.add(leavings.poll()[1]);
            int seat = seats.poll();
            if (ele[0] == targetArrival)
                return seat;
            leavings.add(new int[]{ele[1], seat});
        }
        return -1; // should not reach here.
    }
}


class Solution {
    public int smallestChair(int[][] times, int targetFriend) {
        /*
         * This is from the official solution which uses a TreeSet to keep
         * track of the unused chairs and a priority queue to keep track of
         * the leaving time. It is essentially the same solution, but we
         * replace one priority queue with a TreeSet. I am not sure about the
         * overhead of these two data structures, but I am sure that with
         * TreeSet, we don't have to pre-populate the max number of chairs.
         * So this solution is very likely faster.
         *
         * O(NlogN) 36 ms, faster than 92.98%
         *
         * That is A LOT faster than I had expected. I am pretty sure the savings
         * happen at the step of not having to pre-populate the chairs.
         */
        int targetArrival = times[targetFriend][0];
        Arrays.sort(times, (a, b) -> Integer.compare(a[0], b[0]));
        PriorityQueue<int[]> leavings = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0])); // [time to leave, seat index]
        TreeSet<Integer> seats = new TreeSet<>();
        int nextSeat = 0;
        for (int[] ele : times) {
            while (!leavings.isEmpty() && leavings.peek()[0] <= ele[0])
                seats.add(leavings.poll()[1]);
            int seat = seats.isEmpty() ? nextSeat++ : seats.pollFirst();
            if (ele[0] == targetArrival)
                return seat;
            leavings.add(new int[]{ele[1], seat});
        }
        return -1; // should not reach here.
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
