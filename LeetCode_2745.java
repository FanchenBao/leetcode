class Solution {
    public int longestString(int x, int y, int z) {
        /*
        AB can form with itself indefinitely.
        
        AA and BB can alternate indefinitely.
        
        AB can always attach to the end of a BB or the front of AA.
        
        Thus the problem is equivalent to asking how many AA and BB
        can we form. This depends on whether x == y. If they are
        equal, we can alternate all of them. Otherwise, we can alternate
        with the smaller of x or y, and then add one more pair.
        
        O(1), 1 ms, faster than 100.00%
        */
        return 2 * (Math.min(x, y) * 2 + z + (x == y ? 0 : 1));
    }
}