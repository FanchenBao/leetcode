#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int numTilings(int n) {
    /*
     * LeetCode 790 (Fail)
     *
     * I was able to solve this by myself twice in 2021 and 2022. But I cannot
     * solve it today, for whatever reason.
     *
     * Based on my previous solutions, the problem can be broken down into
     * such.
     *
     * One vertical, dp the rest.
     *
     * Two horizontal, dp the rest.
     *
     * One top left tromino and one bottom right tromino, move the bottom right
     * tromino to the right, two positions at a time, and dp the rest. Note
     * that the spaces between the two trominoes can only be filled by
     * horizontal dominoes, which means there is only one way to do so.
     *
     * One top left and one top right tromino, move the top right tromino to
     * the right, two positions at a time, and dp the rest. The spaces in
     * between the two trominoes can only be filled by horizontal dominoes
     * again.
     *
     * These four scenarios form the DP relationship.
     */
    std::vector<long long> dp(n + 1);
    long long MOD = 1000000007;
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
      dp[i] = (dp[i] + dp[i - 1]) % MOD; // one vertical
      if (i >= 2)
        dp[i] = (dp[i] + dp[i - 2]) % MOD; // two horizontal
      // top left + bottom right trominoes
      for (int j = i - 3; j >= 0; j -= 2)
        dp[i] = (dp[i] + 2 * dp[j]) % MOD;
      // top left + top right trominoes
      for (int j = i - 4; j >= 0; j -= 2)
        dp[i] = (dp[i] + 2 * dp[j]) % MOD;
    }
    return (int)dp[n];
  }
};

int main() {
  int n = 3;
  Solution sol;
  std::cout << sol.numTilings(n) << std::endl;
}
