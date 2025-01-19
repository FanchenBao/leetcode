#include <deque>
#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int res = 10000;
  std::vector<std::vector<int>> dirs{{1, 0}, {-1, 0}, {0, -1}, {0, 1}};

  int get_dir_symbol(std::vector<int> dir) {
    if (dir[0] == 0 && dir[1] == 1)
      return 1;
    if (dir[0] == 0 && dir[1] == -1)
      return 2;
    if (dir[0] == 1 && dir[1] == 0)
      return 3;
    return 4;
  }

  void backtrack(vector<vector<int>> &grid, int i, int j, int cost) {
    if (cost > res || grid[i][j] < 0)
      return;
    int M = grid.size(), N = grid[0].size();
    if (i == M - 1 && j == N - 1) {
      res = std::min(res, cost);
      return;
    }
    grid[i][j] *= -1;
    for (auto dir : dirs) {
      int ni = i + dir[0];
      int nj = j + dir[1];
      if (0 <= ni && ni < M && 0 <= nj && nj < N && grid[ni][nj] > 0) {
        int symbol = get_dir_symbol(dir);
        backtrack(grid, ni, nj, cost + (symbol + grid[i][j] == 0 ? 0 : 1));
      }
    }
    grid[i][j] *= -1;
  }

  int minCost(vector<vector<int>> &grid) {
    /*
     * LeetCode 1368
     *
     * This is naive backtrack solution. If this ones gets TLE, I will take it
     * for now and improve upon later after reading the hints.
     *
     * TLE
     */
    backtrack(grid, 0, 0, 0);
    return res;
  }
};

class Solution2 {
public:
  int get_dir_symbol(std::vector<int> dir) {
    if (dir[0] == 0 && dir[1] == 1)
      return 1;
    if (dir[0] == 0 && dir[1] == -1)
      return 2;
    if (dir[0] == 1 && dir[1] == 0)
      return 3;
    return 4;
  }

  int minCost(vector<vector<int>> &grid) {
    /*
     * I read the first hint which suggested turning this problem into a
     * graph, where the edge's cost is 1 if we need to make a change, or
     * 0 if we do not change. Then the problem becomes finding the min
     * cost to go from (0, 0) to (M - 1, N - 1). We can use Dijkstra to
     * solve this problem.
     *
     * O(MNlog(MN)), 270 ms, 5.77%
     */
    std::vector<std::vector<int>> dirs{{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
    int M = grid.size(), N = grid[0].size();
    std::vector<std::vector<int>> costs(M, std::vector<int>(N, 100000));
    std::priority_queue<std::vector<int>> max_heap; // [cost, i, j]
    max_heap.push({0, 0, 0});
    costs[0][0] = 0;
    while (!max_heap.empty()) {
      auto ele = max_heap.top();
      max_heap.pop();
      int cost = -ele[0], i = ele[1], j = ele[2];
      if (cost != costs[i][j])
        continue;
      if (i == M - 1 && j == N - 1)
        return cost;
      for (auto dir : dirs) {
        int ni = i + dir[0], nj = j + dir[1];
        if (0 <= ni && ni < M && 0 <= nj && nj < N) {
          int sym = get_dir_symbol(dir);
          int new_cost = cost + (sym == grid[i][j] ? 0 : 1);
          if (new_cost < costs[ni][nj]) {
            costs[ni][nj] = new_cost;
            max_heap.push({-new_cost, ni, nj});
          }
        }
      }
    }
    return -1; // should never reach here
  }
};

class Solution3 {
public:
  int get_dir_symbol(std::vector<int> dir) {
    if (dir[0] == 0 && dir[1] == 1)
      return 1;
    if (dir[0] == 0 && dir[1] == -1)
      return 2;
    if (dir[0] == 1 && dir[1] == 0)
      return 3;
    return 4;
  }

  int minCost(vector<vector<int>> &grid) {
    /*
     * Same as solution2. However, since the cost of each edge is at most 1,
     * we can use 0-1 bfs, which essentially is Dijkstra without using the
     * priority queue, because there is only one possibility to increase the
     * cost at each step. If the cost is 0, we put the next node to the left
     * of the queue, otherwise right.
     * O(MN), 234 ms, 6.47%
     */
    std::vector<std::vector<int>> dirs{{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
    int M = grid.size(), N = grid[0].size();
    std::vector<std::vector<int>> costs(M, std::vector<int>(N, 100000));
    std::deque<std::vector<int>> queue; // [i, j]
    queue.push_back({0, 0});
    costs[0][0] = 0;
    while (!queue.empty()) {
      auto ele = queue.front();
      queue.pop_front();
      int i = ele[0], j = ele[1];
      if (i == M - 1 && j == N - 1)
        return costs[i][j];
      for (auto dir : dirs) {
        int ni = i + dir[0], nj = j + dir[1];
        if (0 <= ni && ni < M && 0 <= nj && nj < N) {
          int sym = get_dir_symbol(dir);
          int w = sym == grid[i][j] ? 0 : 1;
          if (costs[i][j] + w < costs[ni][nj]) {
            costs[ni][nj] = costs[i][j] + w;
            if (w == 0)
              queue.push_front({ni, nj});
            else
              queue.push_back({ni, nj});
          }
        }
      }
    }
    return -1; // should never reach here
  }
};

int main() {
  std::vector<std::vector<int>> grid{{1, 1, 3}, {3, 2, 2}, {1, 1, 4}};
  Solution sol;
  std::cout << sol.minCost(grid) << std::endl;
}
