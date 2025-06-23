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

class Solution2 {
public:
  int maxDistance(string s, int k) {
    /*
     * This solution is inspired by the first solution in the editorial.
     *
     * The idea is to find the frequencies of all the directions and at each
     * step, make change to the smaller on horizontal and smaller on vertical,
     * if possible.
     *
     * Each change will make the Manhatten distance increase by 2.
     *
     * O(N), 127 ms, 34%
     */
    int nc = 0, sc = 0, wc = 0, ec = 0, res = 0;
    for (char c : s) {
      switch (c) {
      case 'N':
        nc++;
        break;
      case 'S':
        sc++;
        break;
      case 'E':
        ec++;
        break;
      case 'W':
        wc++;
        break;
      default:
        break;
      }
      int change_cnt_vert = std::min({nc, sc, k});
      int change_cnt_hori = std::min({wc, ec, k - change_cnt_vert});
      int cur = std::abs(nc - sc) + change_cnt_vert * 2 + std::abs(wc - ec) +
                change_cnt_hori * 2;
      res = std::max(res, cur);
    }
    return res;
  }
};

class Solution3 {
public:
  int maxDistance(string s, int k) {
    /*
     * This is the second solution from the editorial. We don't even have to
     * keep track of the count of each direction. We just keep track of the
     * position of the point. If there are more than k directions that can be
     * changed, the max additional Manhatten distance we can get is k * 2.
     * Also, at each step, the max possible Manhatten distance is index plus 1.
     * Thus, we can find the max possible Manhatten distance at each step
     * taking into account the max additional, if possible, or limited by the
     * max possible distance.
     *
     * O(N), 47 ms, 83%
     */
    int x = 0, y = 0, res = 0;
    for (int i = 0; i < s.size(); i++) {
      switch (s[i]) {
      case 'N':
        y++;
        break;
      case 'S':
        y--;
        break;
      case 'E':
        x++;
        break;
      case 'W':
        x--;
        break;
      default:
        break;
      }
      res = std::max(res, std::min(std::abs(x) + std::abs(y) + 2 * k, i + 1));
    }
    return res;
  }
};

int main() {
  std::string s = "NWSE";
  int k = 1;
  Solution sol;
  std::cout << sol.maxDistance(s, k) << std::endl;
}
