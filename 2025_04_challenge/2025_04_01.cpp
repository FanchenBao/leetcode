#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  long long mostPoints(vector<vector<int>> &questions) {
    /*
     * LeetCode 2140
     *
     * DP, wherre dp[i] is the max points scored from questions[i:]
     *
     * O(N), 0 ms, 100%
     */
    int N = questions.size();
    std::vector<long long> dp(N, 0);
    dp[N - 1] = (long long)questions[N - 1][0];
    for (int i = N - 2; i >= 0; i--) {
      // option 1, skip
      dp[i] = dp[i + 1];
      // option 2, solve question[i]
      int j = questions[i][1];
      dp[i] = std::max(dp[i], (long long)questions[i][0] +
                                  (i + j + 1 >= N ? 0 : dp[i + j + 1]));
    }
    return dp[0];
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
