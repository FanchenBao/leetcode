#include <iostream>
#include <map>
#include <vector>

using namespace std;

class Solution {
private:
  int compute(int mask, std::vector<int> &nums) {
    int sum = 0;
    int N = nums.size();
    for (int i = 0; i < N; i++) {
      if ((mask & (1 << (N - i - 1))) == 0)
        sum += nums[i];
      else
        sum -= nums[i];
    }
    return sum;
  }

public:
  int findTargetSumWays(vector<int> &nums, int target) {
    /*
     * LeetCode 494
     *
     * Brute force, but use bit manipulation to iterate through all possible
     * operator combinations.
     *
     * O(2^N * N) TLE
     */
    int N = nums.size();
    int res = 0;
    int total_pos = 1 << N;
    for (int i = 0; i < total_pos; i++) {
      int sum = compute(i, nums);
      if (sum == target)
        res++;
    }
    return res;
  }
};

class Solution2 {
private:
  int compute(int mask, std::vector<int> &nums, int lo, int hi) {
    int sum = 0;
    for (int i = lo; i <= hi; i++) {
      if ((mask & (1 << (hi - lo - i))) == 0)
        sum += nums[i];
      else
        sum -= nums[i];
    }
    return sum;
  }

public:
  int findTargetSumWays(vector<int> &nums, int target) {
    /*
     * LeetCode 494
     *
     * Do the brute force for half of nums, then match the other half for
     * target.
     *
     * O(2^N * N)
     */
    int N = nums.size();
    int left_size = N / 2, right_size = N - left_size;
    int res = 0;
    int left_pos = 1 << left_size, right_pos = 1 << right_size;
    std::map<int, int> left_counter;
    for (int i = 0; i < left_pos; i++) {
      int sum = compute(i, nums, 0, left_size - 1);
      left_counter[sum]++;
    }
    for (int i = 0; i < right_pos; i++) {
      int tmp = target - compute(i, nums, left_size, N - 1);
      res += left_counter[tmp];
    }
    return res;
  }
};

class Solution3 {
public:
  int findTargetSumWays(vector<int> &nums, int target) {
    /*
     * DP solution. dp[i][j] = number of ways to find sum j + total using only
     * nums[:i + 1]. Here, total is the sum of all nums. The possiblity of
     * all types of sum is from -total to +total.
     *
     * O(MN), where M = len(nums), N = sum of all values in nums.
     * 21 ms Beats 54.10%
     */
    int M = nums.size();
    int N = 0;
    for (int n : nums)
      N += n;
    if (N < target || N < -target)
      return 0;
    std::vector<std::vector<int>> dp(M, std::vector<int>(2 * N + 1, 0));
    dp[0][nums[0] + N] += 1;
    dp[0][N - nums[0]] += 1;
    for (int i = 1; i < M; i++) {
      for (int j = 0; j <= 2 * N; j++) {
        // j - nums[i] derives from (j - N) - nums[i] + N
        // it first converts j to target value, computes a new value, and
        // finally converts the value back to index.
        int op1 = j - nums[i] >= 0 && j - nums[i] <= 2 * N
                      ? dp[i - 1][j - nums[i]]
                      : 0;
        int op2 = j + nums[i] >= 0 && j + nums[i] <= 2 * N
                      ? dp[i - 1][j + nums[i]]
                      : 0;
        dp[i][j] = op1 + op2;
      }
    }
    return dp[M - 1][target + N];
  }
};

int main() {
  std::vector<int> nums{1, 1, 1, 1, 1};
  int target = 3;
  Solution3 sol;
  std::cout << sol.findTargetSumWays(nums, target) << std::endl;
}
