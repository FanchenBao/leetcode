#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minimizeXor(int num1, int num2) {
    /*
     * LeetCode 2429
     *
     * Let M be the set bit count of num1 and N be the set bit count of num2
     * If M and N are equal, we can turn the XOR to 0. So return num1.
     *
     * If M > N, we can remove all the high bits of num1. If M < N, we can
     * first remove all the bits of num1, and then add bits as to the right
     * as possible.
     *
     * 0 ms, 100%
     */
    int M = __builtin_popcount(num1);
    int N = __builtin_popcount(num2);
    if (M == N)
      return num1;
    int XOR;
    if (M > N) {
      XOR = num1;
      for (int i = 31; i >= 0 && N > 0; i--) {
        if ((XOR & (1 << i)) != 0) {
          XOR ^= (1 << i);
          N--;
        }
      }
    } else {
      XOR = 0;
      int k = N - M;
      for (int i = 0; i < 32 && k > 0; i++) {
        if ((num1 & (1 << i)) == 0) {
          XOR |= (1 << i);
          k--;
        }
      }
    }
    return XOR ^ num1;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
