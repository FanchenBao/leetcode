class Solution {
    private boolean isPredecesor(String word1, String word2) {
        // Return true if word1 is a predecessor of word2
        String modWord2;
        for (int i = 0; i < word2.length(); i++) {
            modWord2 = word2.substring(0, i) + word2.substring(i + 1);
            if (word1.equals(modWord2)) {
                return true;
            }
        }
        return false;
    }

    public int longestStrChain(String[] words) {
        /*
        LeetCode 1048

        Create a map where the key is the length of each word and the value is a list of words.
        Then use DP from large word size to small word size, and find the max length of word chain starting from each
        word.

        O(N * m), where N = len(words) and m is the average size of each word
        
        234 ms, faster than 5.70% (the runtime is SOOOO bad)
         */
        Map<Integer, List<String>> sizeMap = new HashMap<>();
        int maxSize = Integer.MIN_VALUE;
        for (String word : words) {
            sizeMap.putIfAbsent(word.length(), new ArrayList<>());
            sizeMap.get(word.length()).add(word);
            maxSize = Math.max(maxSize, word.length());
        }
        Map<String, Integer> dp = new HashMap<>();
        int res = 1;
        for (int s = maxSize - 1; s >= 1; s--) {
            for (String curWord : sizeMap.getOrDefault(s, Collections.emptyList())) {
                dp.put(curWord, 1);
                for (String nextWord : sizeMap.getOrDefault(s + 1, Collections.emptyList())) {
                    if (isPredecesor(curWord, nextWord)) {
                        dp.put(curWord, Math.max(dp.get(curWord), dp.getOrDefault(nextWord, 1) + 1));
                    }
                }
                res = Math.max(res, dp.get(curWord));
            }
        }
        return res;
    }
}


class Solution {

    public int longestStrChain(String[] words) {
        /*
        LeetCode 1048

        Create a map where the key is the length of each word and the value is a list of words.
        Then use DP from large word size to small word size, and find the max length of word chain starting from each
        word.

        UPDATE: make the check for predecessor faster by adding letter to the smaller word and directly check if the
        new version exists in the next word. Since each word is of size 16, and there are only 26 letters, it should
        be faster to check this way than a nested loop

        O(N * m), where N = len(words) and m is the average size of each word
        
        Hehe, it is actually slower. 939 ms, faster than 5.15%
         */
        Map<Integer, List<String>> sizeMap = new HashMap<>();
        int maxSize = Integer.MIN_VALUE;
        for (String word : words) {
            sizeMap.putIfAbsent(word.length(), new ArrayList<>());
            sizeMap.get(word.length()).add(word);
            maxSize = Math.max(maxSize, word.length());
        }
        Map<String, Integer> dp = new HashMap<>();
        int res = 1;
        String nextWord;
        for (int s = maxSize; s >= 1; s--) {
            for (String curWord : sizeMap.getOrDefault(s, Collections.emptyList())) {
                dp.put(curWord, 1);
                for(char c = 'a'; c <='z'; c++ ) {
                    for (int i = 0; i <= curWord.length(); i++) {
                        nextWord = curWord.substring(0, i) + String.valueOf(c) + curWord.substring(i);
                        dp.put(curWord, Math.max(dp.get(curWord), dp.getOrDefault(nextWord, 0) + 1));
                    }
                }
                res = Math.max(res, dp.get(curWord));
            }
        }
        return res;
    }
}


class Solution {

    public int longestStrChain(String[] words) {
        /*
        LeetCode 1048

        UPDATE: No need to do the size map! Just sort words by length
        
        O(NlogN), 52 ms, faster than 30.76%
         */
        Arrays.sort(words, Comparator.comparingInt(String::length));
        Map<String, Integer> dp = new HashMap<>();
        int res = 1;
        String preWord;
        for (String word : words) {
            for (int i = 0; i < word.length(); i++) {
                preWord = word.substring(0, i) + word.substring(i + 1);
                dp.put(word, Math.max(dp.getOrDefault(word, 1), dp.getOrDefault(preWord, 0) + 1));
            }
            res = Math.max(res, dp.get(word));
        }
        return res;
    }
}
