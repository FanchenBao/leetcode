#include <iostream>
#include <set>
#include <vector>

using namespace std;

class TrieNode {
public:
  TrieNode *children[26] = {};
  int count;

  TrieNode() { count = 0; }
};

class Solution {
public:
  int prefixCount(vector<string> &words, string pref) {
    /*
     * LeetCode 2185
     *
     * Use Trie. This is, I think, the firs time that I have implemented a
     * Trie in C++.
     *
     * O(MN + K), where M = len(words), N = len(word), K = len(pref)
     * 31 ms, 5%
     */
    // create the Trie
    TrieNode *root = new TrieNode();
    for (string word : words) {
      TrieNode *node = root;
      for (char c : word) {
        if (node->children[c - 'a'] == NULL)
          node->children[c - 'a'] = new TrieNode();
        node = node->children[c - 'a'];
        node->count++;
      }
    }
    // Query the Trie for the count of prefix
    TrieNode *node = root;
    for (char c : pref) {
      if (node->children[c - 'a'] == NULL)
        return 0;
      node = node->children[c - 'a'];
    }
    return node->count;
  }
};

class Solution2 {
public:
  int prefixCount(vector<string> &words, string pref) {
    /*
     * This should be a faster solution.
     * 6 ms, 7.26%
     */
    int res = 0;
    for (string word : words) {
      if (word.starts_with(pref))
        res++;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
