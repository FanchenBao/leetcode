#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool canChange(string start, string target) {
    /*
     * LeetCode 2337
     *
     * Two pointers. We go from left to right for both pointes. When both
     * pointers point to a non-empty letter, we check. If they are not the
     * same, it's impossible to make the change.
     *
     * If they are the same, depending on the relative position between i and
     * j and the current letter, we have different outcome. If we are talking
     * about L, and i is to the left of j, then start[i] will never be able
     * to reach the position of j. Thus it is impossible. Similarly, if we
     * are talking about R and i is to the right of j, then it is also not
     * possible.
     *
     * O(N), 12 ms, faster than 51.15%
     */
    int j = 0;
    for (int i = 0; i < start.length(); i++) {
      while (j < target.length() && target[j] == '_')
        j++;
      if (start[i] != '_') {
        if (start[i] != target[j] || (start[i] == 'L' && i < j) ||
            (start[i] == 'R' && i > j))
          return false;
        j++;
      }
    }
    while (j < target.length() && target[j] == '_')
      j++;
    return j == target.length();
  }
};

int main() {
  std::string start = "_L__R__R_";
  std::string target = "L______RR";
  Solution sol;
  std::cout << sol.canChange(start, target) << std::endl;
}
