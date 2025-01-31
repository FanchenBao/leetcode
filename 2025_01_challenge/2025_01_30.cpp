#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int bfs(int start, int n, std::vector<std::vector<int>> &graph,
          std::vector<int> &comp_index_map, int comp_idx) {
    std::vector<bool> visited(n, false);
    std::set<int> queue;
    queue.insert(start);
    visited[start] = true;
    comp_index_map[start] = comp_idx;
    int lvl = 0;
    while (!queue.empty()) {
      std::set<int> tmp;
      lvl++;
      for (int cur : queue) {
        for (int next : graph[cur]) {
          if (queue.contains(next))
            return -1; // one of the current layer's node is linked to another
                       // node in the current layer
          if (!visited[next]) {
            visited[next] = true;
            comp_index_map[next] = comp_idx;
            tmp.insert(next);
          }
        }
      }
      queue = tmp;
    }
    return lvl;
  }

  int magnificentSets(int n, vector<vector<int>> &edges) {
    /*
     * LeetCode 2493
     *
     * Brute force. We start from each node and run BFS to see how many levels
     * we can get. While doing the BFS, we check whether there is any link
     * between the nodes of the same level. If there is, then BFS fails and we
     * cannot produce a group out of this. Otherwise, we can return the number
     * of levels.
     *
     * Since the graph can be disconnected, we need to do the BFS thing for
     * each separate graph, and the final answer is the sum of the max BFS
     * levels from each disconnected components.
     *
     * O(N^2), 1724 ms, 5.04%
     */
    std::vector<std::vector<int>> graph(n, std::vector<int>());
    for (auto edge : edges) {
      graph[edge[0] - 1].push_back(edge[1] - 1);
      graph[edge[1] - 1].push_back(edge[0] - 1);
    }
    std::vector<int> comp_index_map(n, -1);
    std::vector<int> comps;
    for (int i = 0; i < n; i++) {
      if (comp_index_map[i] < 0) {
        // node i has never been visited before, we will start BFS with i as the
        // root, and store the number of levels we can get as a new element in
        // the comps array
        comps.push_back(bfs(i, n, graph, comp_index_map, comps.size()));
      } else {
        // node i has been visited before and we know which component it belongs
        // to. We will run the BFS again, but instead of creating a new
        // component, we update the level of the same component that has already
        // been created and keep the larger value
        int ci = comp_index_map[i];
        comps[ci] = std::max(comps[ci], bfs(i, n, graph, comp_index_map, ci));
      }
    }
    int res = 0;
    for (int c : comps) {
      if (c < 0)
        return -1;
      res += c;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
