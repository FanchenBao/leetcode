class Solution {
    public int minimizedStringLength(String s) {
        /*
        Find the count of unique letters.

        7 ms, faster than 78.40%
        */
        Set<Character> uniqs = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            uniqs.add(s.charAt(i));
        }
        return uniqs.size();
    }
}
