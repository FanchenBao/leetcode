class Solution {
    public int maxScore(String s) {
        /*
        LeetCode 1422
        
        O(N), 1 ms, faster than 97.78%
         */
        int left = 0;
        int right = 0;
        for (int i = 0; i < s.length(); i++)
            right += s.charAt(i) == '1' ? 1 : 0;
        int res = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i - 1) == '0')
                left += 1;
            else
                right -= 1;
            res = Math.max(res, left + right);
        }
        return res;
    }
}


class Solution {
    public int maxScore(String s) {
        /*
        This is the one-pass solution from the official solution.

        The key idea is that we can convert the score from
        num_zero_left + num_one_right to
        num_zero_left + total_one - num_one_left

        Thus, we can do one pass and keep track of the number of
        ones and zeros on the left and find the max of
        num_zero_left - num_one_left.

        At the end, we find the total_one and we will have the
        answer. One trick is that as we iterat through the string
        to find num_zero_left and num_one_left, we do NOT iterate
        the entire string, because wherever the index lands, it
        will be the end of the left substring. And since we cannot
        have an empty right substring, the iteration must terminate
        before the last element.
         */
        int ones = 0; int zeroes = 0;
        int res = Integer.MIN_VALUE;
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == '0')
                zeroes++;
            else
                ones++;
            res = Math.max(res, zeroes - ones);
        }
        if (s.charAt(s.length() - 1) == '1')
            ones++;
        return res + ones;
    }
}


