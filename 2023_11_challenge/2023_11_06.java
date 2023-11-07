class SeatManager {
    /*
    LeetCode 1845
    
    Use priority queue.
    
    78 ms, faster than 59.84%
    */
    PriorityQueue<Integer> unreservedSeats = new PriorityQueue<>();
    public SeatManager(int n) {
        for (int i = 1; i <= n; i++) unreservedSeats.add(i);
    }

    public int reserve() {
        return unreservedSeats.poll();
    }

    public void unreserve(int seatNumber) {
        unreservedSeats.add(seatNumber);
    }
}


/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */


class SeatManager {
    /*
    Without pre-initialization of the unreserved min heap.
    
    32 ms, faster than 76.64%
    */
    PriorityQueue<Integer> unreservedSeats = new PriorityQueue<>();
    int cur;
    
    public SeatManager(int n) {
        cur = 1; 
    }

    public int reserve() {
        if (unreservedSeats.isEmpty() || cur < unreservedSeats.peek())
            return cur++;
        return unreservedSeats.poll();
    }

    public void unreserve(int seatNumber) {
        unreservedSeats.add(seatNumber);
    }
}


/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */