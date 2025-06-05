#include <algorithm>
#include <deque>
#include <iostream>
#include <set>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  string answerString(string word, int numFriends) {
    /*
     * LeetCode 3403
     *
     * Find the positions of all the largest letters. Then starting from them,
     * move one letter to the right. Then find the largest letters again, and
     * repeat, until the limit size is hit. The limit size = len(word) -
     * (numFriends - 1). We must respect this limit because the split string
     * cannot be empty.
     *
     * O(N), 263 ms, 5.60%
     */
    if (numFriends == 1)
      return word;
    int limit = word.size() - (numFriends - 1);
    int max_letter = 0;
    std::vector<std::pair<int, int>> queue;
    for (int i = 0; i < word.size(); i++) {
      char c = word[i];
      if (c - 'a' > max_letter) {
        max_letter = c - 'a';
        queue.clear();
        queue.push_back({i, i});
      } else if (c - 'a' == max_letter) {
        queue.push_back({i, i});
      }
    }
    for (int cur_size = 2; cur_size <= limit && queue.size() > 1; cur_size++) {
      std::vector<std::pair<int, int>> tmp;
      max_letter = 0;
      for (const auto &p : queue) {
        int idx = p.second;
        if (idx + 1 < word.size()) {
          char c = word[idx + 1];
          if (c - 'a' > max_letter) {
            max_letter = c - 'a';
            tmp.clear();
            tmp.push_back({p.first, idx + 1});
          } else if (c - 'a' == max_letter) {
            tmp.push_back({p.first, idx + 1});
          }
        }
      }
      queue = std::move(tmp);
    }
    return word.substr(queue[0].first, limit);
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
