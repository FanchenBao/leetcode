#include <cinttypes>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long countSubarrays(vector<int> &nums, long long k) {
    /*
     * LeetCode 2302
     *
     * Two pointers. O(N), 6 ms, 30.60%
     *
     * Update: when hi is N, we can exit the loop because the remaining count
     * of subarrays can be computed mathematically
     *
     * 4 ms, 48.03%
     */
    long long res = 0, s = 0;
    int N = nums.size(), hi = 0, lo = 0;
    while (hi < N) {
      if ((s + nums[hi]) * (hi - lo + 1) < k) {
        s += (long long)nums[hi++];
      } else {
        res += (long long)(hi - lo);
        s -= (long long)nums[lo++];
      }
    }
    return res + (long long)(1 + (hi - lo)) * (hi - lo) / 2;
  }
};

class Solution2 {
public:
  long long countSubarrays(vector<int> &nums, long long k) {
    /*
     * This is the standard solution from the editorial
     */
    long long res = 0, s = 0;
    int N = nums.size(), lo = 0;
    for (int hi = 0; hi < N; hi++) {
      s += (long long)nums[hi];
      while (lo <= hi && s * (hi - lo + 1) >= k)
        s -= (long long)nums[lo++];
      res += (long long)(hi - lo + 1);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
