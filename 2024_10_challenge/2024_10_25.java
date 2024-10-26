import java.util.*;
import java.util.stream.Stream;
import java.math.*;

/**
 * Definition for a binary tree node.
 */
//class TreeNode {
//    int val;
//    TreeNode left;
//    TreeNode right;
//    TreeNode() {}
//    TreeNode(int val) { this.val = val; }
//    TreeNode(int val, TreeNode left, TreeNode right) {
//        this.val = val;
//        this.left = left;
//        this.right = right;
//    }
//}

class TrieNode {
    Map<String, TrieNode> children;
    boolean isEnd;
    TrieNode() {
        this.children = new HashMap<>();
        this.isEnd = false;
    }
}

class Solution {
    private int countChar(String s, char tgt) {
        int res = 0;
        for (char c : s.toCharArray()) {
            if (c == tgt)
                res++;
        }
        return res;
    }

    public List<String> removeSubfolders(String[] folder) {
        /*
         * LeetCode 1233
         *
         * Use Trie, but need to sort folder by the number of folders first.
         *
         * 96 ms, faster than 18.37%
         */
        List<String> res = new ArrayList<>();
        Arrays.sort(folder, (a, b) -> Integer.compare(countChar(a, '/'), countChar(b, '/')));
        TrieNode root = new TrieNode();
        for (String s : folder) {
            TrieNode node = root;
            boolean shouldIgnore = false;
            for (String f : s.split("/")) {
                if (!node.children.containsKey(f)){
                    node.children.put(f, new TrieNode());
                    node = node.children.get(f);
                } else if (!node.children.get(f).isEnd) {
                    node = node.children.get(f);
                } else {
                    shouldIgnore = true;
                    break;
                }
            }
            if (!shouldIgnore) {
                node.isEnd = true;
                res.add(s);
            }
        }
        return res;
    }
}


class Solution2 {
    private int countChar(String s, char tgt) {
        int res = 0;
        for (char c : s.toCharArray()) {
            if (c == tgt)
                res++;
        }
        return res;
    }

    public List<String> removeSubfolders(String[] folder) {
        /*
         * Use Trie, but need to sort folder by the number of folders first.
         *
         * Use auxillary array to store the folder levels so that we don't need
         * to compute it repeatedly while sorting.
         *
         * 55 ms, faster than 39.80%
         */
        List<String> res = new ArrayList<>();
        int[] folderLvls = new int[folder.length];
        Integer[] indices = new Integer[folder.length];
        for (int i = 0; i < folder.length; i++) {
            folderLvls[i] = countChar(folder[i], '/');
            indices[i] = i;
        }
        Arrays.sort(indices, (a, b) -> Integer.compare(folderLvls[a], folderLvls[b]));
        TrieNode root = new TrieNode();
        for (int i : indices) {
            String s = folder[i];
            TrieNode node = root;
            boolean shouldIgnore = false;
            for (String f : s.split("/")) {
                if (!node.children.containsKey(f)){
                    node.children.put(f, new TrieNode());
                    node = node.children.get(f);
                } else if (!node.children.get(f).isEnd) {
                    node = node.children.get(f);
                } else {
                    shouldIgnore = true;
                    break;
                }
            }
            if (!shouldIgnore) {
                node.isEnd = true;
                res.add(s);
            }
        }
        return res;
    }
}


class Solution3 {
    public List<String> removeSubfolders(String[] folder) {
        /*
         * We can sort the folder alphabetically. Silly me!!
         *
         * 71 ms, faster than 31.63%
         */
        List<String> res = new ArrayList<>();
        Arrays.sort(folder);
        TrieNode root = new TrieNode();
        for (String s : folder) {
            TrieNode node = root;
            boolean shouldIgnore = false;
            for (String f : s.split("/")) {
                if (!node.children.containsKey(f)){
                    node.children.put(f, new TrieNode());
                    node = node.children.get(f);
                } else if (!node.children.get(f).isEnd) {
                    node = node.children.get(f);
                } else {
                    shouldIgnore = true;
                    break;
                }
            }
            if (!shouldIgnore) {
                node.isEnd = true;
                res.add(s);
            }
        }
        return res;
    }
}





class Main{
    public static void main(String[] args) {
        String s = "acbbaca";
        String t = "aba";
        Solution sol = new Solution();
        System.out.println(sol.minWindow(s, t));
    }
}
