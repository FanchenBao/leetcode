#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int maxScoreSightseeingPair(vector<int> &values) {
    /*
     * LeetCode 1014
     *
     * The sum that we want to find can be rearranged to (values[i] + i) +
     * (values[j] - j) We go through values from right to left. For each
     * values[i], we find its values[i] + i. Then we add to it the max values[j]
     * - j where j > i. This can be found via suffix max.
     *
     * O(N)
     */
    int N = values.size();
    int sufmax = values[N - 1] - (N - 1);
    int res = 0;
    for (int i = N - 2; i >= 0; i--) {
      res = std::max(res, values[i] + i + sufmax);
      sufmax = std::max(sufmax, values[i] - i);
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
