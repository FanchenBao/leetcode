#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  void dfs(int node, std::vector<std::vector<int>> &graph,
           std::vector<bool> &visited, std::vector<std::vector<bool>> &des) {
    if (visited[node])
      return;
    visited[node] = true;
    for (int child : graph[node]) {
      dfs(child, graph, visited, des);
      des[node][child] = true;
      for (int i = 0; i < des[child].size(); i++)
        des[node][i] = des[node][i] | des[child][i];
    }
  }

  vector<bool> checkIfPrerequisite(int numCourses,
                                   vector<vector<int>> &prerequisites,
                                   vector<vector<int>> &queries) {
    /*
     * LeetCode 1462
     *
     * DFS the graph and find all the descendants of each node.
     *
     * O(U + V + Q), where V = len(prerequisites), U = numCourses, Q =
     * len(queries), 71 ms, 44.39%
     */
    std::vector<std::vector<bool>> des(
        numCourses,
        std::vector<bool>(numCourses, false)); // record each node's descendants
    std::vector<bool> visited(numCourses, false);
    std::vector<std::vector<int>> graph(numCourses, std::vector<int>());
    for (auto p : prerequisites) {
      int a = p[0], b = p[1];
      graph[a].push_back(b);
    }
    for (int i = 0; i < numCourses; i++)
      dfs(i, graph, visited, des);
    // find answers
    std::vector<bool> res;
    for (auto q : queries) {
      res.push_back(des[q[0]][q[1]]);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
