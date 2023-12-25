class Solution {
    public int minOperations(String s) {
        /*
        LeetCode 1758
        
        Naive solution, try two ways with the first digit
        being either 1 or 0.
        
        O(N), 4 ms, faster than 74.75%
         */
        int atmpt1 = 0;
        int atmpt2 = 0;
        char exp1 = '1';
        char exp2 = '0';
        for (char c : s.toCharArray()) {
            atmpt1 += c == exp1 ? 0 : 1;
            exp1 = exp1 == '1' ? '0' : '1';
            atmpt2 += c == exp2 ? 0 : 1;
            exp2 = exp2 == '0' ? '1' : '0';
        }
        return Math.min(atmpt1, atmpt2);

    }
}


class Solution {
    public int minOperations(String s) {
        /*
        Use bit to alternate the expected

        O(N), 4 ms, faster than 74.75%
         */
        int atmpt1 = 0;
        int atmpt2 = 0;
        char exp1 = 1;
        char exp2 = 0;
        for (char c : s.toCharArray()) {
            atmpt1 += (c - '0') ^ exp1;
            exp1 ^= 1;
            atmpt2 += (c - '0') ^ exp2;
            exp2 ^= 1;
        }
        return Math.min(atmpt1, atmpt2);
    }
}


class Solution {
    public int minOperations(String s) {
        /*
        Use bit to alternate the expected. And only
        perform one attempt. The number of operations
        of the other attempt is the length of s minus
        the first attempt

        O(N), 3 ms, faster than 92.13%
         */
        int atmpt = 0;
        char exp = 1;
        for (char c : s.toCharArray()) {
            atmpt += (c - '0') ^ exp;
            exp ^= 1;
        }
        return Math.min(atmpt, s.length() - atmpt);
    }
}

