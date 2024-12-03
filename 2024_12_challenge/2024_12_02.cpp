#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  int isPrefixOfWord(string sentence, string searchWord) {
    /*
     * LeetCode 1455
     *
     * Use stringstream to split sentence by empty space (see
     * https://www.geeksforgeeks.org/how-to-split-string-by-delimiter-in-cpp/)
     * Then use starts_with to chekc whether searchWord is a prefix.
     *
     * O(NM), where N = len(sentence) and M = len(searchWord), 0 ms, faster than
     * 100.00%
     */
    std::stringstream ss(sentence);
    int cnt = 0;
    for (std::string tmp; std::getline(ss, tmp, ' ');) {
      cnt++;
      if (tmp.starts_with(searchWord))
        return cnt;
    }
    return -1;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
