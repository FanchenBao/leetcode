#include <climits>
#include <iostream>
#include <queue>
#include <set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  int countPaths(int n, vector<vector<int>> &roads) {
    /*
     * Second time doing this. Let's see if we can get it done in one shot.
     *
     * 0 ms
     */
    std::vector<std::vector<std::pair<int, int>>> graph(n);
    int MOD = 1000000007;
    for (auto const &e : roads) {
      graph[e[0]].push_back({e[1], e[2]});
      graph[e[1]].push_back({e[0], e[2]});
    }
    std::vector<long long> min_costs(n, LONG_MAX);
    std::vector<int> num_ways(n, 0);

    // each element is (cost, node)
    min_costs[0] = (long long)0;
    num_ways[0] = 1;
    std::priority_queue<std::pair<long long, int>> queue;
    queue.push({(long long)0, 0});
    while (!queue.empty()) {
      auto p = queue.top();
      queue.pop();
      long long cost = -p.first;
      int node = p.second;
      if (cost > min_costs[node])
        continue;
      for (auto pp : graph[node]) {
        int child = pp.first, c = (long long)pp.second;
        if (cost + c < min_costs[child]) {
          num_ways[child] = num_ways[node];
          min_costs[child] = cost + c;
          queue.push({-min_costs[child], child});
        } else if (cost + c == min_costs[child]) {
          num_ways[child] = (num_ways[child] + num_ways[node]) % MOD;
        }
      }
    }
    return num_ways[n - 1];
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
