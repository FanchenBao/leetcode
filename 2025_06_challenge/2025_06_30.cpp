#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int possibleStringCount(string word) {
    /*
     * LeetCode 3330
     *
     * Count the consecutive frequencies
     */
    int res = 1, consec = 1;
    for (int i = 1; i < word.size(); i++) {
      if (word[i] == word[i - 1]) {
        consec++;
      } else {
        res += consec - 1;
        consec = 1;
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
