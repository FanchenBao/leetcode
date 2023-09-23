class Solution1 {
    private double getMedian(int[] nums) {
        if (nums.length % 2 == 1) {
            return nums[nums.length / 2];
        }
        return (nums[nums.length / 2] + nums[nums.length / 2 - 1]) / 2.0;
    }

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        /*
        LeetCode 4

        This is the dumb solution. O(N), not the required O(log(MN))
        */
        int[] merged = new int[nums1.length + nums2.length];
        int i = 0; int j = 0; int k = 0;
        while (i < nums1.length && j < nums2.length) merged[k++] = nums1[i] <= nums2[j] ? nums1[i++] : nums2[j++];
        while (i < nums1.length) merged[k++] = nums1[i++];
        while (j < nums2.length) merged[k++] = nums2[j++];
        return getMedian(merged);
    }
}


class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        /*
        This is the official binary search solution.

        We use two partition points. i for nums1, and j for nums2, such that i + j = (len(nums1) + len(nums2)) / 2
        Then, nums1[i - 1], nums1[i], nums2[j - 1], and nums2[j] becomes the four values surrounding the median point
        when nums1[i - 1] <= nums2[j] and nums2[j - 1] <= nums1[i]. If either does not match, we move i accordingly and
        subsequently, j will move as well.

        Eventually we will arrive at the proper i and j positions, and from there, we can compute the median.

        One trick is that we make nums1 always the shorter of the two arrays, such that the runtime can be optimized.
        
        O(log(min(M, N))), 1 ms, faster than 100.00% 
         */
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int half = (nums1.length + nums2.length) / 2;
        boolean isOdd = (nums1.length + nums2.length) % 2 == 1;
        int i; int j;
        int maxLeft1; int minRight1; int maxLeft2; int minRight2;
        int lo = 0; int hi = nums1.length + 1;
        while (lo <= hi) {
            i = (lo + hi) / 2; j = half - i;
            // These four statements are very tricky to get right.
            maxLeft1 = i == 0 ? Integer.MIN_VALUE : nums1[i - 1];
            minRight1 = i == nums1.length ? Integer.MAX_VALUE : nums1[i];
            maxLeft2 = j == 0 ? Integer.MIN_VALUE : nums2[j - 1];
            minRight2 = j == nums2.length ? Integer.MAX_VALUE : nums2[j];
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                if (isOdd) {
                    return Math.min(minRight1, minRight2);
                } else {
                    return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2.0;
                }
            } else if (maxLeft1 > minRight2) {
                hi = i - 1;
            } else {
                lo = i + 1;
            }
        }
        return 0.0; // we shall not reach here.
    }
}
