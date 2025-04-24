#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
private:
  std::vector<long long> FACT;

  void precompute_factorial(long long max_n, long long MOD) {
    FACT.push_back(1); // factorial(0)
    for (long long i = 1; i <= max_n; i++) {
      FACT.push_back(FACT[FACT.size() - 1] * i % MOD);
    }
  }

  long long power(long long x, long long p, long long MOD) {
    long long res = 1, base = x;
    while (p > 0) {
      if (p % 2 == 1) {
        res = (res * base) % MOD;
      }
      base = (base * base) % MOD;
      p /= 2;
    }
    return res;
  }

  long long inverse(long long n, long long MOD) {
    // compute n^-1 modulo MOD using Fermat's Little Theorum, which states
    // that for any integer a, if p is prime, then a^p and a has the same
    // modulo against p. Thus, a^(p - 2) and a^-1 has the same modulo against
    // p.
    return power(n, MOD - 2, MOD);
  }

  long long comb(long long n, long long k, long long MOD) {
    // compute nCk with MOD
    long long numerator = FACT[n];
    long long denominator = (FACT[n - k] * FACT[k]) % MOD;
    return (numerator * inverse(denominator, MOD)) % MOD;
  }

public:
  int idealArrays(int n, int maxValue) {
    /*
     * LeetCode 2338
     *
     * This is a solution inspired by the hints. We will define dp such that
     * dp[i][j] = the number of strictly increasing array that satisfy the
     * requirement starting with number i and with the size being j.
     *
     * Use an example of n = 5, maxValue = 6. If the first number is 1, there
     * are two ways to put two more numbers in the array (2, 4), (2, 6), and
     * (3, 6). For each array, there are 4C2 number of ways to organize the
     * two numbers. For each such organization, we can create an ideal array
     * by filling the empty space with the same value immediately to its
     * left. For example, if we go with 1_2_4_, then the ideal array is
     * 112244. If we go with 1__24_, then the ideal array is 111244.
     *
     * Efficiency boost:
     * 1. the max length of a strictly increasing array cannot exceed
     * log2(maxValue) + 2. This is the scenario where the array starts with 1
     * and 2, and continue doubling until maxValue is reached.
     *
     * 54 ms, 54.31%
     */
    long long MOD = 1000000007;
    int M = maxValue + 1, N = std::min(n + 1, (int)std::log2(maxValue) + 2);
    std::vector<std::vector<long long>> dp(M, std::vector<long long>(N));
    // Populate DP
    for (int i = maxValue; i >= 1; i--) {
      dp[i][1] = 1;
      for (int k = 2; k * i < M; k++) {
        for (int j = 2; j < N && dp[i * k][j - 1] > 0; j++) {
          dp[i][j] = (dp[i][j] + dp[i * k][j - 1]) % MOD;
        }
      }
    }
    long long res = 0;
    precompute_factorial((long long)n, MOD);
    for (long long i = 1; i < M && dp[i][1] > 0; i++) {
      res = (res + 1) % MOD; // this is handling dp[i][1]
      for (long long j = 2; j < N && dp[i][j] > 0; j++) {
        long long c = comb((long long)n - 1, j - 1, MOD);
        res = (res + c * dp[i][j]) % MOD;
      }
    }
    return (int)res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
