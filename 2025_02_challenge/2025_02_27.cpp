#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  int lenLongestFibSubseq(vector<int> &arr) {
    /*
     * LeetCode 873
     *
     * dp[i][j] is the max length fib subseq ending at arr[i] with the previous
     * value being arr[j]
     *
     * dp[i][j] = 1 + dp[j][index of arr[i] - arr[j]]
     *
     * If arr[i] - arr[j] is not in the arr, we default dp[j][index of arr[i] -
     * arr[j]] to 1.
     *
     * O(N^2), 351 ms, 39.10%
     */
    int N = arr.size();
    std::unordered_map<int, int> atoi;
    atoi[arr[0]] = 0;
    int res = 0;
    std::vector<std::vector<int>> dp(N, std::vector<int>(N, 1));
    for (int i = 1; i < N; i++) {
      atoi[arr[i]] = i;
      for (int j = i - 1; j >= 0; j--) {
        int diff = arr[i] - arr[j];
        if (atoi.contains(diff))
          dp[i][j] += dp[j][atoi[diff]];
        else
          dp[i][j] += 1;
        res = std::max(res, dp[i][j]);
      }
    }
    return res >= 3 ? res : 0;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
