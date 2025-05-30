#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  std::vector<std::vector<int>>
  build_graph(const std::vector<std::vector<int>> &edges) {
    std::vector<std::vector<int>> graph(edges.size() + 1);
    for (const auto &e : edges) {
      graph[e[0]].push_back(e[1]);
      graph[e[1]].push_back(e[0]);
    }
    return graph;
  }

  void GetParity(int node, int p, const std::vector<std::vector<int>> &graph,
                 std::vector<int> &parity) {
    if (parity[node] >= 0)
      return;
    parity[node] = p;
    for (int child : graph[node])
      GetParity(child, p ^ 1, graph, parity);
  }

  vector<int> maxTargetNodes(vector<vector<int>> &edges1,
                             vector<vector<int>> &edges2) {
    /*
     * LeetCode 3373
     *
     * Traverse the tree to find the parity of each node. Adjacent nodes have
     * different parity. If the original node has parity 1, the number of its
     * target nodes is the total count of nodes with parity 1. The same goes
     * for parity zero.
     *
     * For the second tree, we do the same parity and find the parity with
     * the more number of nodes (essentially, after we build an edge, we need
     * to go from parity 0 to parity 1 or vice versa on the second tree, but
     * this does not matter, because eventually all we need is the max number
     * of nodes with either parity).
     *
     * O(N), 288 ms, 87.07%
     */
    int N = edges1.size() + 1;
    int M = edges2.size() + 1;
    auto graph1 = build_graph(edges1);
    auto graph2 = build_graph(edges2);
    std::vector<int> parity1(N, -1);
    std::vector<int> parity2(M, -1);
    GetParity(0, 0, graph1, parity1);
    GetParity(0, 0, graph2, parity2);
    int num_one_1 = 0, num_one_2 = 0;
    for (int p : parity1)
      num_one_1 += p == 1;
    int num_zero_1 = N - num_one_1;
    for (int p : parity2)
      num_one_2 += p == 1;
    int num_zero_2 = M - num_one_2;
    std::vector<int> res;
    for (int i = 0; i < N; i++) {
      res.push_back((parity1[i] == 0 ? num_zero_1 : num_one_1) +
                    std::max(num_zero_2, num_one_2));
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
