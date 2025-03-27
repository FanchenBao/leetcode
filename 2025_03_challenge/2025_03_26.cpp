#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minOperations(vector<vector<int>> &grid, int x) {
    /*
     * LeetCode 2033
     *
     * To find the min operations is equivalent to find the sum of all the
     * absolute deltas. Based on this, I think I can prove two things.
     *
     * First, the min sum of deltas is achieved when the converging number
     * is a member of the grid.
     *
     * Two, if one of the grid member can make it happen, any member of the
     * grid can make it happen. If one of the grid member fails, then no
     * other member can succeed.
     *
     * Given an array [a1, a2, a3, ..., an], and prefix sum array [s0, s1, ...
     * sn], if we choose am to be the converging number, the sum we want to
     * minimize is
     *
     * (2 * m - n - 1) * am - Sm-1 + Sn - Sm
     *
     * O(TlogT), where T = M * N, 59 ms, 15.50%
     */
    int M = grid.size(), N = grid[0].size();
    int T = M * N;
    std::vector<int> psum(T + 1, 0);
    std::vector<int> flatten(T);
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        flatten[i * N + j] = grid[i][j];
      }
    }
    std::sort(flatten.begin(), flatten.end());
    for (int i = 0; i < T; i++) {
      psum[i + 1] = psum[i] + flatten[i];
    }
    // check if it is possible
    for (int i = 1; i < T; i++) {
      if ((flatten[i] - flatten[0]) % x != 0) {
        return -1;
      }
    }
    // find the smallest sum of delta
    int min_sum_delta = INT_MAX;
    for (int i = 0; i < T; i++) {
      int cur =
          (2 * (i + 1) - T - 1) * flatten[i] - psum[i] + psum[T] - psum[i + 1];
      min_sum_delta = std::min(min_sum_delta, cur);
    }
    return min_sum_delta / x;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
