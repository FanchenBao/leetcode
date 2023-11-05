 class Solution {
    public int getWinner(int[] arr, int k) {
        /*
        LeetCode 1535
        
        Since k can get really big, it is not possible to simulate the
        entire process. We recognize that after going through the arr
        for the first time, the largest value must be at arr[0] and it
        will never be de-throned again. This means, if after going through
        the arr and k is still not matched, then whatever value at arr[0]
        must be the answer since it will win forever.
        
        Thus, we only need to consider one pass of arr. And since we don't
        need to worry about moving the elements around, a simple iteration
        will work.
        
        O(N), 0 ms, faster than 100.00% 
        */
        int conseqW = 1; arr[0] = Math.max(arr[0], arr[1]);
        for (int i = 2; i < arr.length && conseqW < k; i++) {
            if (arr[i] > arr[0]) {
                arr[0] = arr[i];
                conseqW = 1;
            } else {
                conseqW++;
            }
        }
        return arr[0];
    }
}