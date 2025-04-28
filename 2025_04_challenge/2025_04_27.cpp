#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int countSubarrays(vector<int> &nums) {
    /*
     * LeetCode 3392
     *
     * O(N)
     */
    int res = 0;
    for (int i = 2; i < nums.size(); i++) {
      if (2 * (nums[i] + nums[i - 2]) == nums[i - 1])
        res++;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
