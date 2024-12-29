#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
private:
  void helper(int i, int j, std::vector<long> &presum,
              std::vector<std::vector<std::vector<int>>> &dp, int k) {
    if (dp[i][j][3] > 0)
      return;
    int N = presum.size();
    for (int idx = j; idx + k - 1 < N; idx++) {
      int s = idx > 0 ? (int)(presum[idx + k - 1] - presum[idx - 1])
                      : (int)presum[idx + k - 1];
      if (i < 2 && idx + k < N) {
        helper(i + 1, idx + k, presum, dp, k);
        if (s + dp[i + 1][idx + k][3] > dp[i][j][3]) {
          dp[i][j][i] = idx;
          for (int p = i + 1; p < 3; p++)
            dp[i][j][p] = dp[i + 1][idx + k][p];
          dp[i][j][3] = s + dp[i + 1][idx + k][3];
        }
      } else if (i == 2) {
        if (s > dp[i][j][3]) {
          dp[i][j][i] = idx;
          dp[i][j][3] = s;
        }
      }
    }
  }

public:
  vector<int> maxSumOfThreeSubarrays(vector<int> &nums, int k) {
    /*
     * LeetCode 689
     *
     * Use DP. Basically we want to find the indices of the subarray with max
     * sum under each state. The state can be expressed as the number of
     * subarrays used minus 1 and the starting index of remaining subarray to
     * use.
     *
     * O(N + 3 * N^2), TLE
     */
    int N = nums.size();
    // dp[i][j] = with i number of subarrays used, in nums[j:], what is the
    // [idx0, idx1, idx2, max sum] for the current state.
    std::vector<std::vector<std::vector<int>>> dp(
        3, std::vector<std::vector<int>>(N, std::vector<int>(4, 0)));
    std::vector<long> presum;
    presum.push_back((long)nums[0]);
    for (int i = 1; i < N; i++) {
      presum.push_back(presum[i - 1] + (long)nums[i]);
    }
    helper(0, 0, presum, dp, k);
    return {dp[0][0].begin(), dp[0][0].end() - 1};
  }
};

class Solution2 {
private:
  void helper(int i, int j, std::vector<long> &presum,
              std::vector<std::vector<std::vector<int>>> &dp, int k) {
    if (dp[i][j][3] > 0)
      return;
    int N = presum.size();
    // op1, do not use nums[j]
    if (j + 1 < N) {
      helper(i, j + 1, presum, dp, k);
      for (int p = i; p < 4; p++)
        dp[i][j][p] = dp[i][j + 1][p];
    }
    // op2, use nums[j]..nums[j + k - 1]
    if (j + k - 1 < N) {
      int s = j > 0 ? (int)(presum[j + k - 1] - presum[j - 1])
                    : (int)presum[j + k - 1];
      if (i < 2 && j + k < N) {
        helper(i + 1, j + k, presum, dp, k);
        if (s + dp[i + 1][j + k][3] >= dp[i][j][3]) {
          dp[i][j][i] = j;
          for (int p = i + 1; p < 3; p++)
            dp[i][j][p] = dp[i + 1][j + k][p];
          dp[i][j][3] = s + dp[i + 1][j + k][3];
        }
      } else if (i == 2) {
        if (s >= dp[i][j][3]) {
          dp[i][j][i] = j;
          dp[i][j][3] = s;
        }
      }
    }
  }

public:
  vector<int> maxSumOfThreeSubarrays(vector<int> &nums, int k) {
    /*
     * LeetCode 689
     *
     * Still the DP solution but without unnecessary loop within the recursion
     *
     * O(N + 3 * N), 1524 ms Beats, 5.15%
     */
    int N = nums.size();
    // dp[i][j] = with i number of subarrays used, in nums[j:], what is the
    // [idx0, idx1, idx2, max sum] for the current state.
    std::vector<std::vector<std::vector<int>>> dp(
        3, std::vector<std::vector<int>>(N, std::vector<int>(4, 0)));
    std::vector<long> presum;
    presum.push_back((long)nums[0]);
    for (int i = 1; i < N; i++) {
      presum.push_back(presum[i - 1] + (long)nums[i]);
    }
    helper(0, 0, presum, dp, k);
    return {dp[0][0].begin(), dp[0][0].end() - 1};
  }
};

int main() {
  // std::vector<int> arr{1, 2, 1, 2, 6, 7, 5, 1};
  std::vector<int> arr{7, 13, 20, 19, 19, 2, 10, 1, 1, 19};
  int k = 3;
  Solution2 sol;
  sol.maxSumOfThreeSubarrays(arr, k);
}
