class Solution {
    public String smallestString(String s) {
        /*
        Pay attention to the requirement of the problem:
        
        "performing the above operation exactly once"
        
        Skip all the prefix 'a'.
        Roll back any non-a letter following the prefix.
        Break once another 'a' is encountered.
        
        Special treatment when the entire string consists of only 'a'.
        
        O(N), 9 ms, faster than 96.61%
        */
        int i = 0;
        while (i < s.length() && s.charAt(i) == 'a') i++;
        StringBuilder sb = new StringBuilder(s.substring(0, i));
        boolean actionPerformed = false;
        while (i < s.length() && s.charAt(i) != 'a') {
            sb.append((char)(s.charAt(i++) - 1));
            actionPerformed = true;
        }
        return actionPerformed ? sb + s.substring(i) : s.substring(0, s.length() - 1) + "z";
    }
}