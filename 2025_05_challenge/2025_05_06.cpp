#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> buildArray(vector<int> &nums) {
    /*
     * LeetCode 1920
     */
    std::vector<int> res(nums.size());
    for (int i = 0; i < nums.size(); i++)
      res[i] = nums[nums[i]];
    return res;
  }
};

class Solution2 {
public:
  vector<int> buildArray(vector<int> &nums) {
    /*
     * O(1) space solution
     */
    int ZERO = -1001;
    for (int i = 0; i < nums.size(); i++) {
      nums[i] = -nums[i];
      if (nums[i] == 0)
        nums[i] = ZERO;
    }
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] < 0) {
        int idx = i, val = nums[i] == ZERO ? 0 : -nums[i];
        int j = val, ii = i;
        while (j != idx) {
          int v = nums[j] == ZERO ? 0 : -nums[j];
          nums[ii] = v;
          ii = j;
          j = v;
        }
        nums[ii] = val;
      }
    }
    return nums;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
