#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  string removeOccurrences(string s, string part) {
    /*
     * LeetCode 1910
     *
     * Use stack, but we implement it in-place with indices.
     *
     * O(NM), where N = len(s), M = len(part), 0 ms, 100%
     */
    int i = 0;
    int N = s.size(), M = part.size();
    for (int j = 0; j < N; j++) {
      s[i] = s[j];
      if (i >= M - 1) {
        // check if the suffix matches part
        bool matches = true;
        for (int k = i - M + 1; k <= i; k++) {
          if (s[k] != part[k - i + M - 1]) {
            matches = false;
            break;
          }
        }
        if (matches)
          i -= M;
      }
      i++;
    }
    return s.substr(0, i);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
