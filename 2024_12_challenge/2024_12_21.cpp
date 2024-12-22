#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
private:
  int dfs(int root, int par, std::vector<std::set<int>> &graph,
          std::vector<int> &subtree_sum, int k) {
    for (int c : graph[root]) {
      if (c == par)
        continue;
      if (subtree_sum[c] % k == 0 &&
          (subtree_sum[root] - subtree_sum[c] + k) % k == 0) {
        subtree_sum[root] = (subtree_sum[root] - subtree_sum[c] + k) % k;
        graph[root].erase(c);
        graph[c].erase(root);
        return dfs(c, root, graph, subtree_sum, k) +
               dfs(root, par, graph, subtree_sum, k);
      }
    }
    // No split on the current level. Find splits in children's level
    int comp = 0;
    for (int c : graph[root]) {
      if (c != par) {
        subtree_sum[c] = subtree_sum[root];
        comp += dfs(c, root, graph, subtree_sum, k) - 1;
      }
    }
    return comp + 1;
  }

  void get_subtree_sum(int node, int par, std::vector<std::set<int>> &graph,
                       std::vector<int> &values, int k) {
    for (int c : graph[node]) {
      if (c != par) {
        get_subtree_sum(c, node, graph, values, k);
        values[node] = (int)((long)values[node] + values[c]) % k;
      }
    }
  }

public:
  int maxKDivisibleComponents(int n, vector<vector<int>> &edges,
                              vector<int> &values, int k) {
    /*
     * LeetCode 2872
     *
     * First choose any node as the root, perform DFS to find the subtree sums.
     *
     * Then, DFS again. For each node, if cutting any of its edges results in
     * two components where the sum of both are divisible by k, we will honor
     * this cut. It can be proven that this greedy approach works (because if
     * we choose not to cut and claim that the result gives us the most number
     * of components, we can always make that cut again to obtain even more
     * components. Hence, cutting any edge that satisfies the requirement is
     * a good strategy.)
     *
     * O(N)
     */
    std::vector<std::set<int>> graph(n, std::set<int>());
    for (auto edge : edges) {
      int a = edge[0];
      int b = edge[1];
      graph[a].insert(b);
      graph[b].insert(a);
    }
    get_subtree_sum(0, -1, graph, values,
                    k); // this turns values into subtree sums
    return dfs(0, -1, graph, values, k);
  }
};

class Solution2 {
private:
  int dfs(int root, int par, std::vector<int> graph[], std::vector<int> &values,
          int k, int &res) {
    int sum = values[root];
    for (int c : graph[root]) {
      if (c != par) {
        int c_sum = dfs(c, root, graph, values, k, res);
        sum = (sum + c_sum) % k;
      }
    }
    if (sum % k == 0)
      res += 1;
    return sum;
  }

public:
  int maxKDivisibleComponents(int n, vector<vector<int>> &edges,
                              vector<int> &values, int k) {
    /*
     * This is the DFS solution from the official solution. It uses the
     * same idea as solution1, but its implementation is much simpler
     * because we can decide on the component as we calculate the subtree
     * sum. We still need the greedy, but we can count a component the
     * moment a subtree sum becomes divisible by k. In other words, we
     * don't need a second pass.
     *
     * Also, we can use a trick to make the graph representation faster.
     *
     * O(N), 139 ms, faster than 51.27%
     */
    std::vector<int> graph[n];
    for (auto edge : edges) {
      int a = edge[0];
      int b = edge[1];
      graph[a].push_back(b);
      graph[b].push_back(a);
    }
    int res = 0;
    dfs(0, -1, graph, values, k, res);
    return res;
  }
};

int main() {
  int n = 5;
  std::vector<std::vector<int>> edges{{0, 2}, {1, 2}, {1, 3}, {2, 4}};
  std::vector<int> values{1, 8, 1, 4, 4};
  int k = 6;
  Solution sol;
  std::cout << sol.maxKDivisibleComponents(n, edges, values, k) << std::endl;
}
