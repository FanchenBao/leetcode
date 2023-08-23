class Solution1 {
    public String convertToTitle(int columnNumber) {
        /*
        LeetCode 168

        Not that simple. The main idea is the same as converting a binary value. We mod 26 for each columnNumber,
        and the remainder corresponds to a letter. The tricky part is how to find the next columnNumber. Of course
        we first minus the remainder and then divided by 26, but if the remainder has been zero, we need to minus one
        more.

        O(logN), 0 ms, faster than 100.00%
         */
        String[] alphabet = new String[26];
        alphabet[0] = "Z";
        for (int i = 1; i < 26; i++) {
            alphabet[i] = String.valueOf((char)(64 + i));
        }
        StringBuilder res = new StringBuilder();
        while (columnNumber > 0) {
            int r = columnNumber % 26;
            res.insert(0, alphabet[r]);
            columnNumber = columnNumber / 26 - (r == 0 ? 1 : 0);
        }
        return res.toString();
    }
}


class Solution2 {
    public String convertToTitle(int columnNumber) {
        /*
        Recursion version
        
        Slower. 7 ms, faster than 15.49%
         */
        if (columnNumber <= 0) {
            return "";
        }
        int q = columnNumber / 26; int r = columnNumber % 26;
        if (r == 0) {
            q--; r = 26;
        }
        return convertToTitle(q) + (char)(64 + r);
    }
}


class Solution3 {
    public String convertToTitle(int columnNumber) {
        /*
        Even simpler iterative
         */
        StringBuilder res = new StringBuilder();
        int q = columnNumber;
        while (q > 0) {
            int r = q % 26; q /= 26; 
            if (r == 0) {
                q--; r = 26;  // move one instance from quotient to remainder
            }
            res.insert(0, (char)(64 + r));
        }
        return res.toString();
    }
}
