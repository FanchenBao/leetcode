#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  long long countOfSubstrings(string word, int k) {
    /*
     * LeetCode 3306
     *
     * Sliding window with two pointers.
     *
     * O(N), 210 ms, 43.56%
     */
    long long res = 0;
    std::unordered_map<char, int> counter;
    std::set<char> vowels{'a', 'e', 'i', 'o', 'u'};
    int i = 0, cc = 0;
    // pre and cur is the number of valid substring ending at the previous and
    // current letter
    long long pre = 0, cur = 0;
    for (int j = 0; j < word.size(); j++) {
      cur = 0;
      if (vowels.contains(word[j])) {
        counter[word[j]]++;
        cur = pre;
      } else {
        cc++;
      }
      // reduce the window to exactly k consonants
      while (cc > k && i < j) {
        if (vowels.contains(word[i])) {
          counter[word[i]]--;
          if (counter[word[i]] == 0)
            counter.erase(word[i]);
        } else {
          cc--;
        }
        i++;
      }
      // shrink until word[i:j+1] is not valid
      while (cc == k && counter.size() == vowels.size() && i < j) {
        cur++;
        if (vowels.contains(word[i])) {
          counter[word[i]]--;
          if (counter[word[i]] == 0)
            counter.erase(word[i]);
        } else {
          cc--;
        }
        i++;
      }
      res += cur;
      pre = cur;
    }
    return res;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
