#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool areAlmostEqual(string s1, string s2) {
    /*
     * LeetCode 1790
     *
     * Record the indices where s1 and s2 differ. If there are more than two
     * or less than two differences, return false.
     *
     * Otherwise, check whether a swap on the two indices would make the two
     * strings equal.
     */
    if (s1 == s2)
      return true;
    int lo = -1, hi = -1;
    for (int i = 0; i < s1.size(); i++) {
      if (s1[i] != s2[i]) {
        if (lo < 0)
          lo = i;
        else if (hi < 0)
          hi = i;
        else
          return false;
      }
    }
    return (hi >= 0) && (s1[lo] == s2[hi]) && (s1[hi] == s2[lo]);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
