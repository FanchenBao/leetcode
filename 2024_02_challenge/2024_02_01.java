class Solution {
    public int[][] divideArray(int[] nums, int k) {
        /*
        LeetCode 2966
        
        Very clunky in writing Java again. Getting too spoiled by the
        simplicity of Python.
        
        Greedy solution. Sort nums and just try to put every three values
        into the answer. Need to check whether any two pairs within the
        three consecutive numbers satisfy the difference requirement.
        
        O(NlogN), 24 ms, faster than 68.69%
        */
        Arrays.sort(nums);
        int[][] res = new int[nums.length / 3][3];
        int j = -1;
        for (int i = 0; i < nums.length; i++) {
            if (i % 3 != 0) {
                if (nums[i] - nums[i - 1] > k || (i % 3 == 2 && nums[i] - nums[i - 2] > k))
                    return new int[][]{};
                res[j][i % 3] = nums[i];
            } else {
                j++;
                res[j][0] = nums[i];
            }
        }
        return res;
    }
}


class Solution {
    public int[][] divideArray(int[] nums, int k) {
        /*
        Better implementation
        
        25 ms, faster than 38.13%
         */
        Arrays.sort(nums);
        int[][] res = new int[nums.length / 3][3];
        for (int i = 0; i < nums.length; i += 3) {
            if (nums[i + 2] - nums[i] > k)
                return new int[][]{};
            res[i / 3] = new int[]{nums[i], nums[i + 1], nums[i + 2]};
        }
        return res;
    }
}

