import java.util.*;
import java.util.stream.Stream;
import java.math.*;

/**
 * Definition for a binary tree node.
 */
//class TreeNode {
//    int val;
//    TreeNode left;
//    TreeNode right;
//    TreeNode() {}
//    TreeNode(int val) { this.val = val; }
//    TreeNode(int val, TreeNode left, TreeNode right) {
//        this.val = val;
//        this.left = left;
//        this.right = right;
//    }
//}


class Solution1 {
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    
    private void shuffleArray(int[] array) {
        // Copied from https://stackoverflow.com/a/18456998/9723036
        int index, temp;
        Random random = new Random();
        for (int i = array.length - 1; i > 0; i--)
        {
            index = random.nextInt(i + 1);
            temp = array[index];
            array[index] = array[i];
            array[i] = temp;
        }
    }

    private void quicksort(int[] nums, int lo, int hi) {
        if (lo >= hi)
            return;
        int j = hi;
        int i = lo + 1;
        while (i <= j) {
            if (nums[i] > nums[lo])
                swap(nums, i, j--);
            else
                i++;
        }
        swap(nums, --i, lo);
        quicksort(nums, lo, i - 1);
        quicksort(nums, i + 1, hi);
    }

    public int[] sortArray(int[] nums) {
        /*
         * LeetCode 912
         *
         * Use quick sort, but with a pre-shuffle
         
         * 2198 ms, faster than 5.02% 
         */
        shuffleArray(nums);
        quicksort(nums, 0, nums.length - 1);
        return nums;
    }
}


class Solution2 {
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    private void quicksort(int[] nums, int lo, int hi) {
        if (lo >= hi)
            return;
        Random random = new Random();
        swap(nums, lo, random.nextInt(hi - lo + 1) + lo); // randomize pivot
        int j = hi;
        int i = lo + 1;
        while (i <= j) {
            if (nums[i] > nums[lo])
                swap(nums, i, j--);
            else
                i++;
        }
        swap(nums, --i, lo);
        quicksort(nums, lo, i - 1);
        quicksort(nums, i + 1, hi);
    }

    public int[] sortArray(int[] nums) {
        /*
         * LeetCode 912
         *
         * Randomize the pivot for quicksort
         */
        quicksort(nums, 0, nums.length - 1);
        return nums;
    }
}


class Solution3 {
    private int[] mergeSort(int[] nums, int lo, int hi) {
        if (lo == hi)
            return new int[]{nums[lo]};
        int mid = (lo + hi) / 2;
        int[] left = mergeSort(nums, lo, mid);
        int[] right = mergeSort(nums, mid + 1, hi);
        // Merge
        int[] res = new int[hi - lo + 1];
        int i = 0;
        int j = 0;
        int k = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j])
                res[k++] = left[i++];
            else
                res[k++] = right[j++];
        }
        while (i < left.length)
            res[k++] = left[i++];
        while (j < right.length)
            res[k++] = right[j++];
        return res;
    }

    public int[] sortArray(int[] nums) {
        /*
         * Use merge sort. Seems like it is faster than quick sort.
         *
         * 21 ms, faster than 79.13%
         */
        return mergeSort(nums, 0, nums.length - 1);
    }
}






class Main{
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
