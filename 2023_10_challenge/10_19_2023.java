class Solution {
    private String build(String s) {
        Stack<Character> ss = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!ss.isEmpty() && c == '#') ss.pop();
            if (c != '#') ss.push(c);
        }
        return ss.toString();
    }

    public boolean backspaceCompare(String s, String t) {
        /*
        LeetCode 844

        Stack. 2 ms, faster than 62.00%
         */
        return build(s).equals(build(t));
    }
}
