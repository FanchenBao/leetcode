#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
  std::set<char> vowels{'a', 'e', 'i', 'o', 'u'};

private:
  int does_start_end_with_vowel(string &word) {
    // return 1 if word starts and ends with vowel, otherwise 0
    if (vowels.contains(word[0]) && vowels.contains(word[word.size() - 1]))
      return 1;
    return 0;
  }

public:
  /**
   * @brief LeetCode 2559
   *
   * If a word starts and ends in vowel, we count it as 1, otherwise 0.
   * Produce a prefix sum array of all the words, then do the query.
   *
   * O(N + M), where N = len(words), M = len(queries)
   *
   * @param words
   * @param queries
   * @return
   */
  vector<int> vowelStrings(vector<string> &words,
                           vector<vector<int>> &queries) {
    int N = words.size();
    std::vector<int> presum(N);
    presum[0] = does_start_end_with_vowel(words[0]);
    for (int i = 1; i < N; i++)
      presum[i] = presum[i - 1] + does_start_end_with_vowel(words[i]);
    std::vector<int> res;
    for (auto query : queries) {
      if (query[0] == 0)
        res.push_back(presum[query[1]]);
      else
        res.push_back(presum[query[1]] - presum[query[0] - 1]);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
