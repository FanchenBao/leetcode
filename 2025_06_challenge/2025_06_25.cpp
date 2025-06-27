#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int longestSubsequence(string s, int k) {
    /*
     * LeetCode 2311
     *
     * The core idea is that removing a leading one is always more beneficial
     * than removing a trailing zero. Therefore, we shall always remove
     * leading ones (ignoring any leading zeros) until the remaining number
     * is not bigger than k.
     *
     * In other words, we can go from right to left, find the value at each
     * time a one is encountered. If at a certain one, the value is bigger
     * than k, we do not take this one and other ones to the left, but we will
     * collect all the zeros.
     *
     * 0 ms
     */
    int cur = 0, res = 0;
    for (int i = s.size() - 1; i >= 0; i--) {
      if (s[i] == '0') {
        res++;
      } else if (cur >= 0 && cur <= k && s.size() - i - 1 < 32) {
        // Note that we also limit the number of shifts that is allowed
        cur += 1 << (s.size() - i - 1);
        if (cur >= 0 && cur <= k)
          res++;
      }
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
