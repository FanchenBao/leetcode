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

