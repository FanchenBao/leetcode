#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  long long num_matching_pairs(int n) {
    return (long long)n * (long long)(n - 1) / 2;
  }

  long long countGood(vector<int> &nums, int k) {
    /*
     * LeetCode 2537
     *
     * Use sliding window to find the smallest subarray starting at nums[i]
     * that satisfies the requirement. Then we can find the total number of
     * subarrays anchored by the current smallest subarray as N - i
     *
     * O(N), 87 ms, 41.71%
     */
    long long res = 0;
    std::unordered_map<int, int> counter;
    int N = nums.size();
    int lo = 0, cumsum = 0;
    for (int hi = 0; hi < N; hi++) {
      cumsum = cumsum - num_matching_pairs(counter[nums[hi]]) +
               num_matching_pairs(counter[nums[hi]] + 1);
      counter[nums[hi]]++;
      while (cumsum >= k) {
        res += (long long)(N - hi);
        cumsum = cumsum - num_matching_pairs(counter[nums[lo]]) +
                 num_matching_pairs(counter[nums[lo]] - 1);
        counter[nums[lo]]--;
        lo++;
      }
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
