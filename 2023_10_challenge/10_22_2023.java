class Solution {
    public int maximumScore(int[] nums, int k) {
        /*
        LeetCode 1793

        Build a suffix min array to the left of k and a prefix min array to the right of k. Then use two pointers, one
        at the front and the other at the end of the prefix-suffix min array.

        We start from the overall min of nums with the longest length. That gives us one candidate for a score. Then
        we must find the next smallest value with the longest possible length. We do that by shrinking the prefix-
        suffix min array on the side where a previous min has been taken. The shrinking also skips all the identical
        values as the previous min. We stop the shrinking until a different min is found or we have crossed the
        threshold of k.

        Keep doing this either on the left or right side until the entire prefix-suffix min array has been consumed.

        O(N) time, O(N) space; 4 ms, faster than 95.37%
         */
        int[] mins = new int[nums.length];
        mins[k] = nums[k];
        for (int i = k - 1; i >= 0; i--) mins[i] = Math.min(nums[i], mins[i + 1]);
        for (int j = k + 1; j < nums.length; j++) mins[j] = Math.min(nums[j], mins[j - 1]);
        int i = 0; int j = nums.length - 1;
        int res = 0;
        while (i <= k && j >= k) {
            if (mins[i] <= mins[j]) {
                res = Math.max(res, mins[i] * (j - i + 1));
                i++;
                while (i <= k && mins[i] == mins[i - 1]) i++;
            } else if (mins[j] < mins[i]) {
                res = Math.max(res, mins[j] * (j - i + 1));
                j--;
                while (j >= k && mins[j] == mins[j + 1]) j--;
            } else {
                res = Math.max(res, mins[i] * (j - i + 1));
                i++; j--;
                while (i <= k && mins[i] == mins[i - 1]) i++;
                while (j >= k && mins[j] == mins[j + 1]) j--;
            }
        }
        return res;
    }
}


class Solution {
    public int maximumScore(int[] nums, int k) {
        /*
        Monotonic stack approach from the second solution of the official solution.

        The idea is that we go through nums one by one and designate each nums[i] as the current smallest value of the
        potential good array. Now the question is to find out what is the longest version of such good array. This
        problem can be written in another way as to find the first value smaller than nums[i] on the left, and the first
        value smaller than nums[i] on the right. Then the subarray in between is a good array with nums[i] as its min.
        We will have the length of the good array as well.

        To find the first value smaller than nums[i] on the left and right, we can use monotonic stack. Suppose we are
        doing a monotonic increasing stack. Then the first time a smaller value is encountered, all the bigger ones
        currently in the stack must be popped. As they are popped, they can record the smaller value as the first value
        smaller than itself on the right.
        
        O(N), 131 ms, faster than 33.33%
         */
        int[] left = new int[nums.length];  // left[i] is the index of the first value ≤ nums[i] on the left
        Arrays.fill(left, -1);
        int[] right = new int[nums.length];  // right[i] is the index of the first value ≤ nums[i] on the right
        Arrays.fill(right, nums.length);
        Stack<Integer> mon = new Stack<>();
        for (int i = 0; i < nums.length; i++) {
            while (!mon.isEmpty() && nums[mon.peek()] > nums[i]) right[mon.pop()] = i;
            mon.push(i);
        }
        mon.clear();
        for (int j = nums.length - 1; j >= 0; j--) {
            while (!mon.isEmpty() && nums[mon.peek()] > nums[j]) left[mon.pop()] = j;
            mon.push(j);
        }
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (left[i] < k && right[i] > k) res = Math.max(res, nums[i] * (right[i] - left[i] - 1));
        }
        return res;
    }
}


class Solution {
    public int maximumScore(int[] nums, int k) {
        /*
        Greedy.

        This is the third method from the official solution. Its idea is to start from nums[k] going either left or
        right. Each time, we include the larger one, because by doing so, we are increasing the chance of elongating
        the subarray while not decreasing the min value too much. The official solution has a proof for that. Simply
        put, if we choose not to go with the larger value, then we have to go with the smaller value. In that case,
        going with the larger value in the next round will NOT affect the overall min, yet we can extend the length even
        further. Thus, going with the larger value is always the optimal choice.

        O(N), 5 ms, faster than 94.44%
         */
        int res = nums[k]; int curMin = nums[k];
        int i = k - 1; int j = k + 1;
        while (true) {
            if (i >= 0 && j < nums.length) {
                if (nums[i] >= nums[j]) {
                    curMin = Math.min(curMin, nums[i]); i--;
                    res = Math.max(res, curMin * (j - i - 1));
                } else {
                    curMin = Math.min(curMin, nums[j]); j++;
                    res = Math.max(res, curMin * (j - i - 1));
                }
            } else if (i >= 0) {
                curMin = Math.min(curMin, nums[i]); i--;
                res = Math.max(res, curMin * (j - i - 1));
            } else if (j < nums.length) {
                curMin = Math.min(curMin, nums[j]); j++;
                res = Math.max(res, curMin * (j - i - 1));
            } else break;
        }
        return res;
    }
}


class Solution {
    public int maximumScore(int[] nums, int k) {
        /*
        Greedy.

        This is the third method from the official solution. Its idea is to start from nums[k] going either left or
        right. Each time, we include the larger one, because by doing so, we are increasing the chance of elongating
        the subarray while not decreasing the min value too much. The official solution has a proof for that. Simply
        put, if we choose not to go with the larger value, then we have to go with the smaller value. In that case,
        going with the larger value in the next round will NOT affect the overall min, yet we can extend the length even
        further. Thus, going with the larger value is always the optimal choice.

        O(N), 5 ms, faster than 94.44%
         */
        int res = nums[k]; int curMin = nums[k];
        int i = k - 1; int j = k + 1;
        while (i >= 0 || j < nums.length) {
            if ((i >= 0 ? nums[i] : 0) >= (j < nums.length ? nums[j] : 0)) {
                curMin = Math.min(curMin, nums[i]); i--;
            } else {
                curMin = Math.min(curMin, nums[j]); j++;
            }
            res = Math.max(res, curMin * (j - i - 1));
        }
        return res;
    }
}


class Solution {
    public int maximumScore(int[] nums, int k) {
        /*
        LeetCode 1793

        Build a suffix min array to the left of k and a prefix min array to
        the right of k. Then use two pointers, one at the front and the other
        at the end of the prefix-suffix min array.

        We start from the overall min of nums with the longest length. That
        gives us one candidate for a score. Then we must find the next smallest
        value with the longest possible length. We do that by shrinking the
        prefix-suffix min array on the side where a previous min has been taken.
        If both ends of the prefix-suffix min array are the same, we can pick
        either end to shrink.

        Keep doing this until the entire prefix-suffix min array has been
        consumed.

        O(N) time, O(N) space
         */
        int[] mins = new int[nums.length];
        mins[k] = nums[k];
        for (int i = k - 1; i >= 0; i--) mins[i] = Math.min(nums[i], mins[i + 1]);
        for (int j = k + 1; j < nums.length; j++) mins[j] = Math.min(nums[j], mins[j - 1]);
        int i = 0; int j = nums.length - 1;
        int res = 0;
        while (i <= k && j >= k) {
            res = Math.max(res, Math.min(mins[i], mins[j]) * (j - i + 1));
            mins[i] <= mins[j] ? i++ : j--;
        }
        return res;
    }
}