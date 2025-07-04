#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int CountBit(int n) {
    int res = 0;
    while (n > 0) {
      n >>= 1;
      res++;
    }
    return res;
  }

  char kthCharacter(int k) {
    /*
     * LeetCode 3304
     *
     * Use DP where dp[i] is the ith letter. For an unknown i, we remove its
     * most significant bit to form j. Then dp[i] = (dp[j] + 1) % 26.
     *
     * 3 ms, 57.81%
     */
    std::vector<int> dp{0, 0};
    for (int i = 2; i <= k; i++) {
      int c = CountBit(i);
      int rem = i & ((1 << (c - 1)) - 1);
      if (rem == 0) {
        dp.push_back((dp[i / 2] + 1) % 26);
      } else {
        dp.push_back((dp[rem] + 1) % 26);
      }
    }
    return dp[k] + 97;
  }
};

class Solution2 {
public:
  char kthCharacter(int k) {
    /*
     * After further analysis, the number of steps is equal to the number of
     * set bits.
     */
    // First find the number of bits until the least significant bit.
    int res = 0;
    while ((k & 1) == 0) {
      k >>= 1;
      res++;
    }
    res += __builtin_popcount(k);
    return 'a' + res - 1;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
