#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <vector>

using namespace std;

class Solution1 {
public:
  int mincostTickets(vector<int> &days, vector<int> &costs) {
    /*
     * LeetCode 983
     *
     * DP, where dp[i] is the min cost of traveling every day in days[i:].
     *
     * To compute dp[i], we can choose to use 1, 7 or 30 day pass, then find
     * the first day that is not covered by the chosen pass. Since the min
     * cost of covering the first day has already been computed, we can use
     * the previously computed value for finding the min cost of dp[i].
     *
     * O(N * 3 * log(N)), 3 ms Beats 26.60%
     */
    int N = days.size();
    std::vector<int> dp(N + 1, 1000000000);
    dp[N] = 0;
    std::vector<int> pass_days{1, 7, 30};
    for (int i = N - 1; i >= 0; i--) {
      for (int j = 0; j < 3; j++) {
        int end_day = days[i] + pass_days[j] - 1;
        auto it = std::upper_bound(days.begin(), days.end(), end_day);
        dp[i] = std::min(dp[i], dp[std::distance(days.begin(), it)] + costs[j]);
      }
    }
    return dp[0];
  }
};

class Solution2 {
public:
  int mincostTickets(vector<int> &days, vector<int> &costs) {
    /*
     * Same as solution1, but instead of binary search, we just loop through
     * the days vector to find the smallest day that is larger than the reach
     * of the chosen pass. Maybe the reduced overhead of binary search can
     * make this solution even faster.
     *
     * O(3N^2), 0 ms Beats 100.00%
     */
    int N = days.size();
    std::vector<int> dp(N + 1, 1000000000);
    dp[N] = 0;
    std::vector<int> pass_days{1, 7, 30};
    for (int i = N - 1; i >= 0; i--) {
      for (int j = 0; j < 3; j++) {
        int end_day = days[i] + pass_days[j] - 1;
        int k = i + 1;
        while (k < N && days[k] <= end_day)
          k++;
        dp[i] = std::min(dp[i], dp[k] + costs[j]);
      }
    }
    return dp[0];
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
