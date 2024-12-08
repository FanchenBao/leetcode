#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minimumSize(vector<int> &nums, int maxOperations) {
    /*
     * LeetCode 1760
     *
     * This is a min-max problem, so we use binary search.
     *
     * O(NlogM), where M is the difference between the max and min values in
     * nums. 46 ms, faster than 29.33%
     *
     * UPDATE: this is kinda slow. My suspicion is that std::div() takes too
     * long. Let's use a trick ceil(x / y - 1) to get the number of ops. The
     * trick comes from the official solution. 80 ms, faster than 5.33%
     *
     * UPDATE: using the ceil trick is actually slower. Screw this, let's use
     * modulo and division directly. No more trick. 25 ms, faster than 92.44%
     *
     * In conclusion, the fastest is always without any complex function calls
     * or object creation.
     */
    int hi = 0;
    for (int n : nums)
      hi = std::max(n, hi);
    hi++;
    int lo = 1;
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      int ops = 0;
      for (int n : nums) {
        if (n > mid) {
          int q = n / mid;
          int r = n % mid;
          ops += r == 0 ? q - 1 : q;
          if (ops > maxOperations)
            break;
        }
      }
      if (ops > maxOperations)
        lo = mid + 1;
      else
        hi = mid;
    }
    return lo;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
