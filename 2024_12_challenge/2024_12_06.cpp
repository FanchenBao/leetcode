#include <algorithm>
#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  int maxCount(vector<int> &banned, int n, int maxSum) {
    /*
     * LeetCode 2554
     *
     * Two pointers again.
     *
     * O(MlogM + N), 54 ms, faster than 87.79%
     */
    int i = 0, sum = 0, j = 1, res = 0;
    int bannedLen = banned.size();
    std::sort(banned.begin(), banned.end());
    while (j <= n && sum <= maxSum) {
      while (i < bannedLen && i > 0 && banned[i] == banned[i - 1])
        i++;
      if (i < bannedLen && j == banned[i]) {
        i++;
      } else {
        sum += j;
        res++;
      }
      j++;
    }
    return sum <= maxSum ? res : res - 1;
  }
};

class Solution2 {
public:
  int maxCount(vector<int> &banned, int n, int maxSum) {
    /*
     * This solution uses a set. It's easier to write and technically faster
     * but I am not sure whether the overhead of a set will neutralize the
     * performance boost of not having to sort.
     *
     * O(M + N). 156 ms, faster than 75.57%
     *
     * Although time complexity is better, this solution is slower due to the
     * overhead of set operations.
     */
    std::unordered_set<int> bannedSet(banned.begin(), banned.end());
    int res = 0;
    for (int i = 1; i <= n; i++) {
      if (!bannedSet.contains(i)) {
        maxSum -= i;
        if (maxSum >= 0)
          res++;
        else
          break;
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
