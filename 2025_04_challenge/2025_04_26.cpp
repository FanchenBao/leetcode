#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long countSubarrays(vector<int> &nums, int minK, int maxK) {
    /*
     * LeetCode 2444
     *
     * As we traverse nums, anytime a value outside the range is encountered,
     * we have to reset. For a sliding window all within range, if we hit
     * a min, we want to know the most recent max's position, if such max
     * exists. Then we can compute all the subarrays that includes the latest
     * min and latest max ending at the latest min. Moving on, for the next
     * within-range value, it will form the same number of subarrays as the
     * most recent encounter of min. The situation for max is the same,
     * except we will look for the latest min.
     *
     * O(N), 1 ms, 63.96%
     */
    long long res = 0;
    int lo = 0;
    int pre_min = -1, pre_max = -1, pre_cnt = 0;
    for (int hi = 0; hi < nums.size(); hi++) {
      if (nums[hi] < minK || nums[hi] > maxK) {
        // reset
        lo = hi + 1;
        pre_min = pre_max = -1;
        pre_cnt = 0;
        continue;
      }
      if (nums[hi] == minK) {
        if (pre_max >= 0) {
          pre_cnt = pre_max - lo + 1;
        }
        pre_min = hi;
      }
      if (nums[hi] == maxK) {
        if (pre_min >= 0) {
          pre_cnt = pre_min - lo + 1;
        }
        pre_max = hi;
      }
      res += (long long)pre_cnt;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
