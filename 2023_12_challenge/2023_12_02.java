class Solution {
    public int countCharacters(String[] words, String chars) {
        /*
        LeetCode 1160
        
        Use counter.
        
        O(N) where N is the total number of letters in words.
        8 ms, faster than 65.56%
        */
        int[] counts = new int[26];
        for (int i = 0; i < chars.length(); i++)
            counts[chars.charAt(i) - 'a']++;
        int res = 0;
        for (String w : words) {
            int [] countsCopy = counts.clone();
            boolean canForm = true;
            for (int i = 0; i < w.length(); i++) {
                if (countsCopy[w.charAt(i) - 'a'] <= 0) {
                    canForm = false;
                    break;
                }
                countsCopy[w.charAt(i) - 'a']--;
            }
            if (canForm)
                res += w.length();
        }
        return res;
    }
}
