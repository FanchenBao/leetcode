#include <climits>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int closestMeetingNode(vector<int> &edges, int node1, int node2) {
    /*
     * LeetCode 2359
     *
     * Traverse from node1, keep a record of all the nodes visited.
     *
     * Then traverse from node2. The first node encountered that has already
     * been visited in the node1 traversal
     */
    int N = edges.size();
    std::vector<int> smallest_node(N, INT_MAX);
    // traverse from node1
    dfs(node1, edges, smallest_node);
    // traverse from node2
    int node = node2;
    while (node >= 0 && smallest_node[node] == INT_MAX) {
      node = edges[node];
    }
    return (node < 0 || smallest_node[node] == INT_MAX) ? -1
                                                        : smallest_node[node];
  }
};

int main() {
  std::vector<int> edges{9, 8, 7, 0, 5, 6, 1, 3, 2, 2};
  int node1 = 1;
  int node2 = 6;
  Solution sol;
  std::cout << sol.closestMeetingNode(edges, node1, node2) << std::endl;
}
