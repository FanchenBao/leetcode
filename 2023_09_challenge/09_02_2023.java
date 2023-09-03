class TrieNode {
    HashMap<Character, TrieNode> map = new HashMap<>();
    boolean endOfWord = false;
}

class Solution {
    Integer[] memo;
    String s;
    TrieNode root;

    private int dp(int idx) {
        if (idx >= s.length()) {
            return 0;
        }
        if (memo[idx] != null) {
            return memo[idx];
        }
        // option 1, make s[idx] the extra character
        memo[idx] = 1 + dp(idx + 1);
        // option 2, try to fit s[idx:] into one of the word in the dictionary
        TrieNode node = root;
        for (int i = idx; i < s.length() && node != null; i++) {
            node = node.map.getOrDefault(s.charAt(i), null);
            if (node != null && node.endOfWord) {
                memo[idx] = Math.min(memo[idx], dp(i + 1));
            }
        }
        return memo[idx];
    }
    public int minExtraChar(String s, String[] dictionary) {
        /*
        LeetCode 2707

        Use trie to convert dictionary into something easier to check.
        Then DP, in which dp(i) is the min extra character needed in s[i:]. For each i, we can choose to make it extra,
        or try to match s[i:] in the trie.

        O(KM + N^2), where K = len(dictionary), N = len(s), and M is the average length of word in dictionary.
        14 ms, faster than 94.00%
         */
        memo = new Integer[s.length()];
        this.s = s;
        root = new TrieNode();
        for (String word : dictionary) {
            TrieNode node = root;
            for (int i = 0; i < word.length(); i++) {
                node.map.putIfAbsent(word.charAt(i), new TrieNode());
                node = node.map.get(word.charAt(i));
            }
            node.endOfWord = true;
        }
        return dp(0);
    }
}
