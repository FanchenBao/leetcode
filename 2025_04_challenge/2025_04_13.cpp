#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int pow(long long b, long long p, long long m) {
    int res = 1;
    while (p) {
      if (p % 2 == 1)
        res = (res * b) % m;
      res = (res * res) % m;
      p /= 2;
    }
    return res;
  }

  int countGoodNumbers(long long n) {
    /*
     * LeetCode 1922
     *
     * This problem is very simple, but it does require the implementation of
     * power with modulo.
     *
     * At even positions, there are 5 choices; at odd positions, there are 4
     * choices. Thus each pair has 20 choices. The total number of choices are
     * 20 ^ (n / 2) if n is even, or 20 ^ ((n - 1) / 2) * 5 if n is odd.
     */
    int MOD = 1000000007;
    if (n % 2 == 0)
      return pow(20, n / 2, MOD);
    return (pow(20, (n - 1) / 2, MOD) * 5) % MOD;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
