#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <set>
#include <unordered_map>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  std::unordered_map<char, int> DIRS{{'S', -1}, {'N', 1}, {'E', 1}, {'W', -1}};
  std::unordered_map<char, char> OPPS{
      {'W', 'E'}, {'E', 'W'}, {'N', 'S'}, {'S', 'N'}};

  int GetMaxDistance(const std::string &s, char xdir, char ydir, int k) {
    int x = 0, y = 0, res = 0;
    for (char c : s) {
      if (c == xdir) {
        x += DIRS[c];
      } else if (c == OPPS[xdir]) {
        if (k > 0) {
          x += DIRS[xdir];
          k--;
        } else {
          x += DIRS[c];
        }
      } else if (c == ydir) {
        y += DIRS[c];
      } else {
        if (k > 0) {
          y += DIRS[ydir];
          k--;
        } else {
          y += DIRS[c];
        }
      }
      res = std::max(res, std::abs(x) + std::abs(y));
    }
    return res;
  }

  int maxDistance(string s, int k) {
    /*
     * LeetCode 3443 (Hint)
     *
     * This solution is inspired by the editorial. We will brute force four
     * directions: NE, NW, SE, SW. For example, if we go NE, then any S shall
     * be changed to N and any W shall be changed to E. We accumulate k
     * changes as early as possible and find out what the max distance would
     * be. Repeat this for the other directions.
     *
     * O(N), 518 ms, 5.15%
     */
    std::vector<int> cands{
        GetMaxDistance(s, 'E', 'N', k),
        GetMaxDistance(s, 'W', 'N', k),
        GetMaxDistance(s, 'W', 'S', k),
        GetMaxDistance(s, 'E', 'S', k),
    };
    return *std::max_element(cands.begin(), cands.end());
  }
};

int main() {
  std::string s = "NWSE";
  int k = 1;
  Solution sol;
  std::cout << sol.maxDistance(s, k) << std::endl;
}
