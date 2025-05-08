#include <climits>
#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minTimeToReach(vector<vector<int>> &moveTime) {
    /*
     * LeetCode 3341
     *
     * We will use Dijkstra for this., 8 ms, 99.38%
     */
    std::vector<std::pair<int, int>> DIRS{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
    int M = moveTime.size(), N = moveTime[0].size();
    std::priority_queue<std::pair<int, std::pair<int, int>>> queue;
    std::vector<std::vector<int>> reach_time(M, std::vector<int>(N, INT_MAX));
    reach_time[0][0] = 0;
    queue.push({0, {0, 0}});
    while (!queue.empty()) {
      auto ele = queue.top();
      queue.pop();
      int cur_time = -ele.first, i = ele.second.first, j = ele.second.second;
      if (i == M - 1 && j == N - 1)
        return cur_time;
      for (auto p : DIRS) {
        int ni = i + p.first, nj = j + p.second;
        if (ni >= 0 && ni < M && nj >= 0 && nj < N) {
          int next_time = moveTime[ni][nj] <= cur_time ? cur_time + 1
                                                       : moveTime[ni][nj] + 1;
          if (next_time < reach_time[ni][nj]) {
            reach_time[ni][nj] = next_time;
            queue.push({-next_time, {ni, nj}});
          }
        }
      }
    }
    return -1; // should never reach here.
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
