#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> highestPeak(vector<vector<int>> &isWater) {
    /*
     * LeetCode 1765
     *
     * BFS, start from the water cells and plus one on its adjacent land cells.
     * Then we start from the land cells and do the same to propagate the
     * entire grid.
     *
     * O(MN), 75 ms, 74.51%
     */
    std::vector<std::pair<int, int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int M = isWater.size(), N = isWater[0].size();
    std::vector<std::vector<int>> res(M, std::vector<int>(N, INT_MAX));
    std::queue<std::pair<int, int>> queue;
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        if (isWater[i][j] == 1) {
          res[i][j] = 0;
          queue.push({i, j});
        }
      }
    }
    while (!queue.empty()) {
      auto [i, j] = queue.front();
      queue.pop();
      for (auto [di, dj] : dirs) {
        int ni = i + di, nj = j + dj;
        if (0 <= ni && ni < M && 0 <= nj && nj < N && res[ni][nj] == INT_MAX) {
          res[ni][nj] = std::min(res[ni][nj], res[i][j] + 1);
          queue.push({ni, nj});
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
