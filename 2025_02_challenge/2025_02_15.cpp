#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

class Solution {

public:
  bool is_ok(int x) {
    int xx = x * x;
    std::string xxstr = std::to_string(xx);
    std::vector<std::vector<int>> dp(xxstr.size());
    for (int i = 0; i < xxstr.size(); i++) {
      int cur = xxstr[i] - '0';
      for (int j = i - 1; j >= 0; j--) {
        for (int pre : dp[j])
          dp[i].push_back(pre + cur);
        cur = cur + std::pow(10, i - j) * (xxstr[j] - '0');
      }
      dp[i].push_back(cur);
    }
    for (int v : dp[xxstr.size() - 1]) {
      if (v == x)
        return true;
    }
    return false;
  }

  int punishmentNumber(int n) {
    /*
     * LeetCode 2698
     *
     * Use DP to decide whether a number x is equal to some substring sum of
     * the decimal representation of its squared value.
     *
     * O(NlogN), 385 ms, 16.37%
     */
    int res = 0;
    for (int i = 1; i <= n; i++) {
      if (is_ok(i))
        res += i * i;
    }
    return res;
  }
};

class Solution2 {

public:
  std::vector<int> valid;

  Solution2() {
    for (int i = 1; i <= 1000; i++) {
      if (is_ok(i))
        valid.push_back(i);
    }
    for (int v : valid)
      std::cout << v << ", ";
  }

  bool is_ok(int x) {
    int xx = x * x;
    std::string xxstr = std::to_string(xx);
    std::vector<std::vector<int>> dp(xxstr.size());
    for (int i = 0; i < xxstr.size(); i++) {
      int cur = xxstr[i] - '0';
      for (int j = i - 1; j >= 0; j--) {
        for (int pre : dp[j])
          dp[i].push_back(pre + cur);
        cur = cur + std::pow(10, i - j) * (xxstr[j] - '0');
      }
      dp[i].push_back(cur);
    }
    for (int v : dp[xxstr.size() - 1]) {
      if (v == x)
        return true;
    }
    return false;
  }

  int punishmentNumber(int n) {
    /*
     * Try pre-computing all valid numbers from 1 to 1000.
     *
     * 979 ms, apparently the Solution object is created on the fly
     */
    int res = 0;
    for (int i = 0; i < valid.size() && valid[i] <= n; i++)
      res += valid[i] * valid[i];
    return res;
  }
};

class Solution3 {

public:
  std::vector<int> valid{1,   9,   10,  36,  45,  55,  82,  91,  99,  100,
                         235, 297, 369, 370, 379, 414, 657, 675, 703, 756,
                         792, 909, 918, 945, 964, 990, 991, 999, 1000};

  int punishmentNumber(int n) {
    /*
     * Truly pre-computed, 0 ms
     */
    int res = 0;
    for (int i = 0; i < valid.size() && valid[i] <= n; i++)
      res += valid[i] * valid[i];
    return res;
  }
};

int main() {
  int n = 10;
  Solution2 sol;
  std::cout << sol.punishmentNumber(n) << std::endl;
}
