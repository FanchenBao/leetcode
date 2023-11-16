class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        /*
        LeetCode 1846
        
        Sort arr, and for each position, find its max possible value based on its previous neighbor.
        
        O(NlogN), 6 ms, faster than 82.14%
         */
        Arrays.sort(arr);
        arr[0] = 1;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > arr[i - 1] + 1)
                arr[i] = arr[i - 1] + 1;
        }
        return arr[arr.length - 1];
    }
}


class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        /*
        Counting sort again!

        The max value possible after arr is rearranged is n. Thus, we can count
        the number of appearances of num in arr with the max topped at n.

        Then we go through the counts. If for the current value num, counts[num] > 0,
        we can fill up the rearranged arr up to num or however much affordable by
        counts[num].

        O(N), 3 ms, faster than 100.00%
         */
        int[] counts = new int[arr.length + 1];
        for (int a : arr) counts[Math.min(a, arr.length)]++;
        int res = 1;
        for (int a = 2; a <= arr.length; a++)
            // for the position (and the current value of a, the max value in
            // arr cannot exceed a itself
            res = Math.min(res + counts[a], a);
        return res;
    }
}
