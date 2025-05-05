#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int numEquivDominoPairs(vector<vector<int>> &dominoes) {
    /*
     * LeetCode 1128
     *
     * Use counter
     *
     * O(N), 8 ms 35%
     */
    int max = 9;
    std::vector<std::vector<int>> counter(max + 1, std::vector<int>(max + 1));
    for (auto p : dominoes)
      counter[std::min(p[0], p[1])][std::max(p[0], p[1])]++;
    int res = 0;
    for (int i = 1; i <= max; i++) {
      for (int j = i; j <= max; j++)
        res += counter[i][j] * (counter[i][j] - 1) / 2;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
