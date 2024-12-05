#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  bool canMakeSubsequence(string str1, string str2) {
    /*
     * LeetCode 2825
     *
     * Two pointers.
     *
     * O(N), 8 ms, faster than 26.52%
     *
     * UPDATE: exit early if str2 has been completely traversed. We can
     * significantly improve performance this way. 2 ms, faster than 72.38%
     *
     * UPDATE 2: there is an easier way to do the logic of checking. 8 ms,
     * faster than 26.52%
     */
    int j = 0;
    int str1_len = str1.length();
    int str2_len = str2.length();
    for (int i = 0; i < str1_len && j < str2_len; i++) {
      if (str2[j] == str1[i] || str2[j] == str1[i] + 1 ||
          str2[j] == str1[i] - 25) {
        j++;
      }
    }
    return j == str2.length();
  }
};

int main() {
  std::string str1 = "abc";
  std::string str2 = "ad";
  Solution sol;
  std::cout << sol.canMakeSubsequence(str1, str2) << std::endl;
}
