#include <climits>
#include <deque>
#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int countPaths(int n, vector<vector<int>> &roads) {
    /*
     * LeetCode 1976, Fail
     *
     * Didn't realize we can attach another array to keep track of the number
     * of times each node is visited during Dijkstra to count the paths.
     *
     * O((V + E)logV), 7 ms, 72.55%
     */
    int MOD = 1000000007;
    std::vector<std::vector<std::pair<int, long long>>> graph(n);
    for (auto &r : roads) {
      graph[r[0]].push_back({r[1], (long long)r[2]}); // {node, cost}
      graph[r[1]].push_back({r[0], (long long)r[2]});
    }
    // dijkstra to find the min time to reach n - 1 from 0
    std::vector<long long> min_time(n, LLONG_MAX);
    std::vector<int> ways(n);
    min_time[0] = 0;
    ways[0] = 1;
    std::priority_queue<std::pair<long long, int>> queue; // {cost, node}
    queue.push({0, 0});
    while (!queue.empty()) {
      auto ele = queue.top();
      queue.pop();
      long long cost = -ele.first;
      int node = ele.second;
      if (cost > min_time[node])
        continue;
      for (auto child : graph[node]) {
        if (child.second + cost < min_time[child.first]) {
          min_time[child.first] = child.second + cost;
          queue.push({-min_time[child.first], child.first});
          ways[child.first] = ways[node];
        } else if (child.second + cost == min_time[child.first]) {
          ways[child.first] = (ways[child.first] + ways[node]) % MOD;
        }
      }
    }
    return ways[n - 1];
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
