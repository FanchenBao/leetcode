#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int longestMonotonicSubarray(vector<int> &nums) {
    /*
     * LeetCode 3105
     *
     * Examine mountain or valley subarrays
     * O(N), 0 ms, 100%
     */
    int res = 1, cur = 0;
    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] == nums[i - 1]) {
        cur = 1;
      } else if (nums[i] > nums[i - 1]) {
        if (i == 1 || nums[i - 1] <= nums[i - 2])
          cur = 2;
        else
          cur++;
      } else {
        if (i == 1 || nums[i - 1] >= nums[i - 2])
          cur = 2;
        else
          cur++;
      }
      res = std::max(res, cur);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
