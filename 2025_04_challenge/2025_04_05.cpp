#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int subsetXORSum(vector<int> &nums) {
    /*
     * LeetCode 1863
     *
     * Use bitmask to obtain all subset of nums.
     * 2 ms, 44%
     */
    int res = 0;
    int N = nums.size();
    for (int i = 1; i < (1 << N); i++) {
      int cur = 0;
      for (int j = 0; j < N; j++) {
        if ((1 << j) & i)
          cur ^= nums[N - j - 1];
      }
      res += cur;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
