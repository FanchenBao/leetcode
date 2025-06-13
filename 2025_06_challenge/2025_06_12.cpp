#include <cstdlib>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maxAdjacentDistance(vector<int> &nums) {
    /*
     * LeetCode 3423
     *
     * Just remember to do one more difference between the first and last
     * number.
     */
    int res = std::abs(nums[0] - nums[nums.size() - 1]);
    for (int i = 0; i < nums.size() - 1; i++)
      res = std::max(res, std::abs(nums[i] - nums[i + 1]));
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
