#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minimizeMax(vector<int> &nums, int p) {
    /*
     * This is inspired by the hints.
     *
     * We will use binary search to find the min max difference. Let's call it
     * M. For each search, we want to find the max number of pairs that we
     * can obtain whose differences are not larger than M.
     *
     * If this number is larger or equal to p, that means we can make M even
     * smaller. Otherwise, M has to be bigger. This fulfills the binary search
     * requirements.
     *
     * Anothe key aspect is to realize that after we sort nums, we should always
     * take the first adjacent pair with difference no larger than M. This can
     * be proven the correct strategy because if we don't take the first pair,
     * we either have to take the second pair, or the following pairs. If it
     * is the case that we have to take the second pair, then among the first
     * three numbers, we can only take one pair. It can either be the second
     * pair, or the first pair. In other words, in this scenario, it does not
     * make a difference if we take the first or second pair. We might as well
     * take the first pair. If it is the case that we have to take the third,
     * or fourth, ... pair, then it is always beneficial that we take the first
     * pair.
     *
     * This proof guanratees that a greedy solution for binary search will
     * work.
     *
     * O(NlogN)
     */
    std::sort(nums.begin(), nums.end());
    int lo = 0, hi = nums[nums.size() - 1] + 1;
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      int cnt = 0, i = 0;
      while (i < nums.size() - 1) {
        if (nums[i + 1] - nums[i] <= mid) {
          cnt++;
          i += 2;
        } else {
          i++;
        }
      }
      if (cnt >= p) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }
    return lo;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
