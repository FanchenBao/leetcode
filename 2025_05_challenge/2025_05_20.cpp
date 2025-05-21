#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool isZeroArray(vector<int> &nums, vector<vector<int>> &queries) {
    /*
     * LeetCode 3355
     *
     * Linesweep.
     *
     * O(N), 7 ms, 66.55%
     */
    std::vector<int> sweeps(nums.size() + 1);
    for (const auto &q : queries) {
      sweeps[q[0]]++;
      sweeps[q[1] + 1]--;
    }
    if (sweeps[0] < nums[0])
      return false;
    for (int i = 1; i < nums.size(); i++) {
      sweeps[i] += sweeps[i - 1];
      if (sweeps[i] < nums[i])
        return false;
    }
    return true;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
