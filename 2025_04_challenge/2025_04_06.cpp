#include <algorithm>
#include <iostream>
#include <set>
#include <sys/syslimits.h>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution1 {
public:
  void dfs(int idx, std::vector<std::vector<int>> &graph,
           std::vector<int> &nums, std::vector<std::vector<int>> &dp) {
    dp[idx].push_back(nums[idx]);
    int max_child_size = 0;
    int max_child = -1;
    for (int child : graph[idx]) {
      if (dp[child].empty()) {
        dfs(child, graph, nums, dp);
      }
      if (dp[child].size() > max_child_size) {
        max_child_size = dp[child].size();
        max_child = child;
      }
    }
    if (max_child >= 0) {
      for (int e : dp[max_child])
        dp[idx].push_back(e);
    }
  }

  vector<int> largestDivisibleSubset(vector<int> &nums) {
    /*
     * LeetCode 368
     *
     * Sort nums and then produce a group where the child value is multiples
     * of the node value. Then we traverse the map from the lowest node value
     * and a longest path
     *
     * O(N^2), 30 ms, 10%
     */
    std::sort(nums.begin(), nums.end());
    int N = nums.size();
    std::vector<std::vector<int>> graph(N);
    for (int i = 0; i < N; i++) {
      for (int j = i + 1; j < N; j++) {
        if (nums[j] % nums[i] == 0)
          graph[i].push_back(j);
      }
    }
    std::vector<int> path;
    std::vector<std::vector<int>> dp(
        N); // dp[i] is the longest path starting from nums[i]
    for (int i = 0; i < N; i++) {
      if (dp[i].empty())
        dfs(i, graph, nums, dp);
    }
    std::vector<int> res;
    for (auto p : dp) {
      if (p.size() > res.size())
        res = p;
    }
    return res;
  }
};

class Solution {
public:
  void dfs(int idx, std::vector<std::vector<int>> &graph,
           std::vector<std::vector<int>> &dp) {
    dp[idx] = {idx, 1};
    int max_child_size = 0;
    int max_child = -1;
    for (int child : graph[idx]) {
      if (dp[child].empty()) {
        dfs(child, graph, dp);
      }
      if (dp[child][1] > max_child_size) {
        max_child_size = dp[child][1];
        max_child = child;
      }
    }
    if (max_child >= 0) {
      dp[idx] = {max_child, dp[max_child][1] + 1};
    }
  }

  vector<int> largestDivisibleSubset(vector<int> &nums) {
    /*
     * The same DP solution but hopefully with better performance.
     *
     * 26 ms 11.16%
     */
    std::sort(nums.begin(), nums.end());
    int N = nums.size();
    std::vector<std::vector<int>> graph(N);
    for (int i = 0; i < N; i++) {
      for (int j = i + 1; j < N; j++) {
        if (nums[j] % nums[i] == 0)
          graph[i].push_back(j);
      }
    }
    std::vector<int> path;
    // dp[i] = [next child of the longest path, path size]
    std::vector<std::vector<int>> dp(N);
    for (int i = 0; i < N; i++) {
      if (dp[i].empty())
        dfs(i, graph, dp);
    }

    int node = -1, max_size = 0;
    for (int i = 0; i < N; i++) {
      if (dp[i][1] > max_size) {
        max_size = dp[i][1];
        node = i;
      }
    }

    std::vector<int> res;
    while (!dp[node].empty() && dp[node][0] != node) {
      res.push_back(nums[node]);
      node = dp[node][0];
    }
    res.push_back(nums[node]);
    return res;
  }
};

int main() {
  std::vector<int> nums{1, 2, 3};
  Solution sol;
  sol.largestDivisibleSubset(nums);
}
