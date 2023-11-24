class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        /*
        LeetCode 1630

        Naive solution, in which we simply copy out the nums subarray from l[i] to r[i]
        sort it and check.

        O(MNlogN), 21 ms, 36.81%
         */
        List<Boolean> res = new ArrayList<>();
        for (int i = 0; i < l.length; i++) {
            int[] tmp = new int[r[i] - l[i] + 1];
            System.arraycopy(nums, l[i], tmp, 0, r[i] + 1 - l[i]);
            Arrays.sort(tmp);
            int diff = tmp[1] - tmp[0];
            res.add(true);
            for (int j = 2; j < tmp.length; j++) {
                if (tmp[j] - tmp[j - 1] != diff) {
                    res.set(i, false);
                    break;
                }
            }
        }
        return res;
    }
}


class Solution {
    private boolean check(int[] nums, int rl, int rr) {
        int[] tmp = new int[rr - rl + 1];
        System.arraycopy(nums, rl, tmp, 0, rr + 1 - rl);
        Arrays.sort(tmp);
        int diff = tmp[1] - tmp[0];
        for (int j = 2; j < tmp.length; j++) {
            if (tmp[j] - tmp[j - 1] != diff) {
                return false;
            }
        }
        return true;
    }
    
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        /*
        LeetCode 1630

        Naive solution, in which we simply copy out the nums subarray from l[i] to r[i]
        sort it and check.

        O(MNlogN), 16 ms, faster than 94.51%
         */
        List<Boolean> res = new ArrayList<>();
        for (int i = 0; i < l.length; i++)
            res.add(check(nums, l[i], r[i]));
        return res;
    }
}


class Solution {
    private boolean check(int[] nums, int rl, int rr) {
        int[] tmp = new int[rr - rl + 1];
        System.arraycopy(nums, rl, tmp, 0, rr + 1 - rl);
        int min = tmp[0];
        int max = tmp[0];
        Set<Integer> seen = new HashSet<>();
        for (int n : tmp) {
            min = Math.min(min, n);
            max = Math.max(max, n);
            seen.add(n);
        }
        if ((max - min) % (tmp.length - 1) != 0)
            return false;
        int diff = (max - min) / (tmp.length - 1);
        for (int i = 1; i < tmp.length - 1; i++) {
            if (!seen.contains(min + diff * i))
                return false;
        }
        return true;
    }

    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        /*
        This is the O(MN) solution from the official solution.
        
        We find the min and max of the copied array, which allows us to compute the diff.
        Then we use a set to check whether all required elements are in the copied array.

        30 ms, faster than 32.14%
         */
        List<Boolean> res = new ArrayList<>();
        for (int i = 0; i < l.length; i++)
            res.add(check(nums, l[i], r[i]));
        return res;
    }
}
