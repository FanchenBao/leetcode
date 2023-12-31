class Solution {
    public boolean makeEqual(String[] words) {
        /*
        LeetCode 1897
        
        Make sure the count of each letter in all words is divisible
        by the length of words.
        
        O(N) where N is the total number of letters in words.
        
        4 ms, faster than 43.02%
         */
        int[] counter = new int[26];
        for (String word : words) {
            for (char c : word.toCharArray())
                counter[c - 'a']++;
        }
        for (int c : counter) {
            if (c % words.length != 0)
                return false;
        }
        return true;
    }
}

