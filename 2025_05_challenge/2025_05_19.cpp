#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  string triangleType(vector<int> &nums) {
    /*
     * LeetCode 3024
     */
    std::sort(nums.begin(), nums.end());
    if (nums[0] + nums[1] <= nums[2])
      return "none";
    if (nums[0] == nums[1] && nums[1] == nums[2])
      return "equilateral";
    if (nums[0] == nums[1] || nums[1] == nums[2])
      return "isosceles";
    return "scalene";
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
