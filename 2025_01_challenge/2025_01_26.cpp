#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int cycle_idx = 0;

  int dfs(int node, std::vector<std::vector<int>> &status,
          std::vector<int> &favorite, std::vector<bool> &visited) {
    // return -1 if the current node is either an entry point to the cycle or
    // not part of the cycle.
    // return a non-negaive value as the cycle index if the current node is
    // part of the cycle but not the entry point.
    if (!visited[node]) {
      visited[node] = true;
      int cidx = dfs(favorite[node], status, favorite, visited);
      if (cidx >= 0) {
        if (status[node][0] >= 0) {
          // current node is the entry point, it has already been marked
          return -1;
        }
        status[node][0] = cidx;
        status[node][1] = 0;
      } else {
        status[node][1] = status[favorite[node]][1] + 1;
        if (status[favorite[node]][2] == -1)
          status[node][2] = favorite[node]; // next node is entry point
        else
          status[node][2] =
              status[favorite[node]][2]; // share the same entry point
      }
      return cidx;
    } else {
      if (status[node][0] == -1 && status[node][1] == -1 &&
          status[node][2] == -1) {
        // cycle detected. Current node is the entry point
        status[node][0] = cycle_idx;
        cycle_idx++;
        status[node][1] = 0;
        return status[node][0];
      }
      return -1; // if a node has been visited and has its status settled,
                 // whoever goes into it can never be part of the cycle
    }
  }

  int maximumInvitations(vector<int> &favorite) {
    /*
     * LeetCode 2127
     *
     * This is a very convoluted solution. We DFS the graph to obtain the
     * status of each node. For details, see the comments in the code.
     * Essentially, we want each node to tell us whether it is in a cycle. If
     * it is in a cycle, which cycle it is in. If not, which cycle entry point
     * the node will lead to and the distance to the cycle.
     *
     * Once the dfs is done, we can tally all the cycles. If a cycle has length
     * more than 2, it is the only thing allowable on the table. Then the
     * cycle length is the max invitation.
     *
     * If a cycle has only two elements, then each branch going into one of
     * the cycle member is allowed to exist. Then the total invitation for the
     * current cycle is the sum of the max branch size of each member and the
     * cycle size. However, keep in mind that all two-size cycles can be invited
     * simultaenously. e.g., if 1 <-> 2 and 3 <-> 4, all four of them can be
     * invited.
     *
     * 164 ms, 49.18%
     */
    int N = favorite.size();
    // status[i] = node i's status [cycle_idx, distance_to_cycle,
    // cycle_entry_point] If a status value is -1, that means that specific
    // status does not apply to the node. Each node can only be in two statuses.
    // 1. It is part of a cycle, in which case the node will have a cycle_idx,
    // its distance_to_cycle will be 0, and cycle_entry_point will be -1.
    // 2. It is part of a branch going towards a cycle, in which case the node
    // will have -1 as cycle_idx, a positive integer as distance_to_cyle, and
    // the index of the node as the cycle_entry_point
    std::vector<std::vector<int>> status(N, std::vector<int>(3, -1));
    std::vector<bool> visited(N, false);
    for (int i = 0; i < N; i++) {
      dfs(i, status, favorite, visited);
    }
    std::map<int, std::vector<int>> cycles;
    std::map<int, int> max_branch;
    for (int i = 0; i < N; i++) {
      if (status[i][0] >= 0) {
        if (cycles.find(status[i][0]) == cycles.end())
          cycles[status[i][0]] = std::vector<int>();
        cycles[status[i][0]].push_back(i);
      } else {
        if (max_branch.find(status[i][2]) == max_branch.end())
          max_branch[status[i][2]] = 0;
        max_branch[status[i][2]] =
            std::max(max_branch[status[i][2]], status[i][1]);
      }
    }
    int with_two_cycle = 0, with_more_than_two_cycle = 0;
    for (const auto &[k, v] : cycles) {
      if (v.size() > 2) {
        with_more_than_two_cycle =
            std::max(with_more_than_two_cycle, (int)v.size());
      } else {
        int bs1 =
            max_branch.find(v[0]) == max_branch.end() ? 0 : max_branch[v[0]];
        int bs2 =
            max_branch.find(v[1]) == max_branch.end() ? 0 : max_branch[v[1]];
        with_two_cycle += bs1 + bs2 + (int)v.size();
      }
    }
    return std::max(with_two_cycle, with_more_than_two_cycle);
  }
};

int main() {
  std::vector<int> favorite{2, 2, 1, 2};
  Solution sol;
  std::cout << sol.maximumInvitations(favorite) << std::endl;
}
