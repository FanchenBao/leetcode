#include <iostream>
#include <queue>
#include <set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  int minTimeToReach(vector<vector<int>> &moveTime) {
    /*
     * LeetCode 3342
     *
     * Dijkstra still, but we need to keep track of whether the move costs
     * one or two seconds.
     *
     * O(MNlog(MN)), 755 ms, 34.17%
     */
    std::vector<std::pair<int, int>> DIRS{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int M = moveTime.size(), N = moveTime[0].size();
    std::vector<std::vector<int>> reach_time(M, std::vector<int>(N, INT_MAX));
    std::priority_queue<std::vector<int>>
        queue; // {-reach_time, i, j, is_one_second}
    reach_time[0][0] = 0;
    queue.push({0, 0, 0, 1});
    while (!queue.empty()) {
      auto ele = queue.top();
      queue.pop();
      int cur_time = -ele[0], i = ele[1], j = ele[2], dt = ele[3] ? 1 : 2;
      if (i == M - 1 && j == N - 1)
        return cur_time;
      for (auto d : DIRS) {
        int ni = i + d.first, nj = j + d.second;
        if (ni >= 0 && ni < M && nj >= 0 && nj < N) {
          int nex_time = std::max(cur_time, moveTime[ni][nj]) + dt;
          if (nex_time < reach_time[ni][nj]) {
            reach_time[ni][nj] = nex_time;
            queue.push({-nex_time, ni, nj, ele[3] ^ 1});
          }
        }
      }
    }
    return -1; // should not reach here
  }
};

class Solution2 {
public:
  int minTimeToReach(vector<vector<int>> &moveTime) {
    /*
     * Use parity of indices to decide whether it is a one second or two
     * seconds increment.
     *
     * 202 ms, 90.30%
     */
    std::vector<std::pair<int, int>> DIRS{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int M = moveTime.size(), N = moveTime[0].size();
    std::vector<std::vector<int>> reach_time(M, std::vector<int>(N, INT_MAX));
    std::priority_queue<std::pair<int, std::pair<int, int>>> queue;
    reach_time[0][0] = 0;
    queue.push({0, {0, 0}});
    while (!queue.empty()) {
      auto ele = queue.top();
      queue.pop();
      int cur_time = -ele.first, i = ele.second.first, j = ele.second.second;
      if (i == M - 1 && j == N - 1)
        return cur_time;
      for (auto d : DIRS) {
        int ni = i + d.first, nj = j + d.second;
        if (ni >= 0 && ni < M && nj >= 0 && nj < N) {
          int nex_time = std::max(cur_time, moveTime[ni][nj]) + (i + j) % 2 + 1;
          if (nex_time < reach_time[ni][nj]) {
            reach_time[ni][nj] = nex_time;
            queue.push({-nex_time, {ni, nj}});
          }
        }
      }
    }
    return -1; // should not reach here
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
