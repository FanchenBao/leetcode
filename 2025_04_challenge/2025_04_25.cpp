#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  long long countInterestingSubarrays(vector<int> &nums, int modulo, int k) {
    /*
     * LeetCode 2845 (Hint)
     *
     * Have to use the entire nine hints and a lot of additional thinking to
     * convince myself. The hints are pretty good. Briefly, we want to use
     * a prefix sum to keep track of the number of elements that % modulo == k
     * Then to find all the interesting subarrays ending at nums[i], we check
     * count[i], then find j such that (count[i] - count[j]) % modulo == k.
     * This means count[j] = count[i] - k - p * modulo, where p = 0, 1, 2, 3...
     * Notice that regardless of the value of p, all count[j] have the same
     * remainder as (count[i] - k + modulo) % modulo. In other words, the
     * number of interesting subarrays ending at i is the same as the count
     * of (count[i] - k + modulo) % modulo. We can use a counter to keep track
     * of this.
     *
     * O(N), 47 ms 79.78%
     */
    std::unordered_map<int, int> counter;
    counter[0] = 1;
    int good_cnt = 0;
    long long res = 0;
    for (int n : nums) {
      good_cnt += ((n % modulo) == k);
      res = res + (long long)counter[(good_cnt - k + modulo) % modulo];
      counter[good_cnt % modulo]++;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
