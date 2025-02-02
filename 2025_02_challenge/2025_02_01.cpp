#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool isArraySpecial(vector<int> &nums) {
    /*
     * LeetCode 3151
     *
     * O(N)
     */
    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] % 2 == nums[i - 1] % 2)
        return false;
    }
    return true;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
