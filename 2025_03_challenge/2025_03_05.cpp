#include <ios>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long coloredCells(int n) {
    /*
     * LeetCode 2579
     *
     * The pattern is that the number of newly added cells is the number of
     * previously added cells plus four.
     *
     * O(N), 0 ms
     */
    if (n == 1)
      return 1;
    long long total = 1, pre_add = 0;
    for (int i = 1; i < n; i++) {
      long long cur_add = pre_add + 4;
      total += cur_add;
      pre_add = cur_add;
    }
    return total;
  }
};

class Solution2 {
public:
  long long coloredCells(int n) {
    /*
     * The general pattern is An = An-1 + 4(n - 1)
     * From here, we can get An = 1 + 2n(n - 1)
     */
    long long ln = (long long)n;
    return 1 + 2 * ln * (ln - 1);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
