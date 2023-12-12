class Solution {
    public int findSpecialInteger(int[] arr) {
        /*
        LeetCode 1287
        
        O(N), 0 ms, faster than 100.00%
         */
        int count = 1;
        int tgt = arr.length / 4;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == arr[i - 1]) {
                count++;
                if (count > tgt)
                    return arr[i];
            } else {
                count = 1;
            }
        }
        if (count > tgt)
            return arr[arr.length - 1];
        return -1;
    }
}
