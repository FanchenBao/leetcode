#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int GetNumTargetNodes(int node, int parent, int k,
                        std::vector<std::vector<int>> &graph) {
    if (k < 0)
      return 0;
    if (k == 0)
      return 1;
    int res = 1;
    for (int child : graph[node]) {
      if (child != parent)
        res += GetNumTargetNodes(child, node, k - 1, graph);
    }
    return res;
  }

  std::vector<std::vector<int>> GetGraph(std::vector<std::vector<int>> &edges,
                                         int N) {
    std::vector<std::vector<int>> graph(N);
    for (const auto &e : edges) {
      graph[e[0]].push_back(e[1]);
      graph[e[1]].push_back(e[0]);
    }
    return graph;
  }

  vector<int> maxTargetNodes(vector<vector<int>> &edges1,
                             vector<vector<int>> &edges2, int k) {
    /*
     * LeetCode 3372
     *
     * Find each node's target node count in graph1. Then find the max
     * target node in graph2 given k - 1. The answer is the sum of the two
     * target node count for each node in graph1.
     *
     * O(N^2 + M^2), 102 ms, 97.23%
     */
    int M = edges2.size() + 1, N = edges1.size() + 1;
    auto graph1 = GetGraph(edges1, N);
    auto graph2 = GetGraph(edges2, M);
    int max_cnt_2 = 0;
    for (int i = 0; i < M; i++) {
      max_cnt_2 = std::max(max_cnt_2, GetNumTargetNodes(i, -1, k - 1, graph2));
    }
    std::vector<int> res(N);
    for (int i = 0; i < N; i++) {
      res[i] = GetNumTargetNodes(i, -1, k, graph1) + max_cnt_2;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
