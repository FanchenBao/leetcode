#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int possibleStringCount(string word, int k) {
    /*
     * LeetCode 3333
     *
     * First of all, produce an array that counts the number of consecutive
     * letters that are the same from word. Call it consec.
     *
     * Then use DP on it, where dp[i][j] is the number of ways to make a
     * typed string starting from the consec[i:] with length smaller than j.
     *
     * Eventually, when we find dp[0][k], we can compute the result as
     * consec[0] * consec[1] * ... * consec[m] - dp[0][k].
     *
     * In the implementation, we use 1D DP and we make the dp array into a
     * prefix sum.
     *
     * O(NK), TLE (maybe we can use two arrays to avoid the restoration of
     * prefix sum)
     */
    std::vector<int> consec;
    int cur = 1;
    long long MOD = 1000000007;
    for (int i = 1; i < word.size(); i++) {
      if (word[i] != word[i - 1]) {
        consec.push_back(cur);
        cur = 1;
      } else {
        cur++;
      }
    }
    consec.push_back(cur);
    long long total = 1;
    for (int c : consec) {
      total = (total * (long long)c) % MOD;
    }
    if (k == 1)
      return total;
    // DP
    std::vector<long long> dp(k + 1);
    for (int i = 2; i <= k; i++) {
      dp[i] = (dp[i - 1] + std::min(i - 1, consec[consec.size() - 1])) % MOD;
    }
    for (int i = consec.size() - 2; i >= 0; i--) {
      for (int j = dp.size() - 1; j >= 2 && dp[j] > 0; j--) {
        int lo = j - consec[i] - 1, hi = j - 1; // boundaries of prefix sum
        dp[j] = (dp[hi] - (lo >= 0 ? dp[lo] : 0) + MOD) % MOD;
      }
      // restore prefix sum
      for (int j = 1; j < dp.size(); j++)
        dp[j] = (dp[j] + dp[j - 1]) % MOD;
    }
    return (total - (dp[k] - dp[k - 1]) + MOD) % MOD;
  }
};

class Solution {
public:
  int possibleStringCount(string word, int k) {
    /*
     * LeetCode 3333
     *
     * Same as solution1, but we use two arrays to avoid a second pass on the
     * DP array.
     *
     * Also, if a letter is only typed once, it must exist in the final
     * output. Thus, we don't need to include it in the consec array, and we
     * can decrement k.
     *
     * After getting the updated k value, if it is not larger than 1,
     * we can use all combinations to produce the string. This avoids going
     * through the DP.
     *
     * O(NK), 307 ms, 80%
     */
    std::vector<int> consec;
    int cur = 1;
    long long MOD = 1000000007;
    for (int i = 1; i < word.size(); i++) {
      if (word[i] != word[i - 1]) {
        if (cur == 1) {
          k--;
          continue;
        }
        consec.push_back(cur);
        cur = 1;
      } else {
        cur++;
      }
    }
    if (cur > 1)
      consec.push_back(cur);
    else
      k--;
    long long total = 1;
    for (int c : consec) {
      total = (total * (long long)c) % MOD;
    }
    if (k <= 1)
      return total;
    // DP
    std::vector<long long> dp(k + 1);
    for (int i = 2; i <= k; i++) {
      dp[i] = (dp[i - 1] + std::min(i - 1, consec[consec.size() - 1])) % MOD;
    }
    for (int i = consec.size() - 2; i >= 0; i--) {
      std::vector<long long> tmp(k + 1);
      for (int j = 2; j <= k; j++) {
        int lo = j - consec[i] - 1, hi = j - 1; // boundaries of prefix sum
        long long cur = (dp[hi] - (lo >= 0 ? dp[lo] : 0) + MOD) % MOD;
        tmp[j] = (tmp[j - 1] + cur) % MOD;
      }
      dp = std::move(tmp);
    }
    return (total - (dp[k] - dp[k - 1]) + MOD) % MOD;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
