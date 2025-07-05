#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  char kthCharacter(long long k, vector<int> &operations) {
    /*
     * LeetCode 3307
     *
     * This solution builds on top of the solution for problem 3304.
     *
     * We turn k in to a binary number. We count from least significant bit
     * to most significant bit.
     *
     * Before the encounter of the first set bit, the number of the initial
     * zeros represent the number of steps taken. We can get the operations
     * directly from operations array.
     *
     * After the encounter of the first set bit, the next set bit signifies
     * another change in letter. The operation for that is determined by the
     * number of total bits encountered so far.
     *
     * We do this until k is exhausted.
     *
     * 0 ms, 100% Apparently, solving yesterday's problem is the KEY to solving
     * this one.
     */
    bool set_bit_encountered = false;
    int cnt = 0, steps = 0;
    while (k > 0) {
      int b = k & 1;
      if (set_bit_encountered) {
        if (b == 1)
          steps = (steps + operations[cnt]) % 26;
      } else {
        if (b == 0)
          steps = (steps + operations[cnt]) % 26;
        else
          set_bit_encountered = true;
      }
      cnt++;
      k >>= 1;
    }
    return 'a' + steps;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
