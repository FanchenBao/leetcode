#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution1 {
public:
  vector<int> findMissingAndRepeatedValues(vector<vector<int>> &grid) {
    /*
     * LeetCode 2965
     *
     * Brute force. O(N^2), 2 ms, 78.93%
     */
    int N = grid.size();
    std::vector<int> flat = std::vector<int>(N * N + 1, 0);
    for (const auto &row : grid) {
      for (int r : row)
        flat[r] += 1;
    }
    std::vector<int> res = std::vector<int>(2, 0);
    for (int i = 1; i <= N * N; i++) {
      if (flat[i] == 0)
        res[1] = i;
      else if (flat[i] == 2)
        res[0] = i;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
