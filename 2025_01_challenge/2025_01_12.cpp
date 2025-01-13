#include <iostream>
#include <iterator>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool canBeValid(string s, string locked) {
    /*
     * LeetCode 2116 (Fail)
     *
     * I could not solve this problem.
     *
     * Reading the official solution, I am not convinced, because it implies
     * that in a situation of '(*)', the last right can pop the first left
     * while ignoring the flexible in the middle. Although this way of thinking
     * works, I am not convinced.
     *
     * Another approach is also not 100% convincing, but at least better than
     * the one above. It says we should go left to right to count the number
     * of locked right. If there are more locked right than locked left plus
     * flexible at any point in time, the string is unbalanced. Do the same
     * from right to left and count the number of locked left.
     *
     * If both ways suggest there are no excessive locked left and locked right,
     * the string can be balanced. Essentially, this suggests that as we go
     * from left to right, the locked right can all be taken care of with some
     * locked left and flexible in remaining. Since from right to left, all the
     * locked left can be taken care of, that means the remainnig locked left
     * after the left to right pass can all be taken care of, leaving only the
     * flexible. And since the length of s is even, the remaining flexible
     * count must be even, they can take care of themselves as well.
     *
     * O(N), 12 ms 68.59%
     */
    if (s.size() % 2 == 1)
      return false;
    // left to right, check whether all locked right can be taken care of
    int rcnt = 0, lfcnt = 0;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == ')' && locked[i] == '1')
        rcnt += 1;
      else
        lfcnt += 1;
      if (rcnt > lfcnt)
        return false;
    }
    // right to left, check whether all locked left can be taken care of
    int lcnt = 0, rfcnt = 0;
    for (int i = s.size() - 1; i >= 0; i--) {
      if (s[i] == '(' && locked[i] == '1')
        lcnt++;
      else
        rfcnt++;
      if (lcnt > rfcnt)
        return false;
    }
    return true;
  }
};

int main() {
  std::string s{"()()((()))(("};
  std::string locked{"111111101101"};
  Solution sol;
  std::cout << sol.canBeValid(s, locked) << std::endl;
};
