#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long helper(int idx, int rem, int limit,
                   std::vector<std::vector<long long>> &dp) {
    if (dp[idx][rem] >= 0)
      return dp[idx][rem];
    if (idx == 2) {
      dp[idx][rem] = rem <= limit ? 1 : 0;
    } else {
      dp[idx][rem] = 0;
      for (int cur = 0; cur <= std::min(limit, rem); cur++) {
        dp[idx][rem] += helper(idx + 1, rem - cur, limit, dp);
      }
    }
    return dp[idx][rem];
  }

  long long distributeCandies(int n, int limit) {
    /*
     * LeetCode 2929
     *
     * Let's try top-down DP, where dp[i][j] = the number of ways to distribute
     * j number of candies to children i, i + 1, ... 2 (children is
     * zero-indexed).
     *
     * O(N*2), unsurprisingly, it times out.
     */
    std::vector<std::vector<long long>> dp{3,
                                           std::vector<long long>(n + 1, -1)};
    return helper(0, n, limit, dp);
  }
};

class Solution2 {
public:
  long long distributeCandies(int n, int limit) {
    /*
     * Let's try O(N) with bottom-up DP and prefix sum
     *
     * 248 ms, 5.29%
     */
    if (3 * limit < n) // trivial impossible case
      return 0;
    if (limit > n)
      limit = n;
    std::vector<long long> presum(n + 1);
    // set up the prefix sum version of DP for the third child.
    presum[0] = 1;
    for (int i = 1; i <= limit; i++)
      presum[i] = presum[i - 1] + 1;
    for (int i = limit + 1; i <= n; i++)
      presum[i] = presum[i - 1];
    // for the other children
    for (int i = 1; i >= 0; i--) {
      std::vector<long long> tmp(n + 1);
      for (int rem = 0; rem <= n; rem++) {
        long long cur =
            presum[rem] - (rem <= limit ? 0 : presum[rem - limit - 1]);
        tmp[rem] =
            cur + (rem > 0 ? tmp[rem - 1] : 0); // maintain tmp as prefix sum
      }
      presum = std::move(tmp);
    }
    return presum[n] - presum[n - 1];
  }
};

class Solution3 {
public:
  long long distributeCandies(int n, int limit) {
    /*
     * Solution2 is O(N), but still slow. Let's try going from right to left,
     * thus avoiding the creation of an intermediate temporary array.
     *
     * 109 ms, 5.88%
     */
    if (3 * limit < n) // trivial impossible case
      return 0;
    if (limit > n)
      limit = n;
    std::vector<long long> presum(n + 1);
    // set up the prefix sum version of DP for the third child.
    presum[0] = 1;
    for (int i = 1; i <= limit; i++)
      presum[i] = presum[i - 1] + 1;
    for (int i = limit + 1; i <= n; i++)
      presum[i] = presum[i - 1];
    // for the other children
    for (int i = 1; i >= 0; i--) {
      for (int rem = n; rem >= 0; rem--) {
        // from right to left, but temporarily, it is not a presum
        presum[rem] =
            presum[rem] - (rem <= limit ? 0 : presum[rem - limit - 1]);
      }
      // make it presum again
      for (int j = 1; j <= n; j++)
        presum[j] += presum[j - 1];
    }
    return presum[n] - presum[n - 1];
  }
};

class Solution4 {
public:
  long long distributeCandies(int n, int limit) {
    /*
     * The official non-math solution. Essentially, this solution takes
     * advantage of the constraint that there is only three children. Thus,
     * once the number of candies for the first and second child is determied,
     * the third child is also determined.
     *
     * Solutions 2 and 3 are the generic version which can handle arbitrary
     * number of children.
     *
     * O(N), 32 ms, 20%
     */
    long long res = 0;
    for (int i = 0; i <= std::min(n, limit); i++) {
      // i is the number of candies the first child can take
      if (n - i > 2 * limit) // too many candies left, impossible case
        continue;
      // if second child takes less than this amount, third child would have to
      // take more than limit.
      int second_min = std::max(0, n - i - limit);
      int second_max = std::min(limit, n - i);
      // once the number of candies the second child can take is determined,
      // the third child is also determined. Thus the total number of ways is
      // the same as the number of ways the second child can take the candies.
      res += second_max - second_min + 1;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
