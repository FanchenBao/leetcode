#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
private:
  bool check(std::vector<int> &nums, std::vector<std::vector<int>> &queries,
             int k, std::vector<std::vector<int>> &linesweep) {
    // are the first k queries able to cover the entirety of nums?
    // If yes, return true, otherwise, false
    int i = 0, cur = 0;
    for (int j = 0; j < nums.size(); j++) {
      while (i < linesweep.size() && linesweep[i][0] <= j) {
        if (linesweep[i][1] + 1 <= k)
          cur += linesweep[i][2];
        i++;
      }
      if (nums[j] > cur)
        return false;
    }
    return true;
  }

public:
  int minZeroArray(vector<int> &nums, vector<vector<int>> &queries) {
    /*
     * LeetCode 3356
     *
     * Bineary search. At each step, use linesweep to find the max value that
     * can be accumulated for each position.
     *
     * O(MlogM + NlogM), where N = len(nums), M = len(queries) 806 ms, 8.56%
     */
    std::vector<std::vector<int>> linesweep;
    for (int i = 0; i < queries.size(); i++) {
      auto q = queries[i];
      linesweep.push_back({q[0], i, q[2]});
      linesweep.push_back({q[1] + 1, i, -q[2]});
    }
    std::sort(linesweep.begin(), linesweep.end());

    int lo = 0, hi = queries.size() + 1;
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      if (check(nums, queries, mid, linesweep))
        hi = mid;
      else
        lo = mid + 1;
    }
    return lo <= queries.size() ? lo : -1;
  }
};

class Solution2 {
public:
  int minZeroArray(vector<int> &nums, vector<vector<int>> &queries) {
    /*
     * This is also linesweep, but much better implementation. It is from
     * the editorial. We use a delta array to keep track of the delta
     * value at each position mentioned in queries. Then as we go through
     * nums left to right, we use the delta value to compute the current
     * max value accumulated for each position.
     */
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
