#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> lexicalOrder(int n) {
    /*
     * LeetCode 386
     *
     * Check the current number. If it is within range, add it to the result.
     * Then append a zero to it. Otherwise, pop the last digit then increment
     * by one. If the increment leads to the last digit being zero, we need to
     * pop it because the prefix has not been considered yet.
     *
     * 0 ms
     */
    std::vector<int> res;
    int cur = 1;
    while (res.size() < n) {
      if (cur <= n) {
        res.push_back(cur);
        cur *= 10;
      } else {
        cur /= 10;
        cur += 1;
        while (cur % 10 == 0) // need to consider the prefix first
          cur /= 10;
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
