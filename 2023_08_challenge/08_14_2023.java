class Solution1 {
    public int findKthLargest(int[] nums, int k) {
        /*
        LeetCode 215
        
        Priority queue.
        
        O(KlogN), 67 ms, faster than 34.90%
         */
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        for (int n: nums) {
            maxHeap.add(n);
        }
        while (--k > 0) {
            maxHeap.poll();
        }
        return maxHeap.poll();
    }
}


class Solution2 {
    public int findKthLargest(int[] nums, int k) {
        /*
        Just sort it.

        O(NlogN), 23 ms, faster than 85.60%
         */
        Arrays.sort(nums);
        return nums[nums.length - k];
    }
}

class Solution3 {
    Random rand = new Random();

    private int quickselect(ArrayList<Integer> nums, int k) {
        ArrayList<Integer> left = new ArrayList<>(); // all values larger than pivot
        ArrayList<Integer> right = new ArrayList<>(); // all values smaller to pivot
        int midCount = 0;
        int idx = rand.nextInt(nums.size());
        int pivot = nums.get(idx);
        for (Integer n : nums) {
            if (n > pivot) {
                left.add(n);
            } else if (n < pivot) {
                right.add(n);
            } else {
                midCount++;
            }
        }
        if (left.size() >= k) {
            return quickselect(left, k);
        }
        if (left.size() + midCount < k) {
            return quickselect(right, k - left.size() - midCount);
        }
        return pivot;
    }

    public int findKthLargest(int[] nums, int k) {
        /*
        From the official solution, quick select.

        Average run time is O(N), 20 ms, faster than 89.57%
         */
        ArrayList<Integer> numsList = new ArrayList<>();
        for (int n : nums) numsList.add(n);
        return quickselect(numsList, k);

    }
}
