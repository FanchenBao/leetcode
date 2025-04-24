#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  int digitsum(int n) {
    int res = 0;
    while (n > 0) {
      res += n % 10;
      n /= 10;
    }
    return res;
  }

  int countLargestGroup(int n) {
    /*
     * LeetCode 1399
     *
     * Counter with the key being the digit sum.
     *
     * O(N), 0 ms, 100%
     */
    std::vector<int> counter(37);
    for (int i = 1; i <= n; i++)
      counter[digitsum(i)]++;

    int res = 0;
    int max_size = 0;
    for (int v : counter) {
      if (v > max_size) {
        max_size = v;
        res = 1;
      } else if (v == max_size) {
        res++;
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
