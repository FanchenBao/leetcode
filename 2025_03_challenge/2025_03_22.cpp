#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  void dfs(int node, std::vector<std::vector<int>> &graph,
           std::unordered_set<int> &seen, std::vector<int> &nodes) {
    nodes.push_back(node);
    seen.insert(node);
    for (int child : graph[node]) {
      if (!seen.contains(child)) {
        dfs(child, graph, seen, nodes);
      }
    }
  }

  int countCompleteComponents(int n, vector<vector<int>> &edges) {
    /*
     * LeetCode 2685
     *
     * DFS to find all the connected components. Then we go through each node
     * in a connected component. For the component with M number of nodes to
     * be complete, each node must have M - 1 number of children.
     *
     * O(V + E), 47 ms, 63.47%
     */
    std::vector<std::vector<int>> graph(n);
    for (auto &e : edges) {
      graph[e[0]].push_back(e[1]);
      graph[e[1]].push_back(e[0]);
    }
    std::unordered_set<int> seen;
    int res = 0;
    for (int i = 0; i < n; i++) {
      if (seen.contains(i))
        continue;
      std::vector<int> nodes;
      dfs(i, graph, seen, nodes);
      bool is_complete = true;
      for (int node : nodes) {
        if (graph[node].size() != nodes.size() - 1) {
          is_complete = false;
          break;
        }
      }
      res += (int)is_complete;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
