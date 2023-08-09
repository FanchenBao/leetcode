import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class TrieNode {
    HashMap<String, TrieNode> dict = new HashMap<>();
    String word;
}

class Solution1 {
    public Integer dp(Integer idx, HashMap<Integer, Integer> memo, String s, TrieNode root) {
        if (memo.containsKey(idx)) {
            return memo.get(idx);
        }
        if (idx == s.length()) {
            memo.put(idx, 0);
            return 0;
        }
        // Option 1, we take s[idx] as the extra character
        memo.put(idx, 1 + dp(idx + 1, memo, s, root));
        // Option 2, if we can, fit a substring starting from s[idx] into one of the words in dictionary
        TrieNode node = root;
        int i = idx;
        while (i < s.length()) {
            String letter = Character.toString(s.charAt(i));
            if (node.dict.containsKey(letter)){
                node = node.dict.get(letter);
                i++;
                if (node.word != null) {
                    memo.put(idx, Math.min(dp(i, memo, s, root), memo.get(idx)));
                }
            } else {
                break;
            }
        }
        if (node.word != null) {
            memo.put(idx, Math.min(dp(i, memo, s, root), memo.get(idx)));
        }
        return memo.get(idx);
    }
    public int minExtraChar(String s, String[] dictionary) {
        /*
        Build a trie out of dictionary. Use dp(idx) to find the min extra characters in s[idx:]. The tricky part
        is that as we go through s[idx:], we need to run dp EACH TIME a word is found. Also, for each s[idx], we
        have to consider a separate operation where s[idx] is NOT considered.

        O(M + N^2), where M is the total number of letters in dictionary. 20 ms, faster than 90.06%
         */
        TrieNode root = new TrieNode();
        for (String word : dictionary) {
            TrieNode node = root;
            for (int i = 0; i < word.length(); i++) {
                String letter = Character.toString(word.charAt(i));
                if (!node.dict.containsKey(letter)) {
                    node.dict.put(letter, new TrieNode());
                }
                node = node.dict.get(letter);
            }
            node.word = word;
        }

        HashMap<Integer, Integer> memo = new HashMap<>();
        return this.dp(0, memo, s, root);
    }
}


class TrieNode {
    HashMap<Character, TrieNode> dict = new HashMap<>();
    boolean isWord; // default value is false
}

class Solution2 {
    Integer[] memo;
    TrieNode root;

    int dp(int idx, String s) {
        if (idx == s.length()) {
            return 0;
        }
        if (memo[idx] != null) {
            return memo[idx];
        }
        // Option 1, we take s[idx] as the extra character
        int res = 1 + dp(idx + 1, s);
        // Option 2, if we can, fit a substring starting from s[idx] into one of the words in dictionary
        TrieNode node = root;
        for (int i = idx; i < s.length(); i++) {
            if (node.dict.containsKey(s.charAt(i))) {
                node = node.dict.get(s.charAt(i));
                if (node.isWord) {
                    res = Math.min(res, dp(i + 1, s));
                }
            } else {
                break;
            }
        }
        memo[idx] = res;
        return res;
    }

