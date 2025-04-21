#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  int numRabbits(vector<int> &answers) {
    /*
     * LeetCode 781
     *
     * This is a little bit brainteaser. All the rabbits that report the same
     * number SHOULD have the same color. However, if the count of the rabbits
     * with the same number exceeds the number they report, we need to break
     * the rabbits into separate groups.
     *
     * O(NlogN), 0 ms
     */
    std::sort(answers.begin(), answers.end());
    int res = 0, cnt = 1, group_limit = answers[0] + 1;
    for (int i = 1; i < answers.size(); i++) {
      if (answers[i] == answers[i - 1] && cnt + 1 <= group_limit) {
        cnt++;
      } else {
        res += group_limit;
        cnt = 1, group_limit = answers[i] + 1;
      }
    }
    return res + group_limit;
  }
};

int main() {
  std::vector<int> arr{10, 2, 5, 3};
  Solution sol;
  std::cout << sol.checkIfExist(arr) << std::endl;
}
