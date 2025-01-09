#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
private:
  int is_pref_suff(string &w1, string &w2) {
    int N = w1.size(), M = w2.size();
    if (N > w2.size())
      return 0;
    // check prefix and suffix
    for (int i = 0; i < N; i++) {
      if (w1[i] != w2[i] || w1[N - i - 1] != w2[M - i - 1])
        return 0;
    }
    return 1;
  }

public:
  int countPrefixSuffixPairs(vector<string> &words) {
    /*
     * LeetCode 3042
     *
     * Brute force
     *
     * O(K^2 * N), where K = len(words) and N is the average length of word
     */
    int res = 0;
    for (int i = 0; i < words.size(); i++) {
      for (int j = i + 1; j < words.size(); j++) {
        res += is_pref_suff(words[i], words[j]);
      }
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
