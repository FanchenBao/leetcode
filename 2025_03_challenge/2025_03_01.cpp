#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> applyOperations(vector<int> &nums) {
    /*
     * LeetCode 2460
     *
     * O(N), 3 ms
     */
    for (int i = 0; i < nums.size() - 1; i++) {
      if (nums[i] == nums[i + 1]) {
        nums[i] *= 2;
        nums[i + 1] = 0;
      }
    }
    std::vector<int> res(nums.size(), 0);
    int i = 0;
    for (int n : nums) {
      if (n != 0)
        res[i++] = n;
    }
    return res;
  }
};

class Solution2 {
public:
  vector<int> applyOperations(vector<int> &nums) {
    /*
     * Let's try doing this in-place
     *
     * 0 ms
     */
    int j = 0;
    for (int i = 0; i < nums.size(); i++) {
      if (i < nums.size() - 1 && nums[i] == nums[i + 1]) {
        nums[i] *= 2;
        nums[i + 1] = 0;
      }
      if (nums[i] != 0)
        std::swap(nums[j++], nums[i]);
    }
    return nums;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
