class Solution {
    public int maximumBeauty(int[] nums, int k) {
        /*
        LeetCode 2779
        
        The problem is equivalent to asking what is the max
        number of overlaps among the ranges. Thus We produce
        all the ranges and sort them. And then we go through
        each extremes. If we hit a start, we increment the count,
        otherwise, we decrement.
        
        Return the max such count. O(NlogN), 300 ms, faster than 6.32%
        
        Based on the performance, this is apparently NOT the best
        solution.
        */
        int[][] extremes = new int[nums.length * 2][2];
        for (int i = 0; i < nums.length; i++) {
            extremes[2 * i][0] = nums[i] - k; // start
            extremes[2 * i][1] = -1; // indicating start
            extremes[2 * i + 1][0] = nums[i] + k; // end
            extremes[2 * i + 1][1] = 1; // indicating the end
        }
        Arrays.sort(
                extremes,
                (tup1, tup2) -> tup1[0] == tup2[0] ? Integer.compare(tup1[1], tup2[1]) : Integer.compare(tup1[0], tup2[0])
        );
        int res = 0;
        int cur = 0;
        for (int[] tup : extremes) {
            cur -= tup[1];
            res = Math.max(res, cur);
        }
        return res;

    }
}


class Solution {
    
    private int bisectRight(int[] arr, int x) {
        int lo = 0; int hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid] <= x)
                lo = mid + 1;
            else 
                hi = mid;
        }
        return lo;
    }
    
    public int maximumBeauty(int[] nums, int k) {
        /*
        Use binary search. We sort nums first. Then a key
        observation is that the longest subsequence of
        equal elements must come from a subarray of the
        sorted nums. This is because if we skip some
        number, then the skipped number can always be
        part of the beautiful numbers.

        Then we check each number in the sorted array, and
        use binary search to find the position of n + 2k.
        Any value in the sorted array that is smaller than
        n + 2k can be included in the beautiful array.
        
        O(NlogN), 84 ms, faster than 13.68%
         */
        Arrays.sort(nums);
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            res = Math.max(res, bisectRight(nums, nums[i] + 2 * k) - i);
        }
        return res;
    }
}

class Solution {    
    public int maximumBeauty(int[] nums, int k) {
        /*
        Use binary search. We sort nums first. Then a key
        observation is that the longest subsequence of
        equal elements must come from a subarray of the
        sorted nums. This is because if we skip some
        number, then the skipped number can always be
        part of the beautiful numbers.
        
        Then we check each number in the sorted array, and
        use binary search to find the position of n + 2k.
        Any value in the sorted array that is smaller than
        n + 2k can be included in the beautiful array.
        
        Note that we need to use a trick to obtain bisect_right
        with java's binary search. Need to convert the nums to
        a double array.
        
        O(NlogN), 64 ms, faster than 26.32%
         */
        Arrays.sort(nums);
        double[] fnums = new double[nums.length];
        for (int i = 0; i < nums.length; i++) fnums[i] = (double)nums[i];
        int res = 0;
        for (int i = 0; i < fnums.length; i++) {
            int j = Arrays.binarySearch(fnums, fnums[i] + 2 * k + 0.1);
            if (j < 0)
                j = -(j + 1);
            res = Math.max(res, j - i);
        }
        return res;
    }
}
