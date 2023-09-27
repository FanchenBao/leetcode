class Solution {
    public String removeDuplicateLetters(String s) {
        /*
        LeetCode 316

        Similar to a monotonic stack. For each new char that has not been incorporated, we check the already built
        string and see if the end of that stirng is smaller or bigger than the current char. If the current char is
        bigger, we append it because that is the best we can achieve at the moment.

        If the current char is smaller than the last of the built string AND if the last of the built string will occur
        again later, we can safely pop the end of the built string and continue the check with the second to last char.
        We keep this check until either we run out of char to check or a char that is either bigger than the current
        or does not appear again later shows up. That is where we place the current char.

        In addition to the monotonic stack, we also need to identify the latest occurrence of each char and establish
        a way to check whether a char has been incorporated.

        O(N), 2 ms, faster than 96.28%
         */
        int[] maxPos = new int[26];
        int[] visited = new int[26];
        for (int i = 0; i < s.length(); i++) {
            maxPos[s.charAt(i) - 97] = i;
        }
        char[] res = new char[26];
        res[0] = s.charAt(0);
        visited[s.charAt(0) - 97] = 1;
        int j = 1;
        char cur; char pre;
        int curIdx; int preIdx;
        for (int i = 1; i < s.length(); i++) {
            cur = s.charAt(i);
            curIdx = cur - 97;
            if (visited[curIdx] == 0) {
                while (j >= 1 && cur < res[j - 1] && i < maxPos[res[j - 1] - 97]) {
                    // cur is smaller than res[j - 1], and res[j - 1] appears again later
                    visited[res[j - 1] - 97] = 0;
                    j--;
                }
                res[j++] = s.charAt(i);
                visited[curIdx] = 1;
            }
        }
        return new String(res, 0, j);
    }
}
