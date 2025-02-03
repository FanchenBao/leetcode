#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution1 {
public:
  bool check(vector<int> &nums) {
    /*
     * LeetCode 1752
     *
     * nums is allowed to drop only once and the dropped number must not be
     * bigger than the start. Also, if rotated, the last number must not be
     * bigger than the first number.
     *
     * O(N)
     */
    bool rotated = false;
    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] < nums[i - 1]) {
        if (!rotated) {
          if (nums[i] > nums[0])
            return false;
          rotated = true;
        } else {
          return false;
        }
      }
    }
    if (rotated)
      return nums[nums.size() - 1] <= nums[0];
    return true;
  }
};

class Solution2 {
public:
  bool check(vector<int> &nums) {
    /*
     * This is the official solution which counts the number of violations.
     * There should be at most one violation.
     *
     * O(N)
     */
    int violation = 0;
    for (int i = 1; i < nums.size(); i++)
      violation += nums[i] < nums[i - 1];
    violation += nums[nums.size() - 1] > nums[0];
    return violation <= 1;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
