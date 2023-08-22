class Solution1 {
    public boolean repeatedSubstringPattern(String s) {
        /*
        LeetCode 459

        Not very happy with this brute force solution. Basically, we check s one by one from the frone to find  a
        letter that is equal to the end of s. Then use that as a candidate to see if the entire string can be formed
        by that candidate.

        O(N^2), 8 ms, faster than 92.56%
         */
        char end = s.charAt(s.length() - 1);
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == end) {
                String cand = s.substring(0, i + 1);
                if (cand.length() * 2 > s.length()) {
                    break;
                }
                if (cand.equals(s.substring(s.length() - i - 1))) {
                    boolean found = true;
                    for (int j = i + 1; j + cand.length() < s.length(); j += cand.length()) {
                        if (!cand.equals(s.substring(j, j + cand.length()))) {
                            found = false;
                            break;
                        }
                    }
                    if (found) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}


class Solution2 {
    public boolean repeatedSubstringPattern(String s) {
        /*
        The ideal solution is to repeat s, remove its front and end character, and see if s is a substring of the
        remainder string.

        Proof: if s contains k repeats of a substring, then duplicating s produces 2k such substrings. Removal of the
        first and last character at most removes 2 substrings, which means the least number of substrings in the
        remainder string is 2k - 2.

        Since we propose that s is a repeat of the substring, it must be that k >= 2. Thus

        k + k >= 2 + k, thus 2k - 2 >= k

        In other words, the remainder string must contain at least k repeats of the substring, or the string s itself.
        Therefore, by checking whether s is a substring of the remainder string, we can determine whether s can be
        expressed as k repeats of a substring.

        The difficult part is to write an algorithm of O(N) complexity for substring match. That can be done via KMP,
        but having done KMP multiple times, I am very positive that I canNOT write KMP from scratch from memory. We will
        mention it to the interviewer, but sorry can't implement it.

        If using KMP, O(N). Otherwise, O(N^2)

        The solution below does not use KMP, and its run time is 74 ms.

        If using KMP, run time is 18 ms, faster than 76.89%
         */
        return (s + s).substring(1, s.length() * 2 - 1).contains(s);
    }
}