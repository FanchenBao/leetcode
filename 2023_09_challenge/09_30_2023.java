class Solution {
    int[] premin;

    private boolean manageMonoStack(List<int[]> stack, int cur) {
        while (!stack.isEmpty() && stack.get(stack.size() - 1)[1] <= cur) {
            int[] popped = stack.remove(stack.size() - 1);
            if (!stack.isEmpty()) {
                int[] pre = stack.get(stack.size() - 1);
                if (popped[1] > premin[pre[0]] && pre[1] > premin[pre[0]]){
                    return true;
                }
            }
        }
        return false;
    }

    public boolean find132pattern(int[] nums) {
        /*
        LeetCode 456
        
        I struggled a lot on this problem in the past. So I am very pleased that we got only a slight hiccup before
        finding the right solution. I have to admit that although I didn't remember the previous solution, I vaguely
        knew the solucion has something to do with monotonic array. This helps reduce the search space of all potential
        solutions.
        
        The most important insight is that monotonic increasing array does not work. Then when I switched to monotonic
        decreasing array, I realized that when numbers get popped in a monotonic decreasing array, as long as the stack
        is not empty, it is guaranteed that we have some value to the left of the popped one that is bigger than the
        popped one. Thus, we only need to ensure that some value to the left of the bigger value currently in the stack
        is smaller than the popped, then we will have found the 132 pattern.
        
        To quickly find the smallest value to the left of any number in nums, we need a prefix min array.
        
        O(N), 16 ms, faster than 67.91% 
         */
        if (nums.length < 3) {
            return false;
        }
        premin = new int[nums.length];
        premin[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            premin[i] = Math.min(premin[i - 1], nums[i]);
        }
        List<int[]> stack = new ArrayList<>(); // monotonic decreasing. stack[i] = [idx, val]
        for (int i = 0; i < nums.length; i++) {
            if (manageMonoStack(stack, nums[i])) {
                return true;
            }
            stack.add(new int[]{i, nums[i]});
        }
        return manageMonoStack(stack, Integer.MAX_VALUE);
    }
}


class Solution {
    public boolean find132pattern(int[] nums) {
        /*
        This is the solution I submitted last year. I am pretty sure I didn't come up with this myself, because it was
        quite brilliant.

        We use a premin array as well. Then we go from right to left on nums and produce a monotonic decreasing array.
        The trick here is that we must ensure that every number in the monotonic decreasing array is bigger than
        the premin of the current value. Then everything in the monotonic decreasing array is a potential nums[k]. The
        premin value is a potential nums[i]. All we need to do is the check whether the current value can be a nums[j].
        We know the current value must be bigger than its premin. So we need to check whether it is also bigger than
        the smallest of the monotonic decreasing array. It just so happens that the smallest in a monotonic decreasing
        array is the value on its tail. Viola, we have a check for the 132 pattern.

        O(N), 15 ms, faster than 72.29%
         */
        if (nums.length < 3) {
            return false;
        }
        int[] premin = new int[nums.length];
        premin[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            premin[i] = Math.min(premin[i - 1], nums[i]);
        }
        List<Integer> stack = new ArrayList<>(); // monotonic decreasing
        for (int i = nums.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && premin[i] >= stack.get(stack.size() - 1)) {
                stack.remove(stack.size() - 1);
            }
            // premin[i] is the potential first value; stack[-1] is the potential third value
            if (!stack.isEmpty() && nums[i] > premin[i] && nums[i] > stack.get(stack.size() - 1)) {
                return true;
            }
            stack.add(nums[i]);
        }
        return false;
    }
}

