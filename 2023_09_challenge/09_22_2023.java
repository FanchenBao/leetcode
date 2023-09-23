class Solution {
    public boolean isSubsequence(String s, String t) {
        /*
        LeetCode 392
        1 ms, faster than 89.69%
         */
        int i = 0; int j = 0;
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
            }
            j++;
        }
        return i == s.length();
    }
}
