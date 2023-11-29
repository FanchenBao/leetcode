class Solution {
    public int numberOfWays(String corridor) {
        /*
        LeetCode 2147
        
        Since each room must have exactly two seats, any consecutive two seats cannot have
        any divider in between them. Thus, we can iterate from left to right and ignore all
        the spaces between consecutive seats. Further, we compute the number of possible
        positions between two pairs of seats. These are the positions where one divider
        can be placed. The result is the multiplication of all these number of possible
        positions.
        
        Also, if the count of seats is odd, the answer is zero.
        
        O(N), 20 ms, faster than 97.37%
         */
        int count = 0;
        int preIdx = -1;
        long res = 1;
        int MOD = 1000000007;
        for (int i = 0; i < corridor.length(); i++) {
            if (corridor.charAt(i) == 'S') {
                if (count == 2) {
                    res = (res * (i - preIdx)) % MOD;
                    count = 0;
                }
                count++;
                preIdx = i;
            }
        }
        return count == 2 ? (int)res : 0;
    }
}
