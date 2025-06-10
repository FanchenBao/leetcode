#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int count(int n, long long lo, long long hi) {
    int res = 0;
    while (lo <= n) {
      res += std::min((long long)n + 1, hi) - lo;
      lo *= 10;
      hi *= 10;
    }
    return res;
  }

  int findKthNumber(int n, int k) {
    /*
     * LeetCode 440 (Fail)
     *
     * I failed this problem in Sep, 2024. I promised myself to revisit it,
     * but I have not done so until this problem popps again on the daily
     * challenge. Now I read the editorial and understand the method.
     *
     * Basically, we want to find all the numbers between cur and cur + 1,
     * with cur inclusive but cur + 1 not.
     *
     * This can be done by thinking about the layout of the numbers as a prefix
     * tree, where cur is the root and all its children are cur * 10 ,
     * cur * 10 + 1, cur * 10 + 2,... cur * 10 + 9.
     *
     * To find the count of numbers between cur and cur + 1, we count the
     * numbers on the level, then move on to the next level, and so on, until
     * the beginning of a level is larger than n.
     *
     * Once the count is available, we will know whether the kth number is
     * within the tree rooted at cur or not. If not, we move on to the next
     * subtree. Otherwise, we drill down cur by mulitplying it by 10.
     */
    long long cur = 1;
    while (k > 0) {
      int cnt = count(n, cur, cur + 1);
      if (cnt <= k) {
        k -= cnt;
        if (k == 0)
          break;
        cur++;
      } else {
        // drill down to the next level
        k--;
        cur *= 10;
      }
    }
    return cur;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
