#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maxAscendingSum(vector<int> &nums) {
    /*
     * LeetCode 1800
     *
     * O(N)
     */
    int pre = 101;
    int res = 0, sum = 0;
    for (int n : nums) {
      if (n <= pre) {
        res = std::max(res, sum);
        sum = n;
      } else {
        sum += n;
      }
      pre = n;
    }
    return std::max(res, sum);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
