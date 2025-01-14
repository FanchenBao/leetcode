#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int minimumLength(string s) {
    /*
     * LeetCode 3223
     *
     * First, we obtain the frequency of each letter.
     *
     * Then we realize that there is a pattern.
     * Given 1 letter, after removeal we have 1.
     * 2 => 2
     * 3 => we pick one letter and remove two, which becomes 1
     * 4 => we pick one letter and remove two, the remaining two letters produce
     * 2 5 => 5 - 2 => 1 6 => 6 - 2 => 2
     * ...
     * odd => 1
     * even => 2
     *
     * Thus we go through all the frequencies and add 1 if the frequency is odd
     * or add 2 if it is even.
     *
     * O(N), 11 ms, 77.02%
     */
    std::vector<int> counter(26);
    for (char c : s)
      counter[c - 'a']++;
    int res = 0;
    for (int c : counter) {
      if (c != 0)
        res += c % 2 == 0 ? 2 : 1;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
