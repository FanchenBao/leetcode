#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool dfs(int node, const std::vector<std::vector<int>> &graph,
           const std::string &colors, std::vector<bool> &visited,
           std::vector<bool> &in_path, std::vector<std::vector<int>> &dp) {
    if (in_path[node])
      return false;
    if (visited[node])
      return true;
    visited[node] = true;
    in_path[node] = true;
    dp[node][colors[node] - 'a']++;

    for (int child : graph[node]) {
      if (!dfs(child, graph, colors, visited, in_path, dp))
        return false;
      for (int i = 0; i < 26; i++) {
        dp[node][i] = std::max(dp[node][i],
                               dp[child][i] + int((colors[node] - 'a') == i));
      }
    }
    in_path[node] = false; // backtracking to detect cycle
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
     * O(26N), 366 ms, 68.82%
     */
    int N = colors.size();
    std::vector<std::vector<int>> graph(N);
    for (const auto &e : edges) {
      graph[e[0]].push_back(e[1]);
    }

    std::vector<bool> visited(N, false); // gloabl visited
    std::vector<bool> in_path(N, false); // whether visited in a path
    std::vector<std::vector<int>> dp(
        N, std::vector<int>(26)); // dp[i][j] is the max count of color j among
                                  // all the paths in the subtree rooted at i

    int res = 0;
    for (int i = 0; i < N; i++) {
      if (!visited[i]) {
        if (!dfs(i, graph, colors, visited, in_path, dp))
          return -1; // cycle identified
        res = std::max(res, *std::max_element(dp[i].begin(), dp[i].end()));
      }
    }
    return res;
  }
};

int main() {
  std::vector<std::vector<int>> edges{{0, 1}, {0, 2}, {2, 3}, {3, 4}};
  std::string colors = "abaca";
  Solution sol;
  std::cout << sol.largestPathValue(colors, edges) << std::endl;
}
