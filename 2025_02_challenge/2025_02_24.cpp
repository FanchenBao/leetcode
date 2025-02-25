#include <climits>
#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
private:
  int get_bob_steps(std::unordered_map<int, std::vector<int>> &graph, int node,
                    int parent, std::unordered_map<int, int> &bob_steps,
                    int bob) {
    if (node == bob) {
      bob_steps[node] = 0;
      return 0;
    }
    for (int child : graph[node]) {
      if (child == parent)
        continue;
      int next_lvl = get_bob_steps(graph, child, node, bob_steps, bob);
      if (next_lvl >= 0) {
        bob_steps[node] = next_lvl + 1;
        return bob_steps[node];
      }
    }
    return -1;
  }

  int get_alice_max_profit(std::unordered_map<int, std::vector<int>> &graph,
                           int node, int parent, int steps,
                           std::unordered_map<int, int> &bob_steps,
                           std::vector<int> &amount) {
    int bs = bob_steps.contains(node) ? bob_steps[node] : INT_MAX;
    int cur_prof =
        steps < bs ? amount[node] : (steps == bs ? amount[node] / 2 : 0);
    int next_max_prof = INT_MIN;
    for (int child : graph[node]) {
      if (child == parent)
        continue;
      next_max_prof = std::max(
          next_max_prof, get_alice_max_profit(graph, child, node, steps + 1,
                                              bob_steps, amount));
    }
    return next_max_prof > INT_MIN ? cur_prof + next_max_prof : cur_prof;
  }

public:
  int mostProfitablePath(vector<vector<int>> &edges, int bob,
                         vector<int> &amount) {
    /*
     * LeetCode 2467
     *
     * Bob's path is determinstic, because there is only one way to go from
     * any node back to the root. We can find that path and record at which
     * step Bob reaches which node.
     *
     * Then we try all possible routes for Alice, and take into consideration
     * Bob's position when Alice reaches each node. This adjusts Alice's
     * profit. We find the max profit Alice can accumulate among all the paths
     * she can take.
     *
     * O(N), 238 ms, 33%
     */
    std::unordered_map<int, std::vector<int>> graph;
    for (auto e : edges) {
      graph[e[0]].push_back(e[1]);
      graph[e[1]].push_back(e[0]);
    }
    std::unordered_map<int, int> bob_steps;
    get_bob_steps(graph, 0, -1, bob_steps, bob);
    return get_alice_max_profit(graph, 0, -1, 0, bob_steps, amount);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
