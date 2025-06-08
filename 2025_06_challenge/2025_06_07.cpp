#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  string clearStars(string s) {
    /*
     * LeetCode 3170
     *
     * We keep track of the indices of all letters. Each time when a '*' is
     * encountered, we go through the indices and delete the largest index of
     * the smallest letter.
     *
     * O(N), 46 ms, 87.34%
     */
    std::vector<std::vector<int>> indices(26);
    std::vector<bool> deleted(s.size());
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '*') {
        for (int j = 0; j < 26; j++) {
          if (!indices[j].empty()) {
            deleted[indices[j].back()] = true;
            indices[j].pop_back();
            break;
          }
        }
      } else {
        indices[s[i] - 'a'].push_back(i);
      }
    }
    std::string res;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '*' || deleted[i]) {
        continue;
      } else {
        res.push_back(s[i]);
      }
    }
    return res;
  }
};

class Solution2 {
public:
  string clearStars(string s) {
    /*
     * The editorial has the exact same solution EXCEPT that it directly
     * assigns '*' to s where the position should be deleted. This avoids the
     * use of an extra deleted array. This is something I do not know. I am
     * not aware that in C++ one can directly use [] operator to assign a
     * char to a string. But now I know.
     *
     * O(N), 4 ms, 98.38%
     */
    std::vector<std::vector<int>> indices(26);
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '*') {
        for (int j = 0; j < 26; j++) {
          if (!indices[j].empty()) {
            s[indices[j].back()] = '*';
            indices[j].pop_back();
            break;
          }
        }
      } else {
        indices[s[i] - 'a'].push_back(i);
      }
    }
    std::string res;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '*') {
        continue;
      } else {
        res.push_back(s[i]);
      }
    }
    return res;
  }
};

int main() {
  std::string s = "ee**";
  Solution sol;
  std::cout << sol.clearStars(s) << std::endl;
}
