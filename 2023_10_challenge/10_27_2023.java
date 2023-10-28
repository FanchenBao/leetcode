class Solution {
    public String longestPalindrome(String s) {
        /*
        LeetCode 5
        
        DP. At each character, we try all the possible palindromes ending
        at the character right in front of us to check the possible palindromes
        that end at the current character.
        
        One tricky part is that if the current character is equal to its
        immediate predecesor, that is a palindrome as well.
        
        O(N^2), 61 ms, faster than 41.72%
        */
        List<Integer> pre = new ArrayList<>();
        pre.add(0);
        String res = s.substring(0, 1);
        for (int i = 1; i < s.length(); i++) {
            List<Integer> tmp = new ArrayList<>();
            tmp.add(i);
            if (s.charAt(i) == s.charAt(i - 1)) {
                tmp.add(i - 1);
                if (res.length() < 2)
                    res = s.substring(i - 1, i + 1);
            }
            for (Integer j : pre) {
                if (j - 1 >= 0 && s.charAt(j - 1) == s.charAt(i)) {
                    tmp.add(j - 1);
                    if (i - j + 2 > res.length())
                        res = s.substring(j - 1, i + 1);
                }
            }
            pre = tmp;
        }
        return res;
    }
}
