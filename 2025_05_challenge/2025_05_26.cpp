#include <algorithm>
#include <iostream>
#include <set>
#include <sys/signal.h>
#include <variant>
#include <vector>

using namespace std;

class Solution {
public:
  bool dfs(int node, const std::vector<std::vector<int>> &graph,
           const std::string &colors, std::vector<bool> &visited,
           std::vector<bool> &in_path, std::vector<int> &counter,
           int &max_count) {
    if (in_path[node])
      return false;
    counter[colors[node] - 'a']++;
    visited[node] = true;
    in_path[node] = true;

    if (graph[node].size() > 0) {
      for (int child : graph[node]) {
        if (!dfs(child, graph, colors, visited, in_path, counter, max_count))
          return false;
      }
    } else {
      max_count = std::max(*std::max_element(counter.begin(), counter.end()),
                           max_count);
    }
    // backtrack (do not back track visited, it is for global use)
    counter[colors[node] - 'a']--;
    in_path[node] = false;
    return true;
  }

  int largestPathValue(string colors, vector<vector<int>> &edges) {
    /*
     * LeetCode 1857
     *
     * Since the graph is directed, if it does not contain a cycle, there must
     * exists a root who has zero indegrees. We will use this fact to find
     * all the roots. Then, we will perform simple DFS to find the max color
     * count for each path and return the max count.
     *
     * TLE
     */
    int N = colors.size();
    std::vector<int> indegrees(N);
    std::vector<std::vector<int>> graph(N);
    for (const auto &e : edges) {
      indegrees[e[1]]++;
      graph[e[0]].push_back(e[1]);
    }

    std::vector<bool> visited(N, false); // global visited state
    std::vector<bool> in_path(N, false); // to be used in each DFS path
    std::vector<int> counter(26);
    int res = 0;
    for (int i = 0; i < N; i++) {
      if (!visited[i] && indegrees[i] == 0) {
        if (!dfs(i, graph, colors, visited, in_path, counter, res))
          return -1; // cycle identified
      }
    }
    for (int i = 0; i < N; i++) {
      if (!visited[i]) // some rode has not been visited after all the roots
                       // have been visited. That means the unvisited nodes
                       // cannot be reached by a root, indicating that it is in
                       // a cycle.
        return -1;
    }

    return res;
  }
};

int main() {
  // std::string colors = "abaca";
  // std::vector<std::vector<int>> edges{{0, 1}, {0, 2}, {2, 3}, {3, 4}};
  std::string colors = "bbbhb";
  std::vector<std::vector<int>> edges{{0, 2}, {3, 0}, {1, 3}, {4, 1}};
  Solution sol;
  std::cout << sol.largestPathValue(colors, edges) << std::endl;
}
