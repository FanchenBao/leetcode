class Solution {
    public int findDuplicate(int[] nums) {
        /*
        LeetCode 287

        Naive solution. Sort.
        O(NlogN), 35 ms, faster than 18.10%
        */
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                return nums[i];
            }
        }
        return -1;
    }
}


class Solution {
    
    private void swap(int i, int j, int[] arr) {
        int tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
    }
    
    public int findDuplicate(int[] nums) {
        /*
        O(N), with swaps. But we modify the array

        6 ms, faster than 52.22%
        */
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] != i + 1) {
                if (nums[i] != nums[nums[i] - 1]) {
                    swap(i, nums[i] - 1, nums);
                } else {
                    return nums[i];    
                }
                
            }
        }
        return -1;
    }
}


class Solution {
    public int findDuplicate(int[] nums) {
        /*
        I remember this one is hare and tortoise, but I couldn't figure out the reasoning behind it. Turns out I
        was wrong regarding how indices work in nums. nums contains 1 to n. nums is of length n + 1, so its indices are
        0 to n. If we start from nums[0] and then traverse the entire nums using the indices as the next node,
        eventually we will hit a cycle because some nums[k] has already been applied to position k, which means nums[k]
        is the duplication.

        O(N) time and O(1) space, 4 ms, faster than 87.14%
         */
        int slow = 0; int fast = 0;
        while (true) {
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (fast == slow) {
                break;
            }
        } // slow and fast end up at one point in the cycle
        slow = 0;
        while (slow != fast) { // the first time slow == fast is the starting point of the cycle
            slow = nums[slow];
            fast = nums[fast];
        }
        return nums[slow];
    }
}