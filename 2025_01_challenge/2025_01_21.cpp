#include <climits>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long gridGame(vector<vector<int>> &grid) {
    /*
     * LeetCode 2017
     *
     * Technically, this problem can be generalized with any M x N grid and
     * each step can take all four directions. If that is the case, we can
     * solve it using Dijkstra.
     *
     * However, in the current problem, we have two restrictions. One is the
     * number of rows and the other is the two directions that we allowed to
     * move. This means, for each robot, it only has one chance to decide where
     * to switch from the top to the bottom row. Thus, for robot 1, all we
     * need to do is to locate the position such that the switch would produce
     * the min points for robot 2.
     *
     * We can create a prefix sum for the bottom and suffix sum for the top
     * find the min points for robot 2
     *
     * O(N), 0 ms, 100%
     */
    int N = grid[0].size();
    std::vector<long long> top(N);
    std::vector<long long> bot(N);
    // prefix sum on bottom
    bot[0] = (long long)grid[1][0];
    for (int i = 1; i < N; i++)
      bot[i] = bot[i - 1] + (long long)grid[1][i];
    // suffix sum on top
    top[N - 1] = (long long)grid[0][N - 1];
    for (int i = N - 2; i >= 0; i--)
      top[i] = top[i + 1] + (long long)grid[0][i];
    // find the pos such that robot 2 has the min points even if
    // it uses the best strategy
    long long res = LONG_MAX;
    for (int i = 0; i < N; i++) {
      long long tp = i < N - 1 ? top[i + 1] : 0;
      long long bp = i > 0 ? bot[i - 1] : 0;
      // the std::max is the robot 2 strategy
      // the std::min is the robot 1 strategy
      res = std::min(res, std::max(tp, bp));
    }
    return res;
  }
};

class Solution2 {
public:
  long long gridGame(vector<vector<int>> &grid) {
    /*
     * Solution 1 uses the correct strategy, but its implementation is
     * lacking. We can leverage accumulate() to quickly find the total
     * sum of top. Then as we traverse through the col, we remove the top
     * value to get the suffix sum. For the bottom, we just accumulate the
     * prefix sum as we go along.
     *
     * In other words, the optimal solution should have O(1) extra space
     */
    long long topsum = std::accumulate(grid[0].begin(), grid[0].end(), 0LL);
    long long botsum = 0;
    long long res = LONG_MAX;
    for (int i = 0; i < grid[0].size(); i++) {
      topsum -= grid[0][i];
      res = std::min(res, std::max(topsum, botsum));
      botsum += grid[1][i];
    }
    return res;
  }
};

int main() {
  std::vector<std::vector<int>> grid{{20, 3, 20, 17, 2, 12, 15, 17, 4, 15},
                                     {20, 10, 13, 14, 15, 5, 2, 3, 14, 3}};
  Solution sol;
  std::cout << sol.gridGame(grid) << std::endl;
}
