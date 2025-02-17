#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool backtrack(int idx, std::vector<int> &res, std::vector<bool> &seen,
                 int n) {
    // Check whether we have placed all the values
    if (idx == res.size()) {
      for (bool s : seen) {
        if (!s)
          return false;
      }
      return true;
    }
    for (int c = n; c >= 1; c--) {
      if (seen[c] || (c != 1 && (idx + c >= res.size() || res[idx + c])))
        continue;
      if (c == 1) {
        seen[c] = true;
        res[idx] = c;
      } else {
        seen[c] = true;
        res[idx] = c;
        res[idx + c] = c;
      }
      int i = idx + 1;
      while (i < res.size() && res[i] != 0)
        i++;
      if (backtrack(i, res, seen, n))
        return true;
      // failed, let's backtrack
      seen[c] = false;
      res[idx] = 0;
      if (c != 1)
        res[idx + c] = 0;
    }
    return false;
  }

  vector<int> constructDistancedSequence(int n) {
    /*
     * LeetCode 1718
     *
     * Pure backtracking. Run time will be awful. O(N!)
     * 0 ms
     */
    std::vector<int> res(2 * n - 1);
    std::vector<bool> seen(n + 1);
    seen[0] = true;
    backtrack(0, res, seen, n);
    return res;
  }
};

int main() {
  int n = 11;
  Solution sol;
  sol.constructDistancedSequence(n);
}
