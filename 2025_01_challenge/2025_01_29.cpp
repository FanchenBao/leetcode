#include <iostream>
#include <map>
#include <set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  bool has_cycle(int node, int parent, std::vector<std::set<int>> &graph,
                 std::set<int> &visited) {
    if (visited.contains(node))
      return true;
    visited.insert(node);
    for (int child : graph[node]) {
      if (child != parent && has_cycle(child, node, graph, visited))
        return true;
    }
    return false;
  }

  vector<int> findRedundantConnection(vector<vector<int>> &edges) {
    /*
     * LeetCode 684
     *
     * Since the size of edges is not more than 1000, we can brute force this
     * by removing each edge from right to left and check whether the remaining
     * graph is connected and has cycle.
     *
     * O(N^2), 8 ms, 15.35%
     */
    int N = edges.size();
    std::vector<std::set<int>> graph(N + 1, std::set<int>());
    for (auto e : edges) {
      graph[e[0]].insert(e[1]);
      graph[e[1]].insert(e[0]);
    }
    for (int i = N - 1; i >= 0; i--) {
      // remove edges[i]
      int a = edges[i][0], b = edges[i][1];
      graph[a].erase(b);
      graph[b].erase(a);
      std::set<int> visited;
      if (!has_cycle(1, 0, graph, visited) && visited.size() == N)
        return edges[i];
      graph[a].insert(b);
      graph[b].insert(a);
    }
    return std::vector<int>(); // should not reach here
  }
};

class Solution2 {
public:
  int dfs(int node, int parent, std::vector<std::vector<int>> &graph,
          std::map<std::pair<int, int>, int> &edge_indices,
          std::vector<int> &path, std::set<int> &visited) {
    if (visited.contains(node)) {
      int idx = -1;
      for (int i = path.size() - 1; path[i] != node; i--) {
        auto edge = std::make_pair(path[i], path[i - 1]);
        idx = std::max(idx, edge_indices[edge]);
      }
      return idx;
    }
    visited.insert(node);
    path.push_back(node);
    for (int child : graph[node]) {
      if (child != parent) {
        int idx = dfs(child, parent, graph, edge_indices, path, visited);
        if (idx >= 0)
          return idx;
      }
    }
    // backtracking
    path.pop_back();
    visited.erase(node);
    return -1;
  }

  vector<int> findRedundantConnection(vector<vector<int>> &edges) {
    /*
     * It is my educated guess that given a connected tree, adding one
     * additional edge can produce at most one cycle.
     * Thus, we can DFS the graph to find the cycle and see which edge in
     * the cycle appears the latest in the edges array.
     */
    int N = edges.size();
    std::vector<std::vector<int>> graph(N + 1, std::vector<int>());
    std::map<std::pair<int, int>, int> edge_indices;
    for (int i = 0; i < N; i++) {
      int a = edges[i][0], b = edges[i][1];
      graph[a].push_back(b);
      graph[b].push_back(a);
      edge_indices[{a, b}] = i, edge_indices[{b, a}] = i;
    }
    std::vector<int> path;
    std::set<int> visited;
    int idx = dfs(1, 0, graph, edge_indices, path, visited);
    return edges[idx];
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
