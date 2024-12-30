#include <algorithm>
#include <array>
#include <iostream>
#include <iterator>
#include <set>
#include <vector>

using namespace std;

class Solution {
  int MOD = 1000000007;

private:
  int helper(int i, int j, int **dp, int **counter, vector<string> &words,
             string &target) {
    int M = words[0].size();
    int N = target.size();
    if (j == N)
      return 1;
    if (i < M && j < N && M - i >= N - j) {
      if (dp[i][j] >= 0)
        return dp[i][j];
      // OP1: do not use any letter at position i
      dp[i][j] = helper(i + 1, j, dp, counter, words, target);
      // OP2: to through the word list and use the ith letter for each elegible
      // word
      dp[i][j] = ((long)counter[i][target[j] - 'a'] *
                      helper(i + 1, j + 1, dp, counter, words, target) +
                  dp[i][j]) %
                 MOD;
      return dp[i][j];
    }
    return 0;
  }

public:
  int numWays(vector<string> &words, string target) {
    /*
     * LeetCode 1639
     *
     * DP, where dp[i][j] = number of ways to make target[j:] using word[i:]
     * for all the word in words.
     *
     * Use a counter to keep track of the letter frequency at ith position for
     * all the words.
     *
     * O(MK + MN), where M = len(word), N = len(target), K = len(words)
     *
     * MLE, damn, don't know how to improve to make memory consumption lower
     * while still using top down.
     *
     */
    int M = words[0].size();
    int N = target.size();
    int **dp = new int *[M];
    for (int i = 0; i < M; i++) {
      dp[i] = new int[N];
      for (int j = 0; j < N; j++)
        dp[i][j] = -1;
    }
    int **counter = new int *[M];
    for (int i = 0; i < M; i++) {
      counter[i] = new int[26];
      for (int j = 0; j < 26; j++)
        counter[i][j] = 0;
    }
    for (int i = 0; i < M; i++) {
      for (auto word : words) {
        counter[i][word[i] - 'a']++;
      }
    }

    int res = helper(0, 0, dp, counter, words, target);
    for (int i = 0; i < M; i++) {
      delete[] dp[i];
      delete[] counter[i];
    }
    delete[] dp;
    delete[] counter;
    return res;
  }
};

class Solution22 {
public:
  int numWays(vector<string> &words, string target) {
    /*
     * This is exactly the same solution as above, but we will use Bottom Up
     * DP.
     *
     * DP, where dp[i][j] = number of ways to make target[j:] using word[i:]
     * for all the word in words.
     *
     * O(MK + MN), where M = len(word), N = len(target), K = len(words)
     * 52 ms, Beats 82.48%
     */
    int MOD = 1000000007;
    int M = words[0].size();
    int N = target.size();
    std::vector<std::vector<int>> counter(M, std::vector<int>(26, 0));
    for (auto word : words) {
      for (int i = 0; i < M; i++)
        counter[i][word[i] - 'a']++;
    }
    std::vector<int> dp(N + 1, 0);
    dp[N] = 1; // target is exhausted, that always counts as one way
    for (int i = M - 1; i >= 0; i--) {
      std::vector<int> tmp(N + 1);
      tmp[N] = 1;
      for (int j = N - 1; j >= 0; j--)
        tmp[j] = ((long)counter[i][target[j] - 'a'] * dp[j + 1] + dp[j]) % MOD;
      dp = tmp;
    }
    return dp[0];
  }
};

int main() {
  std::vector<string> words{"acca", "bbbb", "caca"};
  string target{"aba"};
  Solution sol;
  std::cout << sol.numWays(words, target) << std::endl;
}
