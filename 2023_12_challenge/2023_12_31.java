class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        /*
        LeetCode 1624

        O(N), 1 ms, faster than 86.22%
         */
        int[] initIndices = new int[26];
        Arrays.fill(initIndices, -1);
        int res = -1;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (initIndices[c - 'a'] == -1)
                initIndices[c - 'a'] = i;
            else
                res = Math.max(res, i - initIndices[c - 'a'] - 1);
        }
        return res;
    }
}

