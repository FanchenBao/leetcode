class Solution {
    int k;
    String s;

    private long solve(long preLen, int idx) {
        // when this function is called, k must be larger than preLen. Otherwise, we would've solved it
        // in the previous round of calling solve.
        // It returns a non-negative integer if the kth letter is
        // NOT found in the current stretch of s. We return the position
        // to the previous round of recursion.
        // If the kth letter is found, we return the char but in its
        // negative version to separate from the other form of return value.
        int i = idx;
        while (i < s.length() && s.charAt(i) >= 'a' && s.charAt(i) <= 'z') {i++;}
        int lenCurS = i - idx;
        long lenCurRep = preLen + lenCurS;
        long lenCurTotal = i < s.length() ? lenCurRep * Character.getNumericValue(s.charAt(i)) : lenCurRep;
        long pos;
        if (k > lenCurTotal) {
            pos = solve(lenCurTotal, i + 1);
            if (pos < 0) {
                // found the character
                return pos;
            }
        } else {
            pos = k;
        }
        long r = pos % lenCurRep;
        if (r <= preLen && r > 0) {
            // the position of the letter resides in the previous
            // length, so we return the position to the previous
            // recursion
            return r;
        }
        if (r == 0) {
            // If there is a current stretch of s, the character
            // must be the last character of the current stretch.
            // If there is no current stretch, then we have to
            // find the letter in previous recursions.
            return lenCurS > 0 ? -s.charAt(i - 1) : r;
        }
        // The letter is within the current stretch of s.
        return -s.charAt((int)(idx + r - preLen - 1));
    }

    public String decodeAtIndex(String s, int k) {
        /*
        LeetCode 880
        
        Took A LOT OF efforts to get this one. The basic idea is
        recursion. At each level, we combine whatever length previously
        with the current stretch of s, and see if the kth letter
        can be found. If not, we keep recursion. Otherwise, we rewind
        the call stack to find where the kth letter is.
        
        NOTE: this is Java, int can overflow.
        
        0 ms, faster than 100.00%
        */
        this.s = s;
        this.k = k;
        return String.valueOf((char)-solve(0, 0));
    }
}


class Solution {
    int k;
    String s;

    private char solve(long pos) {
        /*
        Reduce the size of k at each recursion call. And each recursion call repeat the same process starting
        from the beginning. Since each time k is reduced, eventually we will have a k small enough that a
        recursion going from the start will encounter it.
         */
        long preLen = 0;
        long lenCurS = 0;
        long lenCurRep;
        long lenCurTotal;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) < 'a' || s.charAt(i) > 'z') {
                // a digit
                lenCurRep = preLen + lenCurS;
                lenCurTotal = lenCurRep * Character.getNumericValue(s.charAt(i));
                if (lenCurTotal >= pos) {
                    long r = pos % lenCurRep;
                    return solve(r == 0 ? lenCurRep : r); // note the replacement of r with lenCurRep
                }
                preLen = lenCurTotal;
                lenCurS = 0;
            } else {
                lenCurS++;
                if (preLen + lenCurS == pos) {
                    return s.charAt(i);
                }
            }

        }
        return ' '; // will not hit this value
    }

    public String decodeAtIndex(String s, int k) {
        /*
        Inspired by the solution I had two years ago
        
        0 ms, faster than 100.00% 
         */
        this.s = s;
        this.k = k;
        return String.valueOf(solve(k));
    }
}
