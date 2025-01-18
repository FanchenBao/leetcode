#include <iostream>
#include <numeric>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool doesValidArrayExist(vector<int> &derived) {
    /*
     * LeetCode 2683
     *
     * Just set a starting value and go through derived to produce what the
     * original should be. And then compare the computed starting value with
     * the actual starting value. If the two are the same, it is possible.
     * Otherwise, it is not.
     *
     * It does not matter what value we start; it can be zero or one.
     *
     * O(N), 7 ms, 29.44%
     */
    int st = 1, cur = 1;
    for (int d : derived)
      cur ^= d;
    return st == cur;
  }
};

class Solution2 {
public:
  bool doesValidArrayExist(vector<int> &derived) {
    /*
     * This is from the official solution. We can also check the
     * parity of the number of 1s. It has to be even.
     *
     * O(N), 3 ms, 59.81%
     */
    return std::accumulate(derived.begin(), derived.end(), 0) % 2 == 0;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
