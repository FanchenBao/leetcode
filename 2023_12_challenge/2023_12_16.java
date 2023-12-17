class Solution {
    public boolean isAnagram(String s, String t) {
        /*
        LeetCode 242
        
        6 ms, faster than 42.49%
        */
        if (s.length() != t.length())
            return false;
        int[] scount = new int[26];
        int[] tcount = new int[26];
        for (int i = 0; i < s.length(); i++) {
            scount[s.charAt(i) - 97]++;
            tcount[t.charAt(i) - 97]++;
        }
        for (int j = 0; j < 26; j++) {
            if (scount[j] != tcount[j])
                return false;
        }
        return true;
    }
}
