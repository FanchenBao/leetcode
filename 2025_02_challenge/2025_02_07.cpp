#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> queryResults(int limit, vector<vector<int>> &queries) {
    /*
     * LeetCode 3160
     *
     * Use two hashmaps. One keeps a record of the ball's current color, while
     * the other the number of balls with each specific color.
     *
     * At each query, we update the ball's color and update the color counter
     * as well. If a color has no ball associated with it, it will be removed
     * from the counter. The answer to each query is the size of the counter
     * at the moment.
     *
     * O(N), 292 ms, 10%
     */
    std::map<int, int> ball_color;
    std::map<int, int> color_count;
    std::vector<int> res;
    for (auto q : queries) {
      int ball = q[0], color = q[1];
      if (ball_color[ball]) {
        int old_color = ball_color[ball];
        color_count[old_color]--;
        if (!color_count[old_color])
          color_count.erase(old_color);
      }
      ball_color[ball] = color;
      color_count[color]++;
      res.push_back(color_count.size());
    }
    return res;
  }
};

class Solution2 {
public:
  vector<int> queryResults(int limit, vector<vector<int>> &queries) {
    /*
     * Update: use unordered_map to see if performance would improve.
     *
     * This one scores 175 ms, 34%
     */
    std::unordered_map<int, int> ball_color;
    std::unordered_map<int, int> color_count;
    std::vector<int> res;
    for (auto q : queries) {
      int ball = q[0], color = q[1];
      if (ball_color[ball]) {
        int old_color = ball_color[ball];
        color_count[old_color]--;
        if (!color_count[old_color])
          color_count.erase(old_color);
      }
      ball_color[ball] = color;
      color_count[color]++;
      res.push_back(color_count.size());
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
