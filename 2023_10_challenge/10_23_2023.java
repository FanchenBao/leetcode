class Solution {
    public boolean isPowerOfFour(int n) {
        /*
        LeetCode 342
        
        This uses recursion.
         */
        if (n == 1) return true;
        if (n <= 0 || n % 4 != 0) return false;
        return isPowerOfFour(n / 4);
    }
}


class Solution {
    public boolean isPowerOfFour(int n) {
        /*
        LeetCode 342

        Binary version of n if n is power of 4 must have a leading 1 and even number
        of trailing zeros.
         */
        if (n <= 0) return false;
        String bin = Integer.toBinaryString(n);
        return bin.length() % 2 == 1 && (n & (n - 1)) == 0;
    }
}
