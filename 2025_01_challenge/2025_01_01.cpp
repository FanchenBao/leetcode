#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maxScore(string s) {
    /*
     * LeetCode 1422
     *
     * Find total number of ones first. Then iterate through s, accumulate
     * zeros and remove ones, and find the max sum of the two.
     *
     * O(N)
     */
    int ones = 0;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '1')
        ones++;
    }
    int res = 0;
    int zeros = 0;
    for (int i = 0; i < s.size() - 1; i++) {
      if (s[i] == '0')
        zeros++;
      else
        ones--;
      res = std::max(res, ones + zeros);
    }
    return res;
  }
};

class Solution2 {
public:
  int maxScore(string s) {
    /*
     * This is the official solution of one pass.
     * We want to find 0_l + 1_r, we can rewrite it as 0_l - 1_l + 1_l + 1_r,
     * which is 0_l - 1_l + total_ones.
     *
     * total_ones is static and can be obtained by iterating through s. 0_l
     * and 1_l can also be obtained as we iterate through s. All we need to
     * do is to find the max 0_l - 1_l
     */
    int ones = 0, zeros = 0, left = INT_MIN;
    for (int i = 0; i < s.size() - 1; i++) {
      if (s[i] == '1')
        ones++;
      else
        zeros++;
      left = std::max(left, zeros - ones);
    }
    if (s[s.size() - 1] == '1')
      ones++;
    return left + ones;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
