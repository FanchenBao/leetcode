#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int numberOfArrays(vector<int> &differences, int lower, int upper) {
    /*
     * LeetCode 2145
     *
     * Set the first number to be x, then using the differences array, we can
     * produce the remaining numbers with regards to x. Find the min and max
     * among them and restrict them using lower and upper. This can produce the
     * range for x. If the range is reasonable, we can return the number of
     * arrays. Otherwise, we return zero.
     *
     * O(N), 0 ms, 100%
     */
    long long min = 0, max = 0, delta = 0;
    for (int d : differences) {
      delta += d;
      min = std::min(min, delta);
      max = std::max(max, delta);
    }
    min = lower - min, max = upper - max;
    int res = (int)(max - min + 1);
    return res >= 0 ? res : 0;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
