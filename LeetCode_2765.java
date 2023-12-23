class Solution {
    public int alternatingSubarray(int[] nums) {
        /*
        Not a big fan of this solution. Convoluted.
        
        1 ms, faster than 100.00%
         */
        int res = 0;
        int pre = 0;
        int len = 0;
        for (int i = 1; i < nums.length; i++) {
            int cur = nums[i] - nums[i - 1];
            if (cur == 1) {
                if (pre == -1) {
                    len++;
                }
                else {
                    res = Math.max(res, len);
                    len = 2;
                }
            } else if (cur == -1) {
                if (pre == 1) {
                    len++;
                }
                else {
                    res = Math.max(res, len);
                    len = 0;
                    cur = 0; // we cannot use -1 as the cur, because it does not represent a valid subarray
                }
            } else {
                res = Math.max(res, len);
                len = 0;
            }
            pre = cur;
        }
        res = Math.max(res, len);
        return res == 0 ? -1 : res;
    }
}


class Solution {
    public int alternatingSubarray(int[] nums) {
        /*
        Try two pointers

        1 ms, faster than 100.00%
         */
        int res = 0;
        int i = 1;
        while (i < nums.length) {
            if (nums[i] - nums[i - 1] == 1) {
                int j = i - 1; // starting point
                i++;
                while (i < nums.length && nums[i] == nums[i - 2])
                    i++;
                res = Math.max(res, i - j);
            } else {
                i++;
            }
        }
        return res == 0 ? -1 : res;
    }
}

