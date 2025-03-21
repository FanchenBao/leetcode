#include <iostream>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class DSU {
public:
  std::vector<int> par;
  std::vector<int> rnk;

  DSU(int N) {
    for (int i = 0; i < N; i++) {
      par.push_back(i);
      rnk.push_back(0);
    }
  }

  int _find(int x) {
    if (par[x] != x)
      par[x] = _find(par[x]);
    return par[x];
  }

  bool _union(int x, int y) {
    int px = _find(x), py = _find(y);
    if (px == py) // already unioned
      return false;
    if (rnk[px] > rnk[py]) {
      par[py] = px;
    } else if (rnk[px] < rnk[py]) {
      par[px] = py;
    } else {
      par[py] = px;
      rnk[px]++;
    }
    return true;
  }
};

class Solution {
public:
  vector<int> minimumCost(int n, vector<vector<int>> &edges,
                          vector<vector<int>> &query) {
    /*
     * LeetCode 3108
     *
     * The key insights are two folds.
     *
     * First, if the two nodes in the query below to a connected graph, we can
     * traverse all the edges in teh graph to go from one node to the other.
     * Second, the bitwise AND of all the edge weights in a connected graph
     * produces the minimum cost.
     *
     * Thus, we use DSU to establish connectedness, and compute the bitwise
     * AND of all the edges in a connected graph. When we do a query, we check
     * if the two nodes are in the same connected graph. And the answer is
     * yes, we use the bitwise AND of all the edges in the same connected graph
     * as the min cost for the query.
     *
     * 179 ms, 24.67%
     *
     * Update: use reference for the for-loop. 91 ms, 52.25%
     */
    DSU dsu = DSU(n);
    for (auto e : edges) {
      dsu._union(e[0], e[1]);
    }
    std::unordered_map<int, int> path_and;
    for (auto &e : edges) {
      int p = dsu._find(e[0]);
      if (path_and.contains(p)) {
        path_and[p] &= e[2];
      } else {
        path_and[p] = e[2];
      }
    }
    std::vector<int> res;
    for (auto &q : query) {
      int p0 = dsu._find(q[0]);
      int p1 = dsu._find(q[1]);
      if (p0 == p1)
        res.push_back(path_and[p0]);
      else
        res.push_back(-1);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  /* std::cout << sol.checkIfExist(arr) << std::endl; */
}
