#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long countFairPairs(vector<int> &nums, int lower, int upper) {
    /*
     * LeetCode 2563
     *
     * Sort and binary search. O(NlogN), 60 ms, 39.66%
     */
    std::sort(nums.begin(), nums.end());
    long long res = 0;
    for (int i = 0; i < nums.size(); i++) {
      int tgt_lo = lower - nums[i], tgt_hi = upper - nums[i];
      int idx_lo =
          std::max(int(std::lower_bound(nums.begin(), nums.end(), tgt_lo) -
                       nums.begin()),
                   i + 1);
      int idx_hi =
          std::max(int(std::upper_bound(nums.begin(), nums.end(), tgt_hi) -
                       nums.begin()),
                   i + 1);
      if (idx_hi > idx_lo)
        res += (long long)(idx_hi - idx_lo);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
