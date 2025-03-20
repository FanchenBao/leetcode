#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minOperations(vector<int> &nums) {
    /*
     * LeetCode 3191
     *
     * Greedy solution where we always start the operation starting from the
     * first zero bit in vector.
     *
     * O(N), 4 ms, 81.56%
     */
    int res = 0;
    for (int i = 0; i < nums.size() - 2; i++) {
      if (nums[i] == 0) {
        nums[i] = 1;
        nums[i + 1] ^= 1;
        nums[i + 2] ^= 1;
        res++;
      }
    }
    if (nums[nums.size() - 1] == 1 && nums[nums.size() - 2] == 1)
      return res;
    return -1;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
