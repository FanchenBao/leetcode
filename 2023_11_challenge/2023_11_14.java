class Solution {
    public int countPalindromicSubsequence(String s) {
        /*
        LeetCode 1930

        For each letter, all possible 3-letter palindromes with this letter at the start and end
        are aaa, aba, aca, ..., aza.

        Thus, for each letter, we just need to count how many other letters which at least contains
        one index that is between the min and max index of the current letter.

        This can be solved using binary search.

        O(N + 26 * 26 * logN), 20 ms, faster than 92.89% 
         */
        List<List<Integer>> indices = new ArrayList<>();
        for (int i = 0; i < 26; i++) indices.add(new ArrayList<>());
        for (int i = 0; i < s.length(); i++) indices.get(s.charAt(i) - 'a').add(i);
        int res = 0;
        for (int i = 0; i < 26; i++) {
            if (indices.get(i).size() >= 2) {
                List<Integer> curIndices = indices.get(i);
                int minI = curIndices.get(0); int maxI = curIndices.get(curIndices.size() - 1);
                if (maxI - minI > 1) {
                    for (int j = 0; j < 26; j++) {
                        int idx = Collections.binarySearch(indices.get(j), minI);
                        if (idx >= 0 && curIndices.size() >= 3)
                            res++;
                        else if (idx < 0 && -idx - 1 < indices.get(j).size() && indices.get(j).get(-idx-1) < maxI)
                            res++;
                    }
                }
            }
        }
        return res;
    }
}


class Solution {
    public int countPalindromicSubsequence(String s) {
        /*
        Without binary search.
        
        This is the official solution.
        
        193 ms, faster than 54.66%
         */
        int res = 0;
        for (int c = 0; c < 26; c++) {
            // pick a letter that marks the left and right of the 3-letter palindrome
            int i = 0;
            while (i < s.length() && s.charAt(i) - 'a' != c) i++;
            if (i >= s.length() - 2)
                continue;
            int j = s.length() - 1;
            while (j >= 0 && s.charAt(j) - 'a' != c) j--;
            if (j <= 1)
                continue;
            if (j - i <= 1)
                continue;;
            Set<Character> between = new HashSet<>();
            for (int k = i + 1; k < j; k++)
                between.add(s.charAt(k));
            res += between.size();
        }
        return res;
    }
}