#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int waysToSplitArray(vector<int> &nums) {
    /*
     * LeetCode 2270
     *
     * Prefix sum to compare with the remaining sum.
     *
     * O(N), 2 ms, 64.07%
     */
    long sum = 0, presum = 0;
    for (int n : nums)
      sum += (long)n;
    int res = 0;
    for (int i = 0; i < nums.size() - 1; i++) {
      presum += (long)nums[i];
      if (presum >= sum - presum)
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
