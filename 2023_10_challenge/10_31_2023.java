class Solution {
    public int[] findArray(int[] pref) {
        /*
        LeetCode 2433
        
        O(N), 2 ms, faster than 59.65%
        */
        int[] res = new int[pref.length];
        res[0] = pref[0];
        for (int i = 1; i < pref.length; i++) res[i] = pref[i - 1] ^ pref[i];
        return res;
    }
}
