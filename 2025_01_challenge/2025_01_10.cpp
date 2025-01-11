#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<string> wordSubsets(vector<string> &words1, vector<string> &words2) {
    /*
     * LeetCode 916
     *
     * Create a max frequency counter for all the word in words2. Then for
     * each word in words1, if the max frequency counter's values are smaller
     * or equal to the frequency of the current word, we have a subset.
     *
     * O(MP + NQ), where M = len(words2), P is the average length of word in
     * words2. N = len(words1), Q is the average length of word in words1.
     *
     * 18 ms, 78.54%
     */
    std::vector<string> res;
    std::vector<int> words2_max_freq(26);
    std::vector<int> word_freq(26);
    for (string word : words2) {
      for (char c : word)
        word_freq[c - 'a']++;
      for (int i = 0; i < 26; i++)
        words2_max_freq[i] = std::max(words2_max_freq[i], word_freq[i]);
      std::fill(word_freq.begin(), word_freq.end(), 0);
    }
    for (string word : words1) {
      for (char c : word)
        word_freq[c - 'a']++;
      bool is_subset = true;
      for (int i = 0; i < 26; i++) {
        if (word_freq[i] < words2_max_freq[i]) {
          is_subset = false;
          break;
        }
      }
      if (is_subset)
        res.push_back(word);
      std::fill(word_freq.begin(), word_freq.end(), 0);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
