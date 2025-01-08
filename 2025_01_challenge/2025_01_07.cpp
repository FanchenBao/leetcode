#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<string> stringMatching(vector<string> &words) {
    /*
     * LeetCode 1408
     *
     * Brute force. O(N^2 * M), where N = len(words), and M is the average
     * length of each word.
     *
     * 4 ms, 31.92%
     */
    std::vector<string> res;
    std::sort(words.begin(), words.end(),
              [](string a, string b) { return a.size() < b.size(); });
    for (int i = 0; i < words.size(); i++) {
      for (int j = i + 1; j < words.size(); j++) {
        if (words[j].find(words[i]) != std::string::npos) {
          res.push_back(words[i]);
          break;
        }
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
