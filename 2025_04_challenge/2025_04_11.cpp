#include <cmath>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int digitsum(int n) {
    int s = 0;
    while (n > 0) {
      s += n % 10;
      n /= 10;
    }
    return s;
  }

  int countSymmetricIntegers(int low, int high) {
    /*
     * LeetCode 2843
     *
     * Brute force, 24 ms, 77.68%
     */
    int lo = 10, num_digits = 2;
    int res = 0;
    while (lo <= high) {
      for (int i = std::max(low, lo); i <= std::min(high, lo * 10 - 1); i++) {
        int mod = std::pow(10, num_digits / 2);
        if (digitsum(i % mod) == digitsum(i / mod))
          res++;
      }
      lo *= 100;
      num_digits += 2;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
