 class Solution {
    public boolean isFascinating(int n) {
        /*
        10 ms, faster than 48.26%
        */
        String nstr = String.valueOf(n) + String.valueOf(2 * n) + String.valueOf(3 * n);
        Set<Character> seen = new HashSet<>();
        for (int i = 0; i < nstr.length(); i++) seen.add(nstr.charAt(i));
        return !seen.contains('0') && seen.size() == 9 && nstr.length() == 9;
    }
}