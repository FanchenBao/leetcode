#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

class DSU {
public:
  std::vector<int> par;
  std::vector<int> rnk;

  DSU(int total) {
    par = std::vector<int>(total, 0);
    for (int i = 0; i < total; i++)
      par[i] = i;
    rnk = std::vector<int>(total, 0);
  }

  int _find(int x) {
    if (par[x] != x)
      par[x] = _find(par[x]);
    return par[x];
  }

  bool _union(int x, int y) {
    int px = _find(x), py = _find(y);
    if (px == py)
      return false;
    if (rnk[px] > rnk[py]) {
      par[py] = px;
    } else if (rnk[px] < rnk[py]) {
      par[px] = py;
    } else {
      rnk[px]++;
      par[py] = px;
    }
    return true;
  }
};

class Solution {
public:
  int largestIsland(vector<vector<int>> &grid) {
    /*
     * LeetCode 827
     *
     * Use union-find to obtain all the disconnected islands. Then go through
     * each water, turn it into an island and see which disconnected islands
     * can be connected.
     *
     * O(MN * alpha(MN)), 599 ms, 17.66%
     */
    std::vector<std::pair<int, int>> dirs{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int M = grid.size(), N = grid[0].size();
    DSU dsu(M * N);
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        if (grid[i][j] == 0)
          continue;
        for (auto [di, dj] : dirs) {
          int ni = i + di, nj = j + dj;
          if (0 <= ni && ni < M && 0 <= nj && nj < N && grid[ni][nj] == 1)
            dsu._union(i * N + j, ni * N + nj);
        }
      }
    }
    std::map<int, int> island_size;
    for (int i = 0; i < M * N; i++) {
      island_size[dsu._find(i)]++;
    }
    int res = 0;
    for (const auto &p : island_size)
      res = std::max(res, p.second);
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        if (grid[i][j] == 0) {
          // if we turn grid[i][j] into an island, what would be the max number
          // of lands generated
          std::set<int> islands;
          for (auto [di, dj] : dirs) {
            int ni = i + di, nj = j + dj;
            if (0 <= ni && ni < M && 0 <= nj && nj < N && grid[ni][nj] == 1)
              islands.insert(dsu._find(ni * N + nj));
          }
          int cur_size = 0;
          for (int isl : islands)
            cur_size += island_size[isl];
          res = std::max(res, cur_size + 1);
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
