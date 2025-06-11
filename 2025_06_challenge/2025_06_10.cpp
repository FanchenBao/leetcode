#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maxDifference(string s) {
    /*
     * LeetCode 3442
     */
    std::vector<int> counter(26);
    for (char c : s)
      counter[c - 'a']++;
    int min_e = s.size() + 1, max_o = 0;
    for (int c : counter) {
      if (c > 0) {
        if (c % 2 == 1) {
          max_o = std::max(max_o, c);
        } else {
          min_e = std::min(min_e, c);
        }
      }
    }
    return max_o - min_e;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
