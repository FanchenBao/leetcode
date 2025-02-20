#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  string helper(int n, int k, int idx) {
    if (n == 0)
      return "";
    for (int i = 0; i < 3; i++) {
      if (i == idx)
        continue;
      int count = (1 << (n - 1));
      if (count >= k) {
        return char(i + 'a') + helper(n - 1, k, i);
      } else {
        k -= count;
      }
    }
    return "";
  }

  string getHappyString(int n, int k) {
    /*
     * LeetCode 1415
     *
     * Recursion, with each n, k, and previously used letter as the state for
     * each recursion. We can always fill the first letter starting from a.
     * The total number of permutations of the remaining positions is 2^(n - 1)
     * If this count is larger or equal to k, that means we can fill the
     * current position with the current letter, and move on to the next
     * letter.
     *
     * Otherwise, we can move on to the next option for the current position,
     * because there is not enough permutations to satisfy k.
     *
     * O(3N), 3 ms, 74.09%
     */
    return helper(n, k, -1);
  }
};

class Solution2 {
public:
  string getHappyString(int n, int k) {
    /*
     * Try this without recursion.
     * O(3N), 0 ms
     */
    int pi = -1;
    std::string res;
    for (int p = n; p > 0; p--) {
      for (int i = 0; i < 3; i++) {
        if (i == pi)
          continue;
        int c = (1 << (p - 1));
        if (c < k) {
          k -= c;
        } else {
          res += char(i + 'a');
          pi = i;
          break;
        }
      }
    }
    return res.size() == n ? res : "";
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
