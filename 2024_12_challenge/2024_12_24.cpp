#include <iostream>
#include <queue>
#include <set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
private:
  std::vector<std::vector<int>> get_graph(std::vector<vector<int>> &edges) {
    int N = edges.size() + 1;
    std::vector<std::vector<int>> graph(N);
    for (auto e : edges) {
      graph[e[0]].push_back(e[1]);
      graph[e[1]].push_back(e[0]);
    }
    return graph;
  };

  std::pair<int, int>
  get_min_height_max_diameter(std::vector<std::vector<int>> graph) {
    int N = graph.size();
    int lvl = 0;
    std::vector<int> degrees(N, 0);
    std::queue<int> queue;
    for (int i = 0; i < N; i++) {
      if (graph[i].size() == 1)
        queue.push(i);
      degrees[i] = graph[i].size();
    }
    while (!queue.empty() && N > 2) {
      int size = queue.size();
      while (size > 0) {
        int node = queue.front();
        queue.pop();
        for (int c : graph[node]) {
          degrees[c]--;
          if (degrees[c] == 1)
            queue.push(c);
        }
        size--;
        N--;
      }
      lvl++;
    }
    return N == 2 ? std::make_pair(lvl + 1, 2 * lvl + 1)
                  : std::make_pair(lvl, lvl * 2);
  }

public:
  int minimumDiameterAfterMerge(vector<vector<int>> &edges1,
                                vector<vector<int>> &edges2) {
    /*
     * LeetCode 3203 (hint)
     *
     * Topological sort to find the min height of each tree. The answer is
     * the sum of the min heights plus 1.
     *
     * The hint is very important as it points out the diameter of the final
     * tree is the max(first tree's max diameter, second tree's max diameter,
     * first tree's min height + second tree's min height + 1)
     *
     * UPDATE: for topological sort, we don't need to use set in the graph.
     * Instead, we just need a counter to keep track of the degrees
     *
     * O(M + N), 521 ms, faster than 27.10%
     */
    int N = edges1.size() + 1;
    int M = edges2.size() + 1;
    auto graph1 = get_graph(edges1);
    auto graph2 = get_graph(edges2);
    auto p1 = get_min_height_max_diameter(graph1);
    auto p2 = get_min_height_max_diameter(graph2);
    return std::max({p1.second, p2.second, p1.first + p2.first + 1});
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
