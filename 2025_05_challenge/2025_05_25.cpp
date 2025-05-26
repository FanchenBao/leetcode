#include <algorithm>
#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  int longestPalindrome(vector<string> &words) {
    /*
     * LeetCode 2131
     *
     * Counter words, and find the matching pairs: ab matches ba. When we have
     * a word that is a repeat: cc, and its count is odd, we only allow one
     * odd count to go towards the palindrome. For example, if we have three
     * cc, and three dd, we can do three cc + two dd, or two cc + three dd.
     *
     * O(N), 30 ms, 82.10%
     */
    std::unordered_map<std::string, int> counter;
    for (const auto &w : words)
      counter[w]++;
    int res = 0;
    for (const auto &[k, v] : counter) {
      if (v > 0) {
        if (k[0] == k[1]) {
          res += v / 2 * 2;
          res += (res % 2 == 0) * (v % 2);
        } else {
          std::string rev(k.rbegin(), k.rend());
          // cannot use counter[rev] when rev is not in the counter, because
          // the default [] operator initializes a new key-value pair when the
          // key is not in the map. This intialization may break the iteration
          // and lead to early termination of the iteration.
          int rev_cnt = counter.contains(rev) ? counter[rev] : 0;
          res += std::min(v, rev_cnt) * 2;
          if (rev_cnt)
            counter[rev] = 0;
        }
      }
    }
    return res * 2;
  }
};

int main() {
  std::vector<string> words{
      "oo", "vv", "uu", "gg", "pp", "ff", "ss", "yy", "vv", "cc", "rr",
      "ig", "jj", "uu", "ig", "gb", "zz", "xx", "ff", "bb", "ii", "dd",
      "ii", "ee", "mm", "qq", "ig", "ww", "ss", "tt", "vv", "oo", "ww",
      "ss", "bi", "ff", "gg", "bi", "jj", "ee", "gb", "qq", "bg", "nn",
      "vv", "oo", "bb", "pp", "ww", "qq", "mm", "ee", "tt", "hh", "ss",
      "tt", "ee", "gi", "ig", "uu", "ff", "zz", "ii", "ff", "ss", "gi",
      "yy", "gb", "mm", "pp", "uu", "kk", "jj", "ee"};
  Solution sol;
  std::cout << sol.longestPalindrome(words) << std::endl;
}
