#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maxAbsoluteSum(vector<int> &nums) {
    /*
     * LeetCode 1749
     *
     * Use prefix sum. And then find the prefix max and prefix min of the
     * prefix sum. Then for each prefix sum, we compute psum - pmax and psum -
     * pmin. We take the max of the two.
     *
     * O(N), 0 ms, 100%
     */
    int psum = 0, pmin = 0, pmax = 0, res = 0;
    for (int n : nums) {
      psum += n;
      res =
          std::max(res, std::max(std::abs(psum - pmax), std::abs(psum - pmin)));
      pmin = std::min(pmin, psum);
      pmax = std::max(pmax, psum);
    }
    return res;
  }
};

class Solution2 {
public:
  int maxAbsoluteSum(vector<int> &nums) {
    /*
     * This solution is inspired by the editorial. We don't have to compute
     * each absolute subarray sum along the way. All we need is to find the
     * min and max prefix sum. Their difference is the answer.
     *
     * O(N), 0 ms, 100%
     */
    int psum = 0, pmin = 0, pmax = 0;
    for (int n : nums) {
      psum += n;
      pmin = std::min(pmin, psum);
      pmax = std::max(pmax, psum);
    }
    return pmax - pmin;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
