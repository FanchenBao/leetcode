public int buildString(char[] strArray, int start, int[][] sorted, int sortedJ, String s) {
        int j = sortedJ;
        for (int i = start; i < s.length(); i += 2) {
            char cur = (char)(sorted[j][1] + 97);
            if (i > 0 && cur == strArray[i - 1]) {
                // must be smaller than -1, otherwise would confuse with a natural normal output of j when the entire
                // s is exhausted
                return -2;
            }
            strArray[i] = cur;
            sorted[j][0] -= 1;
            if (sorted[j][0] == 0) {
                j--;
            }
        }
        return j;
    }
    public String reorganizeString(String s) {
        /*
        LeetCode 767
        
        I went throuh several iterations of the solution, and finally settled down with the current version. We get the
        count of each letter and sort them by frequency in reverse order. Then we fill the string's even positions first
        using the most frequent letter and so on. Then we fill the odd positions. Anytime a letter to be filled is equal
        to its previous neighbor, we know it is impossible to reorganize the string.
        
        O(NlogN), 3 ms, faster than 68.33%
         */
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 97]++;
        }
        int[][] sorted = new int[26][2];
        for (int i = 0; i < 26; i++) {
            sorted[i][0] = count[i]; sorted[i][1] = i;
        }
        Arrays.sort(sorted, Comparator.comparingInt(tup -> tup[0]));
        char[] res = new char[s.length()];
        // Fill the even positions first. Use the characters with highest count first
        int j = 25;
        j = buildString(res, 0, sorted, j, s);
        if (j < -1) {
            return "";
        }
        // Then fill the odd positions
        if (buildString(res, 1, sorted, j, s) < -1) {
            return "";
        }
        return String.valueOf(res);
    }
}
