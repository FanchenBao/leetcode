#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minimumRecolors(string blocks, int k) {
    /*
     * LeetCode 2379
     *
     * This is a classic sliding window problem.
     *
     * O(N)
     */
    int cntB = 0, res = 1000;
    int i = 0;
    for (int j = 0; j < blocks.size(); j++) {
      cntB += (int)(blocks[j] == 'B');
      if (j - i + 1 > k)
        cntB -= (int)(blocks[i++] == 'B');
      res = std::min(res, k - cntB);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
