class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        /*
        O(N), 4 ms, faster than 49.47%
        */
        Set<String> wordsSet = new HashSet<>(Arrays.asList(words));
        int res = 0;
        for (String w : words) {
            String rev = new StringBuilder(w).reverse().toString();
            if (wordsSet.contains(rev) && !w.equals(rev)) {
                res++;
                wordsSet.remove(rev);
                wordsSet.remove(w);
            }
        }
        return res;
    }
}


class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        /*
        O(N^2)
        
        Since N is so small, this is faster because it has much lower
        overhead compared to the O(N) solution.
        
        1 ms, faster than 100.00%
        */
        int res = 0;
        for (int i = 0; i < words.length; i++) {
            if (words[i].isEmpty())
                continue;
            for (int j = i + 1; j < words.length; j++) {
                if (words[j].isEmpty())
                    continue;
                if (words[i].charAt(0) == words[j].charAt(1) && words[i].charAt(1) == words[j].charAt(0)) {
                    res++;
                    words[j] = "";
                }
            }
        }
        return res;
    }
}
