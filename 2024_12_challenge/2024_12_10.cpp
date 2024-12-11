#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  int maximumLength(string s) {
    /*
     * LeetCode 2981
     *
     * Binary search. For each potential special substring length, we use
     * sliding window to find the max number of repeats of a potential special
     * substring.
     *
     * O(NlogN), 7 ms, faster than 83.54%
     */
    std::unordered_map<char, int> le_freq;
    std::unordered_map<char, int> str_count;
    int N = s.length();
    int lo = 0, hi = N - 1;
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      le_freq.clear();
      str_count.clear();
      for (int i = 0; i < N; i++) {
        le_freq[s[i]]++;
        if (i + 1 > mid) {
          le_freq[s[i - mid]]--;
          if (le_freq[s[i - mid]] == 0)
            le_freq.erase(s[i - mid]);
        }
        if (i + 1 >= mid && le_freq.size() == 1) {
          // special string
          char le = le_freq.begin()->first;
          str_count[le]++;
        }
      }
      int count = 0;
      for (const auto &pair : str_count)
        count = std::max(pair.second, count);
      if (count >= 3)
        lo = mid + 1;
      else
        hi = mid;
    }
    return lo - 1;
  }
};

int main() {
  std::string s{"aaaa"};
  Solution sol;
  std::cout << sol.maximumLength(s) << std::endl;
}
