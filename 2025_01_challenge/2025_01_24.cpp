#include <deque>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int dfs(int node, std::vector<std::vector<int>> &graph,
          std::vector<int> &dp) {
    if (dp[node] == 2) {
      // a cycle has been found and none of the nodes in the cycle should be
      // safe
      dp[node] = 0;
      return 0;
    }
    if (dp[node] >= 0)
      return dp[node];
    dp[node] = 2; // mark as in the stack but undecided.
    for (int child : graph[node]) {
      if (dfs(child, graph, dp) == 0) {
        dp[node] = 0;
        return 0;
      }
    }
    dp[node] = 1;
    return 1;
  }

  vector<int> eventualSafeNodes(vector<vector<int>> &graph) {
    /*
     * LeetCode 802
     *
     * Use dp where dp[i] represent the status of the node. See the comments
     * in the code for what each number represents.
     *
     * We use DFS to go through the graph and fill out the dp array.
     *
     * O(N^2), 5 ms, 87.75%
     */
    int N = graph.size();
    // -1 => not visited, 0 => not safe, 1 => safe, 2 => in the stack and
    // undecided
    std::vector<int> dp(N, -1);
    for (int i = 0; i < N; i++) {
      if (graph[i].size() == 0)
        dp[i] = 1; // terminal nodes
    }
    for (int i = 0; i < N; i++)
      dfs(i, graph, dp);
    std::vector<int> res;
    for (int i = 0; i < N; i++) {
      if (dp[i] == 1)
        res.push_back(i);
    }
    return res;
  }
};

class Solution2 {
public:
  vector<int> eventualSafeNodes(vector<vector<int>> &graph) {
    /*
     * Let's practice topological sort
     *
     * 51 ms, 43.21%
     */
    int N = graph.size();
    std::vector<std::vector<int>> ancestors(N, std::vector<int>());
    std::vector<int> outdegrees(N, 0);
    for (int i = 0; i < N; i++) {
      for (int child : graph[i]) {
        outdegrees[i]++;
        ancestors[child].push_back(i);
      }
    }
    std::deque<int> queue;
    std::vector<int> res;
    for (int i = 0; i < N; i++) {
      if (outdegrees[i] == 0)
        queue.push_back(i);
    }
    while (!queue.empty()) {
      int node = queue.front();
      queue.pop_front();
      res.push_back(node);
      for (int anc : ancestors[node]) {
        outdegrees[anc]--;
        if (outdegrees[anc] == 0)
          queue.push_back(anc);
      }
    }
    std::sort(res.begin(), res.end());
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
