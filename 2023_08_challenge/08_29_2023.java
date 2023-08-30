class Solution1 {
    public int bestClosingTime(String customers) {
        /*
        LeetCode 2483

        Sliding window (do we even consider this as sliding window?)

        O(N), 12 ms, faster than 70.71%
         */
        int pl = 0; int pr = 0;
        for (int i = customers.length() - 1; i >= 0; i--) {
            if (customers.charAt(i) == 'Y') {
                pr++;
            }
        }
        int minP = pr; // penalty when closed at 0th hour
        int res = 0; // closed at 0th hour
        for (int i = 1; i <= customers.length(); i++) {
            if (customers.charAt(i - 1) == 'Y') {
                pr--;
            } else {
                pl++;
            }
            if (pr + pl < minP) {
                minP = pr + pl;
                res = i;
            }
        }
        return res;
    }
}


class Solution2 {
    public int bestClosingTime(String customers) {
        /*
        Update from the official solution. There is no need to pre-compute the exact value of pr. We can simply set
        pr to 0. The penalty computed will not be accurate, but its relative value compared against each other is
        correct. And since we are only concerned about the relative values, this will suffice.
        
        O(N), 9 ms, faster than 91.25% 
         */
        int pl = 0; int pr = 0;
        int minP = pr; // penalty when closed at 0th hour
        int res = 0; // closed at 0th hour
        for (int i = 1; i <= customers.length(); i++) {
            if (customers.charAt(i - 1) == 'Y') {
                pr--;
            } else {
                pl++;
            }
            if (pr + pl < minP) {
                minP = pr + pl;
                res = i;
            }
        }
        return res;
    }
}
