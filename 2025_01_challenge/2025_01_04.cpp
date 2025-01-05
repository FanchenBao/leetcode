#include <climits>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int countPalindromicSubsequence(string s) {
    /*
     * LeetCode 1930
     *
     * We find the left and right most indices for a given letter, then count
     * the number of unique letters in between. The answer is the sum of all
     * those unique letters.
     *
     * O(N + 26N), 71 ms, 93.87%
     */
    std::vector<std::vector<int>> indices(26,
                                          std::vector<int>{(int)s.size(), -1});
    for (int i = 0; i < s.size(); i++) {
      int j = s[i] - 'a';
      indices[j][0] = std::min(indices[j][0], i);
      indices[j][1] = std::max(indices[j][1], i);
    }
    int res = 0;
    for (auto pair : indices) {
      int lo = pair[0], hi = pair[1];
      if (hi - lo >= 2) {
        std::vector<bool> seen(26, false);
        for (int i = lo + 1; i <= hi - 1; i++) {
          if (!seen[s[i] - 'a']) {
            res++;
            seen[s[i] - 'a'] = true;
          }
        }
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
