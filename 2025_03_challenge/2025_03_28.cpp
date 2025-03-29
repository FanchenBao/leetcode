#include <deque>
#include <iostream>
#include <queue>
#include <set>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> maxPoints(vector<vector<int>> &grid, vector<int> &queries) {
    /*
     * LeetCode 2503
     *
     * DFS but with two queues. One keeps track of the front line. The other
     * expands the front line.
     *
     * TLE.
     */
    int M = grid.size(), N = grid[0].size();
    std::vector<std::pair<int, int>> DIRS{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    std::vector<std::vector<bool>> seen(M, std::vector<bool>(N));
    std::vector<std::pair<int, int>> sorted_queries;
    for (int i = 0; i < queries.size(); i++)
      sorted_queries.push_back({queries[i], i});
    std::sort(sorted_queries.begin(), sorted_queries.end());
    std::vector<int> res(queries.size());
    std::vector<std::pair<int, int>> front_line;
    front_line.push_back({0, -1});
    int pre = 0;
    for (auto p : sorted_queries) {
      int k = p.first, idx = p.second;
      res[idx] += pre;
      std::deque<std::pair<int, int>> queue(front_line.begin(),
                                            front_line.end());
      std::vector<std::pair<int, int>> next_front_line;
      while (!queue.empty()) {
        auto cur = queue.front();
        queue.pop_front();
        bool is_obsolete = true;
        for (auto delta : DIRS) {
          int di = delta.first, dj = delta.second;
          int ni = cur.first + di, nj = cur.second + dj;
          if (ni >= 0 && ni < M && nj >= 0 && nj < N && grid[ni][nj] >= 0) {
            if (grid[ni][nj] < k) {
              res[idx]++;
              grid[ni][nj] = -1;
              queue.push_back({ni, nj});
            } else {
              is_obsolete = false;
            }
          }
        }
        if (!is_obsolete)
          next_front_line.push_back(cur);
      }
      front_line = next_front_line;
      pre = res[idx];
    }
    return res;
  }
};

template <> struct hash<std::pair<int, int>> {
  size_t operator()(const std::pair<int, int> &p) const {
    // Combine hash values of the pair elements using XOR and bit shifts
    return std::hash<int>()(p.first) ^ (std::hash<int>()(p.second) << 1);
  }
};

class Solution2 {
public:
  void dfs(int i, int j, std::vector<std::vector<int>> &grid,
           std::priority_queue<std::pair<int, std::pair<int, int>>> &front_line,
           std::unordered_set<std::pair<int, int>> &seen, int k) {
    std::vector<std::pair<int, int>> DIRS{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    if (seen.contains({i, j}))
      return;
    if (grid[i][j] >= k) {
      front_line.push({-grid[i][j], {i, j}});
      return;
    }
    seen.insert({i, j});
    for (auto d : DIRS) {
      int ni = i + d.first, nj = j + d.second;
      if (ni >= 0 && ni < grid.size() && nj >= 0 && nj < grid[0].size() &&
          !seen.contains({ni, nj})) {
        dfs(ni, nj, grid, front_line, seen, k);
      }
    }
  }

  vector<int> maxPoints(vector<vector<int>> &grid, vector<int> &queries) {
    /*
     * Use priority queue to keep track of the front line.
     *
     * Translated from my previous solution in Dec 20, 2022
     */
    int M = grid.size(), N = grid[0].size();
    std::unordered_set<std::pair<int, int>> seen;
    std::vector<int> res(queries.size());

    std::vector<std::pair<int, int>> sorted_queries;
    for (int i = 0; i < queries.size(); i++)
      sorted_queries.push_back({queries[i], i});
    std::sort(sorted_queries.begin(), sorted_queries.end());

    std::priority_queue<std::pair<int, std::pair<int, int>>>
        front_line; // uncharted front for the current iteration
    front_line.push({-grid[0][0], {0, 0}});
    for (auto p : sorted_queries) {
      int k = p.first, idx = p.second;
      while (!front_line.empty()) {
        auto cur = front_line.top();
        int i = cur.second.first, j = cur.second.second;
        if (grid[i][j] >= k)
          break;
        front_line.pop();
        dfs(i, j, grid, front_line, seen, k);
      }
      res[idx] = seen.size();
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
