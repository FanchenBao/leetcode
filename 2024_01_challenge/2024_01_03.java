class Solution {
    public int numberOfBeams(String[] bank) {
        /*
        LeetCode 2125
        
        Just find the count of laser devices on each row and multiply
        that with the count of the next row with laser devices.
        
        O(MN), 16 ms, faster than 32.74%
        */
        int res = 0;
        int pre = 0;
        for (String row : bank) {
            int cur = 0;
            for (char c : row.toCharArray())
                cur += c - '0';
            if (cur > 0) {
                res += pre * cur;
                pre = cur;
            }
        }
        return res;
    }
}

