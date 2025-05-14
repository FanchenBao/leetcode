#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int lengthAfterTransformations(string s, int t) {
    /*
     * LeetCode 3335
     *
     * Use a counter to keep track how many digits are going to wrap around
     * under how many turns.
     *
     * For example, z will wrap around in one turn, thus if there are three
     * z's, we record counter[1] = 3.
     *
     * At each round, we update the counter. The final answer is tjhe sum of
     * all the values in the counter.
     *
     * O(26N), 82 ms, 79.80%
     */
    int MOD = 1000000007;
    std::vector<long long> counter(27);
    for (char c : s) {
      counter['z' - c + 1]++;
    }
    long long tmp = 0;
    for (int i = 0; i < t; i++) {
      tmp = counter[1];
      counter[1] = 0;
      for (int j = 2; j <= 26; j++) {
        counter[j - 1] = counter[j];
        counter[j] = 0;
      }
      counter[26] = (counter[26] + tmp) % MOD;
      counter[25] = (counter[25] + tmp) % MOD;
    }
    long long res = 0;
    for (long long c : counter) {
      res = (res + c) % MOD;
    }
    return (int)res;
  }
};

int main() {
  std::string s = "abcyy";
  int t = 2;
  Solution sol;
  std::cout << sol.lengthAfterTransformations(s, t) << std::endl;
}
