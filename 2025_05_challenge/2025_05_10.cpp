#include <climits>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long minSum(vector<int> &nums1, vector<int> &nums2) {
    /*
     * LeetCode 2918
     *
     * Find the current sum of nums1 and nums2, as well as the count of zeros
     * in both arrays. Suppose filling all the zeros with 1 in nums1 creates
     * the min sum, we check if this sum is reachable by nums2. Similarly, we
     * do the same with nums2. If neither is reachable, return -1. Otherwise,
     * we will return the min sum of either scenario.
     *
     * O(N), 116 ms, 91.53%
     */
    long long s1 = 0, s2 = 0, c1 = 0, c2 = 0;
    for (int n : nums1) {
      s1 += (long long)n;
      c1 += n == 0;
    }
    for (int n : nums2) {
      s2 += (long long)n;
      c2 += n == 0;
    }
    // choose nums1 as the base for min sum
    long long min_sum_1 = s1 + c1;
    if ((c2 == 0 && min_sum_1 != s2) || (min_sum_1 - s2 < c2))
      min_sum_1 = LONG_MAX;
    // choose nums2 as the base for min sum
    long long min_sum_2 = s2 + c2;
    if ((c1 == 0 && min_sum_2 != s1) || (min_sum_2 - s1 < c1))
      min_sum_2 = LONG_MAX;
    long long res = std::min(min_sum_1, min_sum_2);
    return res == LONG_MAX ? -1 : res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
