#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  string addSpaces(string s, vector<int> &spaces) {
    /*
     * LeetCode 2109
     *
     * It's simple, which is perfect for me at the current stage of practicing
     * C++.
     *
     * O(N), 16 ms, faster than 79.82%
     *
     * UPDATE: let's reserve the size for the result, thus speeding things up
     * because there is no need to resize the string.
     *
     * O(N), 15 ms, faster than 85.84%
     */
    int space_idx = 0;
    std::string res;
    res.reserve(s.size() + spaces.size());
    for (int i = 0; i < s.length(); i++) {
      if (space_idx == spaces.size() || i != spaces[space_idx]) {
        res += s[i];
      } else {
        res += ' ';
        res += s[i];
        space_idx++;
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
