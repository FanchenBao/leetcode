#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int numberOfSubstrings(string s) {
    /*
     * LeetCode 1358
     *
     * Sliding window. Given s[i], find the first s[j] such that s[i:j + 1]
     * contains a, b, and c. Then the number of substrings that satisfy the
     * requirement is s.size() - j + 1. We iterate through all i and add up
     * the count for each i.
     *
     * O(N), 13 ms, 42.54%
     */
    int res = 0;
    int j = 0;
    std::vector<int> counter(3, 0);
    for (int i = 0; i < s.size(); i++) {
      while (j < s.size() && counter[0] * counter[1] * counter[2] == 0) {
        counter[s[j++] - 'a']++; // j moves forward
      }
      if (counter[0] * counter[1] * counter[2] != 0)
        res += s.size() - j + 1;
      counter[s[i] - 'a']--; // i moves forward
    }
    return res;
  }
};

class Solution2 {
public:
  int numberOfSubstrings(string s) {
    /*
     * This is from the editorial. The method is called last position
     * tracking. We keep track of the latest index of a, b, and c. Then
     * the number of substrings ending at s[i] that contais all three
     * letters is the smallest latest index plus one.
     *
     * O(N), 0 ms
     */
    std::vector<int> last_indice(3, -1);
    int res = 0;
    for (int i = 0; i < s.size(); i++) {
      last_indice[s[i] - 'a'] = i;
      res += 1 + std::min({last_indice[0], last_indice[1], last_indice[2]});
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
