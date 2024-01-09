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


class Solution {
    public int maximumBeauty(int[] nums, int k) {
        /*
        From lee215
        https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/discuss/3771308/JavaC%2B%2BPython-Sliding-Window

        This solution is lethal, absolutely bonkers good. The crazy thing is that I had
        the similar idea, where we find the smallest value, plus 2k on it, and see how far
        we can reach. Except, in my case, I went for binary search to locate the value on
        the right, but with lee215's solution, he used sliding window, which can solve it
        much faster. And since we are lookinf for the longest subsequence, once we find
        a sliding window that satisfies beauty array, we never shrink it, only expand it.
        
        O(NlogN), 37 ms, faster than 88.66% 
         */
        Arrays.sort(nums);
        int i = 0;
        int res = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] > nums[i] + 2 * k)
                i++;
            res = Math.max(res, j - i + 1);
        }
        return res;
    }
}


