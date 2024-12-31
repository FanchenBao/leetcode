#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int countGoodStrings(int low, int high, int zero, int one) {
    /*
     * LeetCode 2466
     *
     * DP, where dp[i] is the total number of ways to create good strings of
     * size i.
     *
     * For a new dp[i], we can either use '0' first or '1' first. Each will
     * accumulate dp[i - zero] or dp[i - one] number of new good strings. Add
     * them together, we get the total number of good strings with length i.
     *
     * O(N) where N = high - low
     * 1 ms, Beats 99.41%
     */
    std::vector<int> dp(high + 1, 0);
    int MOD = 1000000007;
    dp[0] = 1;
    for (int cur = std::min(zero, one); cur <= high; cur++) {
      int zero_cnt = cur >= zero ? dp[cur - zero] : 0;
      int one_cnt = cur >= one ? dp[cur - one] : 0;
      dp[cur] = (zero_cnt + one_cnt) % MOD;
    }
    int res = 0;
    for (int i = low; i <= high; i++)
      res = (res + dp[i]) % MOD;
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
