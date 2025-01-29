#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  std::vector<std::pair<int, int>> dirs{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

  int dfs(int i, int j, std::vector<std::vector<int>> &grid) {
    if (grid[i][j] == 0)
      return 0;
    // return the sum of the connected cell values starting from grid[i][j]
    int total = grid[i][j];
    int M = grid.size(), N = grid[0].size();
    grid[i][j] = 0; // mark as visited
    for (auto [di, dj] : dirs) {
      int ni = i + di, nj = j + dj;
      if (0 <= ni && ni < M && 0 <= nj && nj < N && grid[ni][nj] > 0)
        total += dfs(ni, nj, grid);
    }
    return total;
  }

  int findMaxFish(vector<vector<int>> &grid) {
    /*
     * LeetCode 2658
     *
     * Essentially finding the max sum of each group of connected cells.
     *
     * O(MN), 0 ms, 100%
     */
    int M = grid.size(), N = grid[0].size();
    int res = 0;
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++)
        res = std::max(res, dfs(i, j, grid));
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
