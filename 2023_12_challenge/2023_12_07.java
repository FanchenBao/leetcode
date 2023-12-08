class Solution {
    public String largestOddNumber(String num) {
        /*
        LeetCode 1903
        
        Go from right to left and find the first digit that is odd. The largest
        odd number starts from the front and ends at that first odd digit.
        
        O(N), 1 ms, faster than 100.00%
         */
       int i = num.length() - 1;
       while (i >= 0 && ((num.charAt(i) - '0') & 1) == 0)
           i--;
       return i < 0 ? "" : num.substring(0, i + 1);
    }
}
