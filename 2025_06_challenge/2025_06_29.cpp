#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int findLHS(vector<int> &nums) {
    /*
     * LeetCode 594
     *
     * Sort nums and then sliding window.
     *
     * O(N), 11 ms, 86.10%
     */
    std::sort(nums.begin(), nums.end());
    int j = 0, res = 0;
    for (int i = 0; i < nums.size(); i++) {
      while (j < nums.size() && nums[j] - nums[i] <= 1)
        j++;
      if (nums[j - 1] - nums[i] == 1)
        res = std::max(res, j - i);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
