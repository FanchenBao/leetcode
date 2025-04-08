#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool canPartition(vector<int> &nums) {
    /*
     * LeetCode 416
     *
     * Use DP, where dp[i][j] is whether it is possible to find a subset in
     * nums[i:] whose sum is j.
     *
     * There is also an early exist. As long as we find some dp[i][tgt] = true,
     * we can terminate the program and return true.
     *
     * O(MN), where M = sum(nums) / 2, N = len(nums)
     * 112 ms, 62.60%
     */
    int total = 0;
    for (int n : nums)
      total += n;
    if (total % 2 == 1)
      return false;
    int tgt = total / 2;
    std::sort(nums.begin(), nums.end());
    std::vector<bool> dp(total + 1, false);
    dp[nums[nums.size() - 1]] = true;
    dp[0] = true;
    for (int i = nums.size() - 2; i >= 0; i--) {
      std::vector<bool> tmp{dp.begin(), dp.end()};
      for (int j = 2 * nums[i]; j <= tgt; j++) {
        tmp[j] = tmp[j] | dp[j - nums[i]];
      }
      tmp[nums[i]] = true;
      if (tmp[tgt]) // early exit
        return true;
      dp = tmp;
    }
    return false;
  }
};

class Solution2 {
public:
  bool canPartition(vector<int> &nums) {
    /*
     * Same as Solution1, but using only one dp array. The trick is to go
     * through the js from large to small. This can avoid using a DP value
     * that is computed in the current round.
     * 51 ms. 91.77%
     */
    int total = 0;
    for (int n : nums)
      total += n;
    if (total % 2 == 1)
      return false;
    int tgt = total / 2;
    std::vector<bool> dp(total + 1, false);
    dp[nums[nums.size() - 1]] = true;
    dp[0] = true;
    for (int i = nums.size() - 2; i >= 0; i--) {
      for (int j = tgt; j >= nums[i]; j--) {
        dp[j] = dp[j] | dp[j - nums[i]];
      }
      if (dp[tgt]) // early exit
        return true;
    }
    return false;
  }
};

int main() {
  std::vector<int> nums{14, 9, 8, 4, 3, 2};
  Solution sol;
  std::cout << sol.canPartition(nums) << std::endl;
}
