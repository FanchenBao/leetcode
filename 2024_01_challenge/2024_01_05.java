class Solution {
    public int lengthOfLIS(int[] nums) {
        /*
        LeetCode 300 (Fail)
        
        This is the seventth time I have solved this problem, but yet again
        I was not able to come up with the O(NlogN) solution. I knew that
        the trick is to form some sorted order and then binary search.
        But I forgot what sorted order it is. I thought it was a monotonic
        array, but that didn't work. It never occurred to me that the sorted
        order is a version of the longest increasing subsequence.
        
        Each time we replace some value in the LIS with a better option. This
        will not affect the actual length of LIS so far, but it provides a
        potential to extend LIS even further, because the value replaced is
        always smaller than the original value at the same position of the
        LIS.
        
        O(NlogN), 6 ms, faster than 84.81% 
        */
        List<Integer> lis = new ArrayList<>();
        for (int n : nums) {
            int idx = Collections.binarySearch(lis, n);
            if (idx < 0) {
                idx = -(idx + 1);
                if (idx == lis.size())
                    lis.add(n);
                else
                    lis.set(idx, n);
            }
        }
        return lis.size();
    }
}

